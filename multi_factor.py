import tushare as ts

start = 2013
end = 2016
data_total ={}

def get_profit_data_quater():
    temp = start
    while(temp != end):
        data_total[str(temp) + "-1"] = ts.get_profit_data(temp, 1)
        temp += 1

get_profit_data_quater()
