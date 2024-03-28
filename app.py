# pylint: disable=missing-module-docstring

import streamlit as st
import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

# solution = duckdb.sql(ANSWER_STR).df()


st.write(
    """
# SQL SRS
Spaced Repetition System SQL practice
"""
)
with st.sidebar:
    theme = st.selectbox(
        "How would you like to review ?",
        ("cross_joins", "Group By", "Windows Functions"),
        index=None,
        placeholder="Select topic...",
    )
    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()

    st.write(exercise)


st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")
# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("expected:")
#     st.dataframe(solution)
#
# with tab3:
#     st.write(ANSWER_STR)
print()
