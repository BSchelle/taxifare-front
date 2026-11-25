import datetime
import requests
import streamlit as st

st.set_page_config(page_title="TaxiFare Predictor", page_icon="🚕")

st.title("🚕 TaxiFare Predictor")
st.markdown("Predict New York City taxi fares in real-time.")

st.header("Ride Details")

col1, col2 = st.columns(2)

with col1:
    pickup_date = st.date_input("Pickup Date", datetime.date(2013, 7, 6))
    pickup_time = st.time_input("Pickup Time", datetime.time(17, 18))
    passenger_count = st.number_input("Passenger Count", min_value=1, max_value=8, value=1)

with col2:
    pickup_longitude = st.number_input("Pickup Longitude", value=-73.950655, format="%.6f")
    pickup_latitude = st.number_input("Pickup Latitude", value=40.783282, format="%.6f")
    dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.984365, format="%.6f")
    dropoff_latitude = st.number_input("Dropoff Latitude", value=40.769802, format="%.6f")

pickup_datetime = f"{pickup_date} {pickup_time}"
url = st.secrets['API_URL']

if st.button("Predict Fare"):
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count,
    }

    response = requests.get(url, params=params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        fare = data.get("fare")
        st.success(f"Estimated Fare: **${fare:.2f}**")
    else:
        st.error(f"Error calling API: status code {response.status_code}")
