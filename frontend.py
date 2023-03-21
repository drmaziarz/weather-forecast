import plotly.express as px
import streamlit as st

from backend import get_data

st.set_page_config(page_title="Weather Forecast",
                   page_icon="🌥",
                   layout="centered", )

st.title("Weather Forecast")
st.write("")

place = st.text_input(label="Place:")

days = st.slider(label="Forecast Days",
                 min_value=1,
                 max_value=5,
                 step=1,
                 help="Select the number of forecasted days")

option = st.selectbox(label="Select data to view",
                      options=("Temperature", "Sky"))

st.write("")

if place:
    try:
        filtered_data = get_data(place, days)

        st.subheader(f"{option} for the next {days} {'day' if days == 1 else 'days'} in {place}")

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=88)
    except KeyError:
        st.error("Please enter the correct name of the place.")
