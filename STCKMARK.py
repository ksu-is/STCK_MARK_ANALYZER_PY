#IMPORT EXTENTIONS TO USE WEBAPP, GRAPHS, STOCK MARKET DATA, AND DATES
import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01" #START DATE FOR WHEN DATA WILL BE 
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME','NFLX','META','QQQ','TSLA','AMC','AMZN','NVDA','NYSE','AMD','OTCMKTS:SIEGY')
selected_stock = st.selectbox('Select dataset for prediction', stocks)
