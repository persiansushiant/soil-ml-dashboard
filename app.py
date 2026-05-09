from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

app = Flask(__name__)


@app.route("/")
def home():
    original_df = pd.read_csv("soil_data.csv")

    selected_country = request.args.get("country")
    selected_soil_type = request.args.get("soil_type")

    df = original_df.copy()

    if selected_country:
        df = df[df["country"] == selected_country]

    if selected_soil_type:
        df = df[df["soil_type"] == selected_soil_type]

    countries = sorted(original_df["country"].unique())
    soil_types = sorted(original_df["soil_type"].unique())

    sample_count = len(df)
    avg_moisture = round(df["moisture"].mean(), 2) if sample_count > 0 else 0

    scatter_fig = px.scatter(
        df,
        x="temperature",
        y="moisture",
        color="soil_type",
        hover_data=["location", "country", "ph", "organic_carbon"],
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

    table = df.head(10).to_html(index=False)

    return render_template(
        "index.html",
        sample_count=sample_count,
        avg_moisture=avg_moisture,
        chart=chart,
        bar_chart=bar_chart,
        table=table,
        countries=countries,
        soil_types=soil_types,
        selected_country=selected_country,
        selected_soil_type=selected_soil_type
    )
if __name__ == "__main__":
    app.run(debug=True)