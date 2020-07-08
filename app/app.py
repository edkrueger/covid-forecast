"""The App."""

import os

from matplotlib import pyplot as plt
from fbprophet import Prophet
from fbprophet.plot import plot_plotly

import streamlit as st  # pylint: disable=import-error
from load_data import load_data

FILEPATH = os.path.join(os.getcwd(), "app", "data.json")

ALL = "All Cumulaive Series - No Forecast"
CASES = "Cumulative Cases"
DEATHS = "Cumulative Deaths"
RECOVERIES = "Cumulative Recoveries"


@st.cache(allow_output_mutation=True)
def make_forecast(selection):
    """Takes a name from the selection and makes a forecast plot."""

    if selection == CASES:

        cumulative_series_name = "cumulative_cases"
        title = "Daily Cases"
        x_label = "Cases"

    if selection == DEATHS:

        cumulative_series_name = "cumulative_deaths"
        title = "Daily Deaths"
        x_label = "Deaths"

    if selection == RECOVERIES:

        cumulative_series_name = "cumulative_recoveries"
        title = "Daily Recoveries"
        x_label = "Recoveries"

    prophet_df = (
        df[cumulative_series_name]
        .diff()
        .dropna()
        .to_frame()
        .reset_index()
        .rename(columns={"date": "ds", cumulative_series_name: "y"})
    )

    model = Prophet()
    model.fit(prophet_df)
    future = model.make_future_dataframe(periods=90)
    forecast = model.predict(future)

    fig = plot_plotly(model, forecast)
    fig.update_layout(
        title=title, yaxis_title=x_label, xaxis_title="Date",
    )

    return fig


df = load_data(FILEPATH)
st.write("# COVID Forecast")

selected_series = st.selectbox("Select a data set:", (ALL, CASES, DEATHS, RECOVERIES))

if selected_series == ALL:
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

else:
    plotly_fig = make_forecast(selected_series)
    st.plotly_chart(plotly_fig)
