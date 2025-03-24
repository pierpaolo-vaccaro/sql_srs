import streamlit as st
import pandas as pd
import duckdb as db

data = {"a": [1,2,3], "b": [4,5,6]}
df = pd.DataFrame(data)

sql_query = st.text_area(label="Insert your SQL query here")
result = db.query(sql_query)
st.write(f"You entered the following input: {sql_query}")
st.dataframe(result)