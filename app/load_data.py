"""Loads the data."""

import pandas as pd

import streamlit as st  # pylint: disable=import-error


@st.cache
def load_data(path):
    """Loads the dataset from a filepath."""
    return (
        pd.read_json(path)
        .rename(
            columns={
                "Total Results as of Date": "date",
                "Cases": "cumulative_cases",
                "Deaths": "cumulative_deaths",
                "Recovered": "cumulative_recoveries",
            }
        )
        .assign(date=lambda df: pd.to_datetime(df["date"]))
        .set_index("date")
    )
