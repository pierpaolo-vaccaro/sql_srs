import streamlit as st
import pandas as pd
import duckdb as db
import io

csv = """
beverage, price
orange juice, 2.5
Expresso, 2
Tea, 3
"""
beverages = pd.read_csv(io.StringIO(csv))

csv2 = """
food_item, food_price
cookie, 2.5
chocolatine, 2
muffin, 3
"""
food_items = pd.read_csv(io.StringIO(csv2))

answer = """
SELECT *
FROM beverages
CROSS JOIN food_items
"""

solution = db.sql(answer)



st.write("""
# SQL SRS
Spaced Repetition System for SQL practice
""")

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "Group By", "Window Functions"),
        index=None,
        placeholder="Select a theme..."
    )
    st.write(f"You selected: {option}")

sql_query = st.text_area(label="Insert your SQL query here")
if sql_query:
    result = db.query(sql_query)
    st.dataframe(result)
st.write(f"You entered the following input: {sql_query}")

tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("Expected output")
    st.dataframe(solution)

with tab2:
    st.write(answer)