#IMPORT EXTENTIONS TO USE WEBAPP, GRAPHS, STOCK MARKET DATA, AND DATES
import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

START = "2015-01-01" #DATE FOR WHEN DATA WILL BE START TO BE ANALYZED 
TODAY = date.today().strftime("%Y-%m-%d")#TAKES CURRENT DATE AND USES IT AS THE END OF ANALYZATION PERIOD

st.title('Stock Forecast App')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME','NFLX','META','QQQ','TSLA','AMC','AMZN','NVDA','NYSE','AMD','OTCMKTS:SIEGY')
selected_stock = st.selectbox('Select dataset for prediction', stocks)

#collect historical stock data
stock_data = yf.download(selected_stock, START, TODAY)
