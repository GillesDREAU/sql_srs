# pylint: disable=missing-module-docstring

import streamlit as st
import duckdb
# import ast

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
        ("cross_joins", "Group By", "window_functions"),
        index=None,
        placeholder="Select topic...",
    )
    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()

    st.write(exercise)


st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)

tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM '{table}'").df()
        st.dataframe(df_table)


with tab3:
    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()
    st.text(answer)
print()
