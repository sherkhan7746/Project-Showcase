import streamlit as st
from PIL import Image
import pandas as pd
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    img = Image.open("images/Photo.png")
    img = img.resize((700,500))
    st.image(img,width=500)


with col2:
    st.title("Sher Khan")
    content = """
    Hi, I’m a Python programmer with a focus on machine learning and deep learning. I graduated in 2023 and have since been working on various projects.
     I have experience with some of the top Python deep learning libraries such as TensorFlow, NumPy, Scikit-Learn, and Scipy.
     I believe that my skills and experience can help me contribute to the development of innovative solutions in the field of machine learning and deep learning.
    """
    st.info(content)

st.write("Below You can find some apps! I have built using Python. Feel free to contact me.")

col3, empty_col,  col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write("[Source Code](https://GOOGLE.COM)")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source Code](https://GOOGLE.COM)")