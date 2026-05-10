from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

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


@app.route("/")
def home():
    original_df = load_data()

    selected_country = request.args.get("country")
    selected_soil_type = request.args.get("soil_type")

    df = apply_filters(
        original_df,
        country=selected_country,
        soil_type=selected_soil_type
    )

    countries = sorted(original_df["country"].unique())
    soil_types = sorted(original_df["soil_type"].unique())

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

    table = df.head(10).to_html(index=False)

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

    selected_target = request.args.get("target")
    selected_model = request.args.get("model")

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
        target_options=target_options,
        model_options=model_options,
        selected_target=selected_target,
        selected_model=selected_model,
        selected_soil_type=selected_soil_type
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