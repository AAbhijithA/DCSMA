import streamlit as st
import pandas as pd
import numpy as np
import json
from PIL import Image
import yfinance as yf
import datetime as dt
import time
from streamlit_lottie import st_lottie
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
st.set_page_config(
    page_title="DCSMA",
    page_icon="chart_with_upwards_trend"
)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
def tget(company : str):
    if company == 'Apple':
        return 'AAPL'
    elif company == 'Google':
        return 'GOOG'
    elif company == 'Tesla':
        return 'TSLA'
    elif company == 'Meta':
        return 'META'
    elif company == 'Microsoft':
        return 'MSFT'
    elif company == 'Amazon':
        return 'AMZN'
    else:
        return " "
def make_model(x,y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
    LGR = LinearRegression()
    LGR.fit(x_train, y_train)
    sVal = LGR.score(x_test, y_test)
    return LGR, sVal
def LRgraph(company : str):
    if tget(company) == " ":
        return
    else:
        df = yf.download(tickers = tget(company), period = '5y', interval = '1d',ignore_tz = True, prepost = False)
        df.reset_index(inplace = True)
        df['Years'] = df['Date'].map(dt.datetime.toordinal)
        df['Years'] = (df['Years'] - min(df['Years']))/365
        df['Price'] = df['Close']
        df.drop(['Open','Close', 'Adj Close', 'Volume'],axis=1,inplace = True)
        x = np.array(df['Years']).reshape(-1, 1)
        y = np.array(df['Price']).reshape(-1, 1)
        progress_text = "Building Model"
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.015)
            my_bar.progress(percent_complete + 1, text=progress_text)
        c1, c2 = st.columns(2)
        LGR1, scr1 = make_model(x,y)
        y_pred = LGR1.predict(x)
        fig, ax = plt.subplots()
        ax.plot(x,y,color='cyan')
        ax.plot(x,y_pred,color='blue')
        ax.set_xlabel('Years')
        ax.set_ylabel('Price')
        ax.set_title('Graph from the model for 5 Year Performance')
        c1.pyplot(fig)
        c1.write("The score of the model is: "+str(scr1))
        df = yf.download(tickers = tget(company), period = '6mo', interval = '1d',ignore_tz = True, prepost = False)
        df.reset_index(inplace = True)
        df['Days'] = df['Date'].map(dt.datetime.toordinal)
        df['Days'] = df['Days'] - min(df['Days'])
        df['Price'] = df['Close']
        df.drop(['Open','Close', 'Adj Close', 'Volume'],axis=1,inplace = True)
        x = np.array(df['Days']).reshape(-1, 1)
        y = np.array(df['Price']).reshape(-1, 1)
        LGR2, scr2 = make_model(x,y)
        y_pred = LGR2.predict(x)
        fig, ax = plt.subplots()
        ax.plot(x,y,color='lime')
        ax.plot(x,y_pred,color='green')
        ax.set_xlabel('Days')
        ax.set_ylabel('Price')
        ax.set_title('Graph from the model for 6 month Performance')
        c2.pyplot(fig)
        c2.write("The score of the model is: "+str(scr2))
        v1 = LGR1.coef_[0,0]
        v2 = LGR2.coef_[0,0]
        with st.expander("Check to see the verdict (with respect to coeficients from the model)"):
            think = load_lottiefile("animations/thinking.json")
            st_lottie(think,speed = 1,reverse = False,quality = "high",height = "10%",width = "70%",key = None)
            if ((v1*v2) >= 0.8):
                st.write("The organization is doing great enough and is safe to invest in.\nYou could try to catch up on the long term investment route here.")
            elif ((v1*v2) >= 0.4):
                st.write("There might be a few downfalls but it might be risky to invest in it currently\nmainly due to the fact it can go either way if you are a short term invester.")
            else:
                st.write("The organization is going through some tough times, you can invest now if you can hold it until it goes up. The best to do is to find a point where it falls and rises and you could invest then.")
st.sidebar.title("Navigation Menu")
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.title("Using the Linear Regressor Model")
st.write("Select the companies you would like to see the analysis of with the help of our model")
stock_options = ['Select a company','Amazon','Apple','Google','Meta','Microsoft','Tesla']
stock_selected = st.selectbox(label = " ", options = stock_options)
LRgraph(stock_selected)