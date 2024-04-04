# pylint: disable=missing-module-docstring

import os
import sys
import logging
import streamlit as st
import duckdb

if "data" not in os.listdir():
    logging.error(os.listdir())
    logging.error("creating folder data")
    os.mkdir("data")

if "exercises_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())
    # subprocess.run([sys.executable, "init_db.py"])
    # subprocess.run(["python", "init_db.py"])

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

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

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df().sort_values("last_reviewed").reset_index(drop=True)
    st.write(exercise)

    exercise_name = exercise.loc[0, "exercise_name"]
    with open(f"answers/{exercise_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header("enter your code:")
query = st.text_area(label="votre code SQL ici", key="user_input")
if query:
    result = con.execute(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("Some columns are missing")


tab2, tab3 = st.tabs(["Tables", "Solution"])

with tab2:
    print(exercise.loc[0, "tables"])
    print(type(exercise.loc[0, "tables"]))
    exercise_tables = exercise.loc[0, "tables"]
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM '{table}'").df()
        st.dataframe(df_table)


with tab3:
    st.text(answer)
print()
