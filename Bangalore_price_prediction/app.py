import streamlit as st
import pandas as pd
import pickle


st.header('Banglore-House-price-prediction')

df = pd.read_csv('clead_data.csv')
selected_location = st.selectbox('Select  location', df['location'].unique())
total_area = st.number_input("Enter the area of the House", placeholder="Type a number...")

no_bhk = st.number_input("Enter the BHK  number", placeholder="Type a number...", step=1,format="%d")
bathroom = st.number_input('Enter the number of  bathrooms', placeholder="Type a number..." ,step=1 ,format="%d")

pipe = pickle.load(open('model.pkl', 'rb'))
result = pipe.predict(pd.DataFrame([[selected_location,total_area,bathroom,no_bhk]],columns =['location','total_sqft','bath','bhk']))
if st.button('Predict'):
    st.header(f"Rs. {result} lakhs")