"""Loads the data."""

import pandas as pd


def load_data(path):
    """Loads the dataset from a filepath."""
    return (
        pd.read_json(path)
        .rename(
            columns={
                "Total Results as of Date": "date",
                "Cases": "cumulative_cases",
                "Deaths": "cumulative_deaths",
                "Recovered": "cumulative_recovered",
            }
        )
        .assign(date=lambda df: pd.to_datetime(df["date"]))
        .set_index("date")
    )


if __name__ == "__main__":
    FILEPATH = "data.json"
    df = load_data(FILEPATH)
    print(df)
