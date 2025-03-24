import streamlit as st
import pandas as pd
import duckdb as db

data = {"a": [1,2,3], "b": [4,5,6]}
df = pd.DataFrame(data)

st.write("""
# SQL SRS
Spaced Repetition System for SQL practice
""")

option = st.selectbox(
    "What would you like to review?",
    ("Joins", "Group By", "Window Functions"),
    index=None,
    placeholder="Select a theme..."
)

st.write(f"You selected: {option}")

sql_query = st.text_area(label="Insert your SQL query here")
result = db.query(sql_query)
st.write(f"You entered the following input: {sql_query}")
st.dataframe(result)