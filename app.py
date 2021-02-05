#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:05:14 2021

@author: sunilkumar
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.title("WELCOME TO CAR PRICE PREDICATION")
pickle_in = open('car_price_predication.pkl','rb')
rf_random = pickle.load(pickle_in)




def price_predication(km_driven,fuel,transmission,owner,old_year):
    predication = rf_random.predict([[km_driven,fuel,transmission,owner,old_year]])
    return predication
def selection(fuel,transmission,owner) :
    l = []
    f = {'Petrol':4 ,'Diesel':1 ,'CNG' :0,'LPG':3, 'Electric':2}
    t = { 'Manual':1 ,'Automatic':0}
    o = {'First Owner':0 ,'Second Owner':2 ,'Fourth & Above Owner':1 ,'Third Owner':4,'Test Drive Car':3}
    

    l.append(f[fuel])
    l.append(t[transmission])
    l.append(o[owner])
    return l
    
        
def main():
    
    
    page_bg_img = '''
    <style>
    body {  
            
            background-image: url('https://images.unsplash.com/photo-1519641471654-76ce0107ad1b?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1651&q=80');
            background-size: cover;
            
            }
    </style>
    
    '''
    #st.selectbox('Car Company',('HYUNDAI','HONDA','SUZUKI'))
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
    Km_driven = st.number_input('Km_driven',1000,step=1000)
    
    fuel = st.sidebar.selectbox('Fuel Type',('Petrol' ,'Diesel' ,'CNG','LPG', 'Electric'))
    
    print()
    transmission = st.sidebar.selectbox('Transmission',('Manual' ,'Automatic'))
    owner = st.sidebar.selectbox('Owner',('First Owner' ,'Second Owner' ,'Fourth & Above Owner' ,'Third Owner',
    'Test Drive Car'))
    oldyear = st.sidebar.slider('Old Year',0,30)
    st.sidebar.write(oldyear)
    k= [Km_driven]+ selection(fuel,transmission,owner)+[oldyear]
    x = "{:,}".format((round((price_predication(k[0],k[1],k[2],k[3],k[4]))[0])))
    
    if st.sidebar.button('Calculate'):
        
        st.sidebar.header('Car Price in 2021'+ ' ::: '+'₹' +str(x))
    
    if st.button('About us'):
        
        st.sidebar.write('This project based on previous car dataset and predict prices with help of Random Forest Regressor')
    
    
    
if __name__=='__main__':
    main()
    