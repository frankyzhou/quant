import tushare as ts

start = 2013
end = 2016
data_total ={}

def get_profit_data_quater():
    temp_year = start
    while(temp_year != end):
        for temp_quater in [1,2,3,4]:
            data_total[str(temp_year) + "-" + str(temp_quater)] = ts.get_profit_data(temp_year, temp_quater)
        temp_year += 1

get_profit_data_quater()

print data_total