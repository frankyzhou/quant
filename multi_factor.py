import tushare as ts
import pandas as pd
from pandas import Series, DataFrame

start = 2013
end = 2014
data_total_raw ={}
data_total_sorted ={}

def get_profit_data_quater():
    temp_year = start
    while(temp_year != end):
        for temp_quater in [1,2,3,4]:
            data_total_raw[str(temp_year) + "-" + str(temp_quater)] = \
                ts.get_profit_data(temp_year, temp_quater)
        temp_year += 1

def get_sorted_data():
    for item in data_total_raw.keys():
        data_total_sorted[item] = DataFrame.sort_values(data_total_raw[item], axis=1,ascending=False,columns="eps")

get_profit_data_quater()
get_sorted_data()

print data_total_raw