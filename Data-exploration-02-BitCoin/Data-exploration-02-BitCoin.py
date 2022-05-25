#Get data for Bitcoin/USD for last 30 days
#Save data to csv file.
#Create candlestick graph.

#API: CoinGecko, https://www.coingecko.com/
#Wrapper: PyCoinGecko, https://github.com/man-c/pycoingecko

import pandas as pd
import plotly.graph_objects as go
import datetime
from pycoingecko import CoinGeckoAPI

#load data
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)
bitcoin_data = bitcoin_data['prices']  #only need prices

#processing
data = pd.DataFrame(bitcoin_data, columns=['TimeStamp','Price'])
data['Date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
#converted timestamp to datetime and created a column 'Date'

#candlestick
candlestick_data = data.groupby(data['Date'], as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})
#grouped and aggregated, data ready for the chart

fig = go.Figure(data=[go.Candlestick(x=candlestick_data['Date'],
                                    open=candlestick_data['Price']['first'],
                                    high=candlestick_data['Price']['max'],
                                    low=candlestick_data['Price']['min'],
                                    close=candlestick_data['Price']['last'])])

fig.update_layout(title_text="Bitcoin/USD for last 30 days", title_x=0.5, xaxis_rangeslider_visible=False)
fig.show()

#save file
candlestick_data.to_csv(r'C:\Users\krzys\Desktop\bit_test2.csv')
