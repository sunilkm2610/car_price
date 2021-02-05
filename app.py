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
    f =  {'Petrol':4 ,'Diesel':1 ,'CNG' :0,'LPG':3, 'Electric':2}
    t =  { 'Manual':1 ,'Automatic':0}
    o = {'First Owner':0 ,'Second Owner':2 ,'Fourth & Above Owner':1 ,'Third Owner':4,
 'Test Drive Car':3}
    

    l.append(f[fuel])
    l.append(t[transmission])
    l.append(o[owner])
    return l
    
        
def main():
    
    page_bg_img = '''
    <style>
    body {
            background-image: url("https://images.wallpaperscraft.com/image/rolls_royce_wraith_movement_side_view_111199_1920x1080.jpg");
            background-size: cover;
            
            }
    </style>
    
    '''
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    Km_driven = st.number_input('Km_driven',1000,step=1000)
    
    fuel = st.sidebar.selectbox('Fuel Type',('Petrol' ,'Diesel' ,'CNG','LPG', 'Electric'))
    
    print()
    transmission = st.sidebar.selectbox('Transmission',('Manual' ,'Automatic'))
    owner = st.sidebar.selectbox('Owner',('First Owner' ,'Second Owner' ,'Fourth & Above Owner' ,'Third Owner',
 'Test Drive Car'))
    oldyear = st.sidebar.slider('Old Year',0,30)
    k= [Km_driven]+ selection(fuel,transmission,owner)+[oldyear]
    x = "{:,}".format((round((price_predication(k[0],k[1],k[2],k[3],k[4]))[0])))
    
    if st.button('Calculate'):
        print(st.sidebar.header('Your Car Price is'+ ' '+ x))
    
    
    
    
if __name__=='__main__':
    main()
    