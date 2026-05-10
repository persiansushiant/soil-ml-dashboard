from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

app = Flask(__name__)


def classify_risk(moisture):
    if moisture < 10:
        return "High Risk"
    elif moisture <= 20:
        return "Medium Risk"
    else:
        return "Low Risk"


def load_data():
    df = pd.read_csv("soil_data.csv")
    df["risk_level"] = df["moisture"].apply(classify_risk)
    return df


def apply_filters(df, country=None, soil_type=None):
    filtered_df = df.copy()

    if country:
        filtered_df = filtered_df[filtered_df["country"] == country]

    if soil_type:
        filtered_df = filtered_df[filtered_df["soil_type"] == soil_type]

    return filtered_df


def get_model(model_name):
    if model_name == "Linear Regression":
        return LinearRegression()

    if model_name == "Decision Tree":
        return DecisionTreeRegressor(random_state=42)

    if model_name == "Random Forest":
        return RandomForestRegressor(random_state=42, n_estimators=100)

    return LinearRegression()


def run_ml_benchmark(df, target, model_name):
    numeric_columns = [
        "moisture",
        "temperature",
        "ph",
        "organic_carbon",
        "nitrogen"
    ]

    feature_columns = [
        col for col in numeric_columns
        if col != target
    ]

    ml_df = df[numeric_columns].dropna()

    X = ml_df[feature_columns]
    y = ml_df[target]

    if len(ml_df) < 5:
        return None

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

    fig.add_shape(
        type="line",
        x0=results_df["actual"].min(),
        y0=results_df["actual"].min(),
        x1=results_df["actual"].max(),
        y1=results_df["actual"].max()
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


@app.route("/")
def home():
    original_df = load_data()

    selected_country = request.args.get("country")
    selected_soil_type = request.args.get("soil_type")
    selected_target = request.args.get("target")
    selected_model = request.args.get("model")

    df = apply_filters(
        original_df,
        country=selected_country,
        soil_type=selected_soil_type
    )

    countries = sorted(original_df["country"].unique())
    soil_types = sorted(original_df["soil_type"].unique())

    target_options = [
        "moisture",
        "temperature",
        "organic_carbon",
        "nitrogen",
        "ph"
    ]

    model_options = [
        "Linear Regression",
        "Decision Tree",
        "Random Forest"
    ]

    sample_count = len(df)
    avg_moisture = round(df["moisture"].mean(), 2) if sample_count > 0 else 0

    scatter_fig = px.scatter(
        df,
        x="temperature",
        y="moisture",
        color="soil_type",
        hover_data=["location", "country", "ph", "organic_carbon", "risk_level"],
        title="Temperature vs Moisture"
    )
    chart = scatter_fig.to_html(full_html=False)

    avg_by_country = (
        df.groupby("country", as_index=False)["moisture"]
        .mean()
        .sort_values("moisture", ascending=False)
    )

    bar_fig = px.bar(
        avg_by_country,
        x="country",
        y="moisture",
        title="Average Moisture per Country"
    )
    bar_chart = bar_fig.to_html(full_html=False)

    hist_fig = px.histogram(
        df,
        x="organic_carbon",
        nbins=8,
        title="Organic Carbon Distribution"
    )
    hist_chart = hist_fig.to_html(full_html=False)

    risk_counts = df["risk_level"].value_counts().reset_index()
    risk_counts.columns = ["risk_level", "count"]

    risk_fig = px.bar(
        risk_counts,
        x="risk_level",
        y="count",
        title="Soil Risk Level Counts"
    )
    risk_chart = risk_fig.to_html(full_html=False)

    ml_results = None
    if selected_target and selected_model and sample_count >= 5:
        ml_results = run_ml_benchmark(
            df,
            selected_target,
            selected_model
        )

    table = df.head(10).to_html(index=False)

    return render_template(
        "index.html",
        sample_count=sample_count,
        avg_moisture=avg_moisture,
        chart=chart,
        bar_chart=bar_chart,
        hist_chart=hist_chart,
        risk_chart=risk_chart,
        table=table,
        countries=countries,
        soil_types=soil_types,
        selected_country=selected_country,
        selected_soil_type=selected_soil_type,
        target_options=target_options,
        model_options=model_options,
        selected_target=selected_target,
        selected_model=selected_model,
        ml_results=ml_results
    )


@app.route("/api/summary")
def api_summary():
    original_df = load_data()

    selected_country = request.args.get("country")
    selected_soil_type = request.args.get("soil_type")

    df = apply_filters(
        original_df,
        country=selected_country,
        soil_type=selected_soil_type
    )

    sample_count = len(df)

    if sample_count == 0:
        return jsonify({
            "sample_count": 0,
            "message": "No data found for selected filters",
            "filters": {
                "country": selected_country,
                "soil_type": selected_soil_type
            }
        })

    summary = {
        "filters": {
            "country": selected_country,
            "soil_type": selected_soil_type
        },
        "sample_count": sample_count,
        "average_moisture": round(df["moisture"].mean(), 2),
        "average_temperature": round(df["temperature"].mean(), 2),
        "average_organic_carbon": round(df["organic_carbon"].mean(), 2),
        "risk_counts": df["risk_level"].value_counts().to_dict(),
        "soil_type_counts": df["soil_type"].value_counts().to_dict()
    }

    return jsonify(summary)


if __name__ == "__main__":
    app.run(debug=True)