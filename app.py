import io

import duckdb
import pandas as pd
import streamlit as st



# answer = """
# SELECT *
# FROM beverages
# CROSS JOIN food_items
# """
#
# solution = duckdb.sql(answer).df()


st.write(
    """
# SQL SRS
Spaced Repetition System for SQL practice
"""
)

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

with st.sidebar:
    option = st.selectbox(
        "What would you like to review?",
        ("Joins", "Group By", "Window Functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write(f"You selected: {option}")

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

sql_query = st.text_area(label="Insert your SQL query here")

#  if sql_query:
#     result = duckdb.query(sql_query).df()
#     st.dataframe(result)
#
#     try:
#         result = result[solution.columns]
#         st.dataframe(result.compare(solution))
#     except KeyError as e:
#         st.write("Some columns are missing")
#
# tab1, tab2 = st.tabs(["Tables", "Solution"])
#
# with tab1:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#    st.dataframe(food_items)
#     st.write("Expected output")
#     st.dataframe(solution)
#
# with tab2:
#     st.write(answer)
