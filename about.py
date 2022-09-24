import pandas as pd
import streamlit as st

st.title('about')

st.info('this is a test')

st.success('this is  a test')

name = st.text_input('entre your name')

age = st.number_input('entre your age')


height = st.slider('entre your hight',min_value=0,max_value=200,value=100,step=10)

dic= {'name':name,'age':age,'height':height}

df = pd.DataFrame(dic,index=[0])

st.write(df)


