import streamlit as st
import pickle
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
import string

ps = PorterStemmer()

def trasform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text) # now it is a list
    y = []
    for i in text :
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text :
        y.append(ps.stem(i))
    return " ".join(y)

tfid = pickle.load(open('tfid.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('Email/SMS classifier')

input_sms = st.text_area("Enter the messsage ")
if st.button('Predict'):
    trasform_sms = trasform_text(input_sms)
    vector_input = tfid.transform([trasform_sms])
    result = model.predict(vector_input)[0]

    if result == 1:
        st.write('Spam')
    else :
        st.write('Not Spam')