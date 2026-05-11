import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


NUMERIC_COLUMNS = [
    "moisture",
    "temperature",
    "ph",
    "organic_carbon",
    "nitrogen"
]


MODEL_OPTIONS = [
    "Linear Regression",
    "Decision Tree",
    "Random Forest"
]


def get_model(model_name):
    """
    Create a regression model based on a user-selected model name.
    """

    if model_name == "Linear Regression":
        return LinearRegression()

    if model_name == "Decision Tree":
        return DecisionTreeRegressor(random_state=42)

    if model_name == "Random Forest":
        return RandomForestRegressor(
            random_state=42,
            n_estimators=100
        )

    return LinearRegression()


def run_ml_benchmark(df, target, model_name):
    """
    Train a regression model and calculate benchmark metrics.
    """

    feature_columns = [
        col for col in NUMERIC_COLUMNS
        if col != target
    ]

    ml_df = df[NUMERIC_COLUMNS].dropna()

    if len(ml_df) < 5:
        return None

    X = ml_df[feature_columns]
    y = ml_df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.3,
        random_state=42
    )

    model = get_model(model_name)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, predictions)

    results_df = pd.DataFrame({
        "actual": y_test.values,
        "predicted": predictions
    })

    fig = px.scatter(
        results_df,
        x="actual",
        y="predicted",
        title=f"Actual vs Predicted: {target}"
    )

    prediction_chart = fig.to_html(full_html=False)

    return {
        "target": target,
        "model": model_name,
        "features": feature_columns,
        "mae": round(mae, 3),
        "rmse": round(rmse, 3),
        "r2": round(r2, 3),
        "prediction_chart": prediction_chart
    }


def compare_models(df, target):
    """
    Compare all supported regression models for a selected target.
    """

    results = []

    for model_name in MODEL_OPTIONS:
        result = run_ml_benchmark(
            df,
            target,
            model_name
        )

        if result:
            results.append({
                "model": model_name,
                "mae": result["mae"],
                "rmse": result["rmse"],
                "r2": result["r2"]
            })

    if not results:
        return None

    comparison_df = pd.DataFrame(results)

    fig = px.bar(
        comparison_df,
        x="model",
        y="r2",
        text="r2",
        title=f"Model Comparison for {target}"
    )

    comparison_chart = fig.to_html(full_html=False)
    comparison_table = comparison_df.to_html(index=False)

    best_model_row = (
        comparison_df
        .sort_values("r2", ascending=False)
        .iloc[0]
    )

    return {
        "chart": comparison_chart,
        "table": comparison_table,
        "best_model": best_model_row["model"],
        "best_r2": best_model_row["r2"]
    }