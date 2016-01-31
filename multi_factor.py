# coding=utf-8
from sqlalchemy import create_engine
import tushare as ts
import pandas as pd
from pandas import Series, DataFrame
from pandas.io import sql

start = 2013
end = 2016
data_total_raw ={}
data_total_sorted ={}
engine = create_engine('mysql://root:zlj@127.0.0.1/profit_data?charset=utf8', encoding='utf-8')

def get_profit_data_quater():
    temp_year = start
    while(temp_year != end):
        for temp_quater in [1,2,3,4]:
            item = str(temp_year) + "-" + str(temp_quater)
            if not sql.has_table(item, engine, flavor="mysql"):
                print item + "begins"
                data_total_raw[item] = ts.get_profit_data(temp_year, temp_quater)
                print "\n"
                if any(data_total_raw[item]):   data_total_raw[item].to_sql(item, engine)
        temp_year += 1

def get_sorted_data():
    temp_year = start
    while(temp_year != end):
        for temp_quater in [1,2,3,4]:
            item = str(temp_year) + "-" + str(temp_quater)
            data_total_raw[item] = sql.read_sql(item, engine)
            print item + " has load."
        temp_year += 1
    for item in data_total_raw.keys():
        data_total_sorted[item] = DataFrame.sort_values(data_total_raw[item], axis=0, ascending=False, by="eps")

# get_profit_data_quater()
get_sorted_data()

print data_total_sorted