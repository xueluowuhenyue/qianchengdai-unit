# -*- coding:utf-8 -*-
error_data=[{'Caseid':1,'module':'投标','title':'投资金额为零','bid_name':'先借一个亿','amount':'0','expect':'请正确填写投标金额'},
            {'Caseid':2,'module':'投标','title':'投资金额为负','bid_name':'先借一个亿','amount':'-100','expect':'请正确填写投标金额'},
            {'Caseid':3,'module':'投标','title':'投资金额不是整百整数','bid_name':'先借一个亿','amount':'10','expect':'投标金额必须为100的倍数'},
            {'Caseid':4,'module':'投标','title':'投资金额大于余额','bid_name':'先借一个亿','amount':'10000000000','expect':'投标金额大于可用金额'}]

error_whole_ten=[{'Caseid':6,'module':'投标','title':'投资金额不是整十数','bid_name':'先借一个亿','amount':'99','expect':'请输入10的整数倍'}]

seccess_data=[{'Caseid':7,'module':'投标','title':'正常投资','bid_name':'先借一个亿','amount':'100','expect':'投标成功！'}]

login_data={'user_name':'18684720553','password':'python'}