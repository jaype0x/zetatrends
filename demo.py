"""
This Lib is to create the renko chart and some stuff in future 
Created by JAY SPARK CEO-FOUNDER OF ZETA X ===> www.zeetaax.com
"""

import pandas as pd

from stocktrends import indicators


df = pd.read_csv('tests/HDFCLIFE')
df.columns = [i.lower() for i in df.columns]
rows = 5

pnf = indicators.PnF(df)
pnf.box_size = 10
pnf.reversal_size = 3


print('\n\nPnF bar data - based on close column')
data = pnf.get_bar_ohlc_data(source='close')
print(data.head(rows))


print('\n\nPnF box data - based on close column')
pnf_data = pnf.get_ohlc_data(source='close')
print(pnf_data.head(rows))


print('\n\nPnF box data - based on high/low columns')
data = pnf.get_bar_ohlc_data(source='hl')
print(data.head(rows))


renko = indicators.Renko(df)


print('\n\nRenko box calcuation based on periodic close')
renko.brick_size = 2
renko.chart_type = indicators.Renko.PERIOD_CLOSE
data = renko.get_ohlc_data()
print(data.tail(rows))



lb = indicators.LineBreak(df)

print('\n\nLine break chart')
lb.line_number = 3
data = lb.get_ohlc_data()
print(data.tail(rows))
