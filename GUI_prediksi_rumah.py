import streamlit as st
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from PIL import Image
import pandas as pd
import time
import matplotlib.pyplot as plt

#load model yang sudah di train
pickle_in = open("model_prediksi_rumah.pkl", "rb")
random_forest_regression_model = pickle.load(pickle_in)

def Home():
    return ('Sabar gan')

def predicting(bedrooms, bathrooms, sqft_living,  floors, grade, yr_built):
    prediction = random_forest_regression_model.predict([[bedrooms, bathrooms, sqft_living,  floors, grade, yr_built]])
    output = round(prediction[0], 2)
    return output
#'bedrooms', 'bathrooms',	'sqft_living', 'floors', 'grade',	'yr_built'
def main():
    html_temp = """
    <div style="background-color:navy;padding:10px">
    <h1 style="color:white;text-align:center;">Prediksi Harga Rumah ($) </h1>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    
    st.subheader("Jumlah Kamar") #bedrooms
    bedrooms = st.slider("", min_value=0, max_value=11, value=0, step=1)

    st.subheader("Jumlah Kamar Mandi") #bathrooms
    bathrooms = st.slider("", min_value=0, max_value=8, value=0, step=1)

    st.subheader("Luas") #sqft_living
    sqft_living = st.text_input("dalam square feet (sqft)", "")


    st.subheader("Jumlah Lantai") #floors
    floors = st.slider("", min_value=1, max_value=3, value=1, step=1)

    st.subheader("Kelas / Grade") #grade
    grade = st.slider("", min_value=1, max_value=13, value=1, step=1)


    st.subheader("Tahun Dibangun") #yr_built
    yr_built = st.text_input("", "")
    

    result = ""
    if st.button("Perkiraan harga"):

        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        result = predicting(bedrooms, bathrooms, sqft_living, floors,  grade, yr_built)

    st.success('Hasil Prediksi : {} Dollars'.format(result))


nav = st.sidebar.radio("Halaman", ["Home", "Data Sample", "About Me"])
if nav == "Home":
    if __name__ == "__main__":
        main()

if nav == "Data Sample":
    st.title("Data Sample")
    data = pd.read_csv("dataFrame_test_train.csv", usecols=['price', 'bedrooms', 'bathrooms', 'sqft_living',	'grade', 'floors',	'yr_built'])
    st.table(data.sample(100))
    plt.show()


if nav == "About Me":
    st.title(" Prediksi Harga Rumah")
    st.subheader("Gilang Agung Saputra (672019229)")
    