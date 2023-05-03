import streamlit as st
import plotly.express as px
from prediction_backend import get_data

title = st.title('Weather Forecast for the Next Days')

place = st.text_input("Place:")
days = st.slider('Forecast Days: ', min_value=1, max_value=5,
                 help='Select the number of forecast days')

data_to_view = st.selectbox('Select data to view',
                            ('Temperature', 'Sky'))

st.subheader(f'{data_to_view} for the next {days} days in {place}')

data = get_data(place, days, data_to_view)

dates = ["4/30", "5/1", "5/2"]
temps = [30, 23, 21]
temps = [days * i for i in temps]
figure = px.line(x=dates, y=temps,
                 labels={"x": "Dates", "y":"Temperatures (C)"})
st.plotly_chart(figure)

