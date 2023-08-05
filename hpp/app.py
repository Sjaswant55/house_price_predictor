import streamlit as st
import pandas as pd
import pickle
import math


data = pd.read_csv('Cleaned_data.csv')
house = pickle.load(open('RidgeModel.pkl','rb'))

st.title('House Price Predictor')

location = st.selectbox(
    'Select Location',
    sorted(data['location'].unique()))
bhk = st.selectbox(
    'Select Number of BHK',
    sorted(data['bhk'].unique()))
bath = st.selectbox(
    'Select Number of bathrooms',
    sorted(data['bath'].unique()))
sqft = st.text_input(
    'Select Expected Area in SQFT')

inputt = pd.DataFrame([[location,sqft,bath,bhk]],columns=['location','total_sqft','bath','bhk'])

if st.button('Predict House Value'):
    st.info(f"Predicted Valuation of the house is: *{math.ceil(house.predict(inputt)[0]*100000)}*")
    # st.error(num2words(math.ceil(house.predict(inputt)[0]*100000)).capitalize())