import streamlit as st
import json
from streamlit_lottie import st_lottie
st.set_page_config(
    page_title="DCSMA",
    page_icon="chart_with_upwards_trend"
)
st.sidebar.title("Navigation Menu")
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
helpgif = load_lottiefile("animations/helper.json")
st.title("What does DCSMA do?")
st.write('''
        This application allows us to understand the stock market of the 
        current dream companies everyone \n aspires to go to. We usually have an issue regarding how well are these 
        companies even faring everyday? \n This application helps us understand this by going through their current stock
        prices and understanding how they stand with their popular competitors.
        ''')
st_lottie(
    helpgif,
    speed = 1,
    reverse = False,
    quality = "high",
    height = "100%",
    width = "100%",
    key = None,
)
st.write("DCSMA (Dream Companies Stock Market Analysis) is here to help you out by running a regression machine learning model on them in order to understand how the general trend of the company is and what you could expect.")
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 