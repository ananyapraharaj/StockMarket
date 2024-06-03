import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import cufflinks as cf

st.markdown(" # **Stock Price App**")  
st.markdown("This stock price app shows price data using *yfinance*")



st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date *(YYYY / MM / DD)*", datetime.date(2022, 1, 1))
end_date = st.sidebar.date_input("End date *(YYYY / MM / DD)*", datetime.date(2024, 1, 31))

df_for_dict = pd.read_csv('name_symbol.csv')[['Symbol','Name']]
symbols=df_for_dict['Symbol'].to_list()


stock = st.sidebar.selectbox('Select the stock.', options=symbols, index = 17)
tickerData = yf.Ticker(stock)
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)
#tickerData.info
#string_logo = '<img src=%s>' % tickerData.info['logo_url']
#st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

string_summary = tickerData.info['longBusinessSummary']
st.info(string_summary)
if (start_date<end_date):

    st.header('**Ticker data**')
    st.write(tickerDf)


    st.header('**Bollinger Bands**')
    qf=cf.QuantFig(tickerDf,title='First Quant Figure',name='GS')
    qf.add_bollinger_bands()
    fig = qf.iplot(asFigure=True)
    st.plotly_chart(fig)

else:
    st.warning('''**Invalid start and end dates**  
               *Please check incase the selected end date is before start date*''')