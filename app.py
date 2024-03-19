import streamlit as st
import pandas as pd
import duckdb

st.write("Hello world !")
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["SQL", "other", "other2"])

with tab1:
    q = st.text_area(label="entrez votre requête")
    st.write(f"Résultats pour la requête : {q}")
    result = duckdb.query(q).df()

    st.dataframe(result)
    # st.write(df)

with tab2:
    st.header("1st other")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("2nd other")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
