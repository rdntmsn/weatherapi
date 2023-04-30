import streamlit as st

title = st.title('Weather Forecast for the Next Days')

place = st.text_input("Place:")
days = st.slider('Forecast Days: ', min_value=1, max_value=5,
                 help='Select the number of forecast days')

data_to_view = st.selectbox('Select data to view',
                            ('Temperature', 'Sky'))

st.subheader(f'{data_to_view} for the next {days} days in {place}')


