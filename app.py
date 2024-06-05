import streamlit as st
import pandas as pd

st.title("Earthquake Data Explorer")
st.text("This is a web app to explore earthquake data.")

st.sidebar.title("Navigation")
file = st.sidebar.file_uploader("Upload the file")

options = st.sidebar.radio("Pages", options=["Home","Data statistics", "Data Preview","Plot"])

def stats(df):
    st.header("Data Statistics")
    st.write(df.describe())

def preview(df):
    st.header("Data Preview")
    st.write(df.head())

def plot(df):
    st.header("Data Visualization")
    st.line_chart(df["Magnitude"])
    st.scatter_chart(df, x="Depth", y="Magnitude")

if file:
    df = pd.read_csv(file)
    if options == "Data statistics":
        stats(df)
    elif options == "Data Preview":
        st.write(df.head())
    elif options == "Plot":
        plot(df)
else: 
    st.write("## Please upload a file")
    



    