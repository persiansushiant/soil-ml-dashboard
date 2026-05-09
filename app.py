from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)


@app.route("/")
def home():
    df = pd.read_csv("soil_data.csv")

    sample_count = len(df)
    avg_moisture = df["moisture"].mean()

    fig = px.scatter(
        df,
        x="temperature",
        y="moisture",
        color="soil_type",
        hover_data=["location", "country", "ph", "organic_carbon"],
        title="Temperature vs Moisture"
    )
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

    chart = fig.to_html(full_html=False)

    table = df.head(10).to_html(index=False)

    return render_template(
        "index.html",
        sample_count=sample_count,
        avg_moisture=avg_moisture,
        chart=chart,
        bar_chart=bar_chart,
        table=table
    )


if __name__ == "__main__":
    app.run(debug=True)