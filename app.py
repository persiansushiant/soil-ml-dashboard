from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():

    df = pd.read_csv("soil_data.csv")

    sample_count = len(df)

    avg_moisture = (
        df["moisture"]
        .mean()
    )

    return render_template(
        "index.html",
        sample_count=sample_count,
        avg_moisture=avg_moisture
    )


if __name__ == "__main__":
    app.run(debug=True)