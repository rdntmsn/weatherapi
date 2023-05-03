import streamlit as st
import plotly.express as px
from prediction_backend import get_data

# front end
# set the title
title = st.title('Weather Forecast for the Next Days')

# text input for the place
place = st.text_input("Place:")

# slider to select the number of days
days = st.slider('Forecast Days: ', min_value=1, max_value=5,
                 help='Select the number of forecast days')
# menu to select either temperature or sky view
data_to_view = st.selectbox('Select data to view',
                            ('Temperature', 'Sky'))
# shows the user what will be viewed
st.subheader(f'{data_to_view} for the next {days} days in {place.title()}')

# get data from front end
if place:
    try:
        filtered_data = get_data(place, days)

        # the temperature in chart
        if data_to_view == 'Temperature':
            temps = [round(dict["main"]['temp'] / 10, 2) for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temps,
                             labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        # the sky charted
        if data_to_view == 'Sky':
            images = {"Clear": 'sky/clear.png', 'Clouds': 'sky/cloud.png',
                      'Rain': 'sky/rain.png', 'Snow': 'sky/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=75)

    except KeyError:
        st.info('You have entered a city that does not exist. Please enter the correct city name')
