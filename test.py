#
# initial_quotas = 1
#
# increase = 1.05
#
# _c = 0
#
# for i in range(15):
#     buy = int(initial_quotas * increase**i)
#     _c += buy
#     print(buy)
#
# print(initial_quotas * (0.97 **15), _c)


# import math
#
# r = math.log(4, 2)
# print(r)
#
# # print(0.975 ** 17)
# import tushare as ts
#
#
# TOKEN = '8fd4826df4da30db172ac6fe205c0d44aac29805de23ddc626edd835'
# # pro = ts.pro_api(TOKEN)
# ts.set_token(TOKEN)
#
# # # df = pro.daily(ts_code='600104.SH', start_date='20200101', end_date='20200528')
# #
# # df = ts.get_hist_data('600848')
# # # df = ts.get_realtime_quotes('600104')  # 实时分笔
#
#
#
# date = ts.pro_bar('600104.SH', start_date='20180201', adj='qfq')
# # date = ts.get_k_data('600104.SH', start='20180201')
# # df = pro.daily(ts_code='600104.SH', start_date='20180201', end_date='20200527')#
# # df = pro.ts.pro_bar(ts_code='600104.SH', adj='qfq', start_date='20180201', end_date='20200527')
# print(date)


import baostock as bs
import pandas as pd

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取沪深A股历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。
# 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
rs = bs.query_history_k_data_plus("sh.600104",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
    start_date='2016-07-12', end_date='2019-12-31',
    frequency="d", adjustflag="2")
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

#### 结果集输出到csv文件 ####
result.to_csv("D:\\history_A_stock_k_data.csv", index=False)
print(result)

#### 登出系统 ####
bs.logout()