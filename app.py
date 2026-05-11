from flask import Flask, render_template, request

from src.data_utils import load_data, apply_filters, get_filter_options
from src.chart_utils import create_dashboard_charts
from src.ml_utils import (
    NUMERIC_COLUMNS,
    MODEL_OPTIONS,
    run_ml_benchmark,
    compare_models
)


app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the main dashboard page.
    """

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

    avg_moisture = (
        round(df["moisture"].mean(), 2)
        if sample_count > 0
        else 0
    )

    charts = create_dashboard_charts(df)

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
        chart=charts["temperature_moisture"],
        bar_chart=charts["country_moisture"],
        hist_chart=charts["organic_carbon"],
        risk_chart=charts["risk_level"],
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