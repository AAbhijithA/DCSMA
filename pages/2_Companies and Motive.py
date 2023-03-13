import streamlit as st
import json
from streamlit_lottie import st_lottie
st.set_page_config(
    page_title="DCSMA",
    page_icon="chart_with_upwards_trend"
)
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
st.sidebar.title("Navigation Menu")
apple = load_lottiefile('animations/apple.json')
amazon = load_lottiefile('animations/amazon.json')
meta = load_lottiefile('animations/meta.json')
google = load_lottiefile('animations/google.json')
mcsoft = load_lottiefile('animations/microsoft.json')
tesla = load_lottiefile('animations/tesla.json')
st.title("Companies")
st.subheader('''
        Since the application is still in its budding stage we have included the top 'six' software companies for the application:\n\n
        ''')
c1, c2, c3 = st.columns(3)
with c1:
    st_lottie(apple)
    st_lottie(tesla)
with c2:
    st_lottie(amazon)
    st_lottie(google)
with c3:
    st_lottie(meta)
    st_lottie(mcsoft)
st.subheader('''We use regression techniques in order to tell about the performance of the company and this enables us to decide upon how is the company faring with respect to others.
        ''')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 