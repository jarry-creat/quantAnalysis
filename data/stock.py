from jqdatasdk import *
auth('18161870857','ZTYhyh123123') 
import datetime
import pandas as pd
# 设置行列不忽略
pd.set_option('display.max_rows',10000)
pd.set_option('display.max_columns',1000)

# 获取所有A股股票列表
def get_stock_list():
    stocks = list(get_all_securities(['stock']).index)
    return stocks

# 获取单个股票行情数据
def get_single_stock_price(code,time_freq,start_date,end_date):
    data = get_price(code,start_date=start_date,end_date=end_date,frequency=time_freq,panel=False)
    return data

# 导出股票数据 type表示 股票数据类型，可以是price，可以是finance
def export_data(data,filename,type): 
    file_root = 'C:/Users/吕强/Desktop/quantAnalysis/data/' + type + '/' + filename + '.csv'
    data.index.names = ['date']
    data.to_csv(file_root)
    print('已成功存储至: ',file_root)

#将数据转换为指定周期：开盘价，收盘价，最高价，最低价
def transfer_price_freq(data,time_freq):
    df_trans = pd.DataFrame()
    df_trans['open'] = data['open'].resample(time_freq).first()
    df_trans['close'] = data['close'].resample(time_freq).last()
    df_trans['high'] = data['high'].resample(time_freq).max()
    df_trans['low'] = data['low'].resample(time_freq).min()
    return df_trans

# 获取单个股票财务指标
def get_single_finance(code,date,statDate):
    data = get_fundamentals(query(indicator).filter(indicator.code == code),date=date, statDate=statDate)
    return data

# 获取单个股票估值指标
def get_single__valuation(code,date,statDate):
    data = get_fundamentals(query(valuation).filter(valuation.code == code), date=date,statDate=statDate)
    return data