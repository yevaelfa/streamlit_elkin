import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout="centered",
                   page_title="talento tech",
                   page_icon=":bar_chart:")

t1, t2 =st.columns([0.3,0.7])
t1.image("via.jpg")

t2.title("Análisis de datos con python")
t2.markdown('**tel:**3016211062 **| email:** yevaelfa@gmail.com**')

steps=st.tabs(["Pestaña 1", "Pestaña 2", "Pestaña $\sqrt{9}$"])

with steps[0]:
    st.write("Contenido de la pestaña 1")

with steps[1]:
    st.title("Pestaña 2")

with steps [2]:
    df=pd.DataFrame({
       "A": [1, 2, 3],
       "B": [4, 5, 6],
       "C": [7, 8, 9]})
    st.dataframe(df)

    fig, ax = plt.subplots()
    ax=sns.barplot(x=["A", "B", "C"], y=[1, 2, 3], ax=ax)
    st.pyplot(fig)
