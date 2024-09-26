import streamlit as st
import pandas as pd

st.title("RAG Project Test")
st.write("This is a test for the RAG application setup.")

# Example dataframe
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [24, 27, 22]}
df = pd.DataFrame(data)
st.write("Example DataFrame:", df)