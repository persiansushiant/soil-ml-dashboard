import pandas as pd


DATA_PATH = "data/soil_data.csv"


def classify_risk(moisture):
    """
    Classify soil moisture into a simple risk category.

    Parameters
    ----------
    moisture : float
        Soil moisture value.

    Returns
    -------
    str
        Risk category based on moisture level.
    """

    if moisture < 10:
        return "High Risk"

    if moisture <= 20:
        return "Medium Risk"

    return "Low Risk"


def load_data():
    """
    Load soil data from CSV and add derived analysis columns.

    Returns
    -------
    pandas.DataFrame
        Soil dataset with an additional risk_level column.
    """

    df = pd.read_csv(DATA_PATH)

    df["risk_level"] = df["moisture"].apply(classify_risk)

    return df


def apply_filters(df, country=None, soil_type=None):
    """
    Filter soil data by country and soil type.

    Parameters
    ----------
    df : pandas.DataFrame
        Input soil dataset.
    country : str, optional
        Country name to filter by.
    soil_type : str, optional
        Soil type to filter by.

    Returns
    -------
    pandas.DataFrame
        Filtered dataset.
    """

    filtered_df = df.copy()

    if country:
        filtered_df = filtered_df[
            filtered_df["country"] == country
        ]

    if soil_type:
        filtered_df = filtered_df[
            filtered_df["soil_type"] == soil_type
        ]

    return filtered_df


def get_filter_options(df):
    """
    Extract available filter options from the dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Soil dataset.

    Returns
    -------
    tuple
        Sorted countries and soil types.
    """

    countries = sorted(df["country"].unique())
    soil_types = sorted(df["soil_type"].unique())

    return countries, soil_types