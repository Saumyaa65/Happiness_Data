import streamlit as st
import plotly.express as px
import pandas as pd

st.header("In Search for Happiness")
x1=st.selectbox("Select the data for the X-axis",
             ("gdp","happiness","generosity"))
y1=st.selectbox("Select the data for the Y-axis",
             ("gdp","happiness","generosity"))
st.subheader(f"{x1} and {y1}")
df=pd.read_csv("happy.csv")
xaxis=df[x1]
yaxis=df[y1]

figure=px.scatter(x=xaxis,y=yaxis,labels={"x": x1, "y": y1})
st.plotly_chart(figure)
