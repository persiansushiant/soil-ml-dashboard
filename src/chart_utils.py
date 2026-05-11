import plotly.express as px


def create_temperature_moisture_chart(df):
    """
    Create an interactive scatter plot for temperature vs moisture.
    """

    fig = px.scatter(
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

    return fig.to_html(full_html=False)


def create_country_moisture_chart(df):
    """
    Create a bar chart showing average moisture per country.
    """

    avg_by_country = (
        df.groupby("country", as_index=False)["moisture"]
        .mean()
        .sort_values("moisture", ascending=False)
    )

    fig = px.bar(
        avg_by_country,
        x="country",
        y="moisture",
        title="Average Moisture per Country"
    )

    return fig.to_html(full_html=False)


def create_organic_carbon_histogram(df):
    """
    Create a histogram for organic carbon distribution.
    """

    fig = px.histogram(
        df,
        x="organic_carbon",
        nbins=8,
        title="Organic Carbon Distribution"
    )

    return fig.to_html(full_html=False)


def create_risk_level_chart(df):
    """
    Create a bar chart showing the count of each risk level.
    """

    risk_counts = (
        df["risk_level"]
        .value_counts()
        .reset_index()
    )

    risk_counts.columns = [
        "risk_level",
        "count"
    ]

    fig = px.bar(
        risk_counts,
        x="risk_level",
        y="count",
        title="Soil Risk Level Counts"
    )

    return fig.to_html(full_html=False)


def create_dashboard_charts(df):
    """
    Create all charts used by the dashboard.

    Returns
    -------
    dict
        HTML strings for dashboard charts.
    """

    return {
        "temperature_moisture": create_temperature_moisture_chart(df),
        "country_moisture": create_country_moisture_chart(df),
        "organic_carbon": create_organic_carbon_histogram(df),
        "risk_level": create_risk_level_chart(df)
    }