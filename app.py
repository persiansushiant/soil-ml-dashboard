from flask import Flask, render_template, request
import plotly.express as px

from src.data_utils import load_data, apply_filters, get_filter_options
from src.ml_utils import (
    NUMERIC_COLUMNS,
    MODEL_OPTIONS,
    run_ml_benchmark,
    compare_models
)


app = Flask(__name__)


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

    countries, soil_types = get_filter_options(original_df)

    sample_count = len(df)
    avg_moisture = round(df["moisture"].mean(), 2)

    scatter_fig = px.scatter(
        df,
        x="temperature",
        y="moisture",
        color="soil_type",
        hover_data=[
            "location",
            "country",
            "ph",
            "organic_carbon",
            "risk_level"
        ],
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

    risk_counts = (
        df["risk_level"]
        .value_counts()
        .reset_index()
    )

    risk_counts.columns = [
        "risk_level",
        "count"
    ]

    risk_fig = px.bar(
        risk_counts,
        x="risk_level",
        y="count",
        title="Soil Risk Level Counts"
    )

    risk_chart = risk_fig.to_html(full_html=False)

    ml_results = None
    model_comparison = None

    if selected_target and selected_model:
        ml_results = run_ml_benchmark(
            df,
            selected_target,
            selected_model
        )

    if selected_target:
        model_comparison = compare_models(
            df,
            selected_target
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
        target_options=NUMERIC_COLUMNS,
        model_options=MODEL_OPTIONS,
        selected_target=selected_target,
        selected_model=selected_model,
        ml_results=ml_results,
        model_comparison=model_comparison
    )


if __name__ == "__main__":
    app.run(debug=True)