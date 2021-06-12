import streamlit as st
import yfinance as yf
import pandas as pd
from ta import trend as ta

st.set_page_config(page_title='Finance App', page_icon='📈',layout='wide')

hide_streamlit_style = """
            <style>
            #MainMenu {

                visibility: hidden;
               
               }
            footer {

                visibility: hidden;

                }
            footer:after {

	            content:'Made by Joey'; 
	            visibility: visible;
	            display: block;
	            position: relative;
	            #background-color: red;
	            padding: 5px;
	            top: 2px;

                }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

list_of_stocks = [

    'TSLA' ,'AAPL' ,'GOOGL' ,'AMC' ,'GME' ,'VOOG' ,'FB' ,'AMZN' ,'MSFT' ,'TLRY' ,
    'LULU' ,'F' ,'TM' ,'T' ,'TWTR' ,'KO' ,'SNAP' ,'NFLX' ,'LYFT' ,'PTON' ,'UBER' , 
    'LYFT' ,'NVDA' ,'PINS' ,'DDD'

    ]

watchlist = st.multiselect(label='Watchlist',options=list_of_stocks, default='TSLA')
start = st.text_input(label='Start Date', value='2020-01-01')


for stock in watchlist:
    col1, col2 = st.beta_columns(2)

    ticker = yf.Ticker(stock)
    df = ticker.history(period='max', start=start)

    col1.subheader(f'{stock} Close vs Time')
    col1.line_chart(data=df.Open)

    merged_df = pd.merge(df.Open,ta.sma_indicator(df.Close,window=30), on=df.index).set_index('key_0')
    merged_df2 = pd.merge(merged_df,ta.sma_indicator(df.Close,window=100), on=merged_df.index).set_index('key_0')

    col2.subheader(f'{stock} Simple Moving Average')
    col2.line_chart(merged_df2)