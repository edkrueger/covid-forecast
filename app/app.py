"""The App."""

import os

from matplotlib import pyplot as plt

import streamlit as st  # pylint: disable=import-error
from load_data import load_data

FILEPATH = os.path.join(os.getcwd(), "app", "data.json")

CASES = "Cumulative Cases"
DEATHS = "Cumulative Deaths"
RECOVERIES = "Cumulative Recoveries"


df = load_data(FILEPATH)
st.write("# COVID Forecast")

selected_series = st.selectbox("Select a data set:", (CASES, DEATHS, RECOVERIES, "All"))

if selected_series == CASES:
    series = df["cumulative_cases"]
    plt.title("Global Cumulative Cases")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.plot(series.index, series.values)
    st.pyplot()

if selected_series == DEATHS:
    series = df["cumulative_deaths"]
    plt.title("Global Cumulative Deaths")
    plt.xlabel("Date")
    plt.ylabel("Deaths")
    plt.plot(series.index, series.values)
    st.pyplot()

if selected_series == RECOVERIES:
    series = df["cumulative_recoveries"]
    plt.title("Global Cumulative Recoveries")
    plt.xlabel("Date")
    plt.ylabel("Recoveries")
    plt.plot(series.index, series.values)
    st.pyplot()

if selected_series == "All":
    cases_series = df["cumulative_cases"]
    deaths_series = df["cumulative_deaths"]
    recoveries_series = df["cumulative_recoveries"]

    plt.title("Global Cumulative Series")
    plt.xlabel("Date")
    plt.ylabel("Cases")
    plt.plot(cases_series.index, cases_series.values, label=CASES)
    plt.plot(deaths_series.index, deaths_series.values, label=DEATHS)
    plt.plot(recoveries_series.index, recoveries_series.values, label=RECOVERIES)
    plt.legend()

    st.pyplot()
