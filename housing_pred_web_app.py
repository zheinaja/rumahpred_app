# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:57:21 2023

@author: Program
"""

import numpy as np
import pickle
import streamlit as st
import catboost
from catboost import CatBoostRegressor, Pool, cv

# loading save model
model_jual = pickle.load(open('Prediksi Harga Jual Perumahan.sav','rb'))
model_sewa = pickle.load(open('Prediksi Sewa Perumahan.sav','rb'))


# creating a function for prediction

def housing_pred(test):
    
    hasil_jual = model_jual.predict(test)
    hasil_jual = hasil_jual/1000000    
    hasil_sewa = model_sewa.predict(test)
    hasil_sewa = hasil_sewa/1000000

    st.write(f'Rumah LB: {test[3]}, LT:{test[4]} dengan:')
    st.write(f'{test[0]} Kamar Tidur, {test[1]} Kamar Mandi, Garasi kapasitas {test[2]} mobil')
    st.write(f'di {test[5]}, {test[6]}')
    st.write(f'mempunyai harga jual sebesar Rp{hasil_jual:,.2f} Juta')
    st.write(f' dan harga sewa sebesar Rp{hasil_sewa:,.2f} Juta')


def main():
    # giving a title
    st.title('Zhein's Prediksi Harga Jual dan Sewa Rumah Jabodetabek')
    
    
    # getting the input data from the user
    
    luasb = st.text_input('Luas Bangunan')
    luast = st.text_input('luas Tanah')
    kamar_tidur = st.text_input('Jumlah Kamar Tidur')
    kamar_mandi = st.text_input('Jumlah Kamar Mandi')
    garasi = st.text_input('Garasi muat berapa mobil')
    lokasi = st.text_input('Kecamatan atau Lokasi')
    lokasi = str.title(lokasi)
    kota = st.selectbox(
    'Nama Kota',
    ('Bekasi','Depok','Bogor','Tangerang','Tangerang Selatan','Jakarta Selatan', 'Jakarta Barat', 'Jakarta Timur', 'Jakarta Utara', 'Jakarta Pusat'))

    
    # code for Prediction
    prediksi = ''
    
    # creating a button for Prediction
    
    if st.button('Prediksi Harga Rumah'):
        prediksi = housing_pred([kamar_tidur, kamar_mandi, garasi, luasb, luast,lokasi, kota ])
        
    
    
    
    
if __name__ == '__main__':
    main()
    
    
