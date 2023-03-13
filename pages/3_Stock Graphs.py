import streamlit as st
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
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
st.sidebar.title("Navigation Menu")
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
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
def deploygraph(company : str):
    if tget(company) == ' ':
        return
    else:
        st.markdown("The price vs day for " + company + " in the past 5 years is:")
        df = yf.download(tickers = tget(company), period = '5y', interval = '1d',ignore_tz = True, prepost = False)
        df.reset_index(inplace = True)
        df['Years'] = df['Date'].map(dt.datetime.toordinal)
        df['Years'] = (df['Years'] - min(df['Years']))/365
        df['Price'] = df['Close']
        df.drop(['Open','Close', 'Adj Close', 'Volume'],axis=1,inplace = True)
        st.line_chart(df,x='Years',y='Price')
        st.dataframe(df,use_container_width=True)
        st.write("You can view the details more extensively using the dataframe shown above")
        return
st.title("Looking at the chart")
st.write("To get started choose any of the following organizations given")
stock_options = ['Select a company','Amazon','Apple','Google','Meta','Microsoft','Tesla']
stock_selected = st.selectbox(label = " ", options = stock_options)
deploygraph(stock_selected)
