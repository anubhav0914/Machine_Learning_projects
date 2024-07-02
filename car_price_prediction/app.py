import streamlit as st
import pandas as pd
import pickle

df = pd.read_csv('cleaned_car.csv')
selected_carName = st.selectbox('Select car Name', df['name'].unique())
selcet_companyname = st.selectbox("select the company name",df['company'].unique())
selected_year = st.slider(
    'Select a year',
    min_value=1995,
    max_value=2023,
    step=1
)
selected_kms = st.number_input("Inter the km driven by the car")
selected_fuel_type = st.selectbox('Select car fuel type', df['fuel_type'].values)

pipe = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
result = pipe.predict(pd.DataFrame([[selected_carName,selcet_companyname,selected_year,selected_kms,selected_fuel_type]],columns =['name','company','year','kms_driven','fuel_type']))
st.header('Car-price-prediction')
if st.button('Predict'):
    st.write(result)