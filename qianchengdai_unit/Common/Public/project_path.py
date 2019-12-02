# -*- coding:utf-8 -*-
import  os
import time
path=os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]


# 日志路径
new=time.strftime('%Y-%m-%d')
time_path=new+'.txt'
log_path=os.path.join(path,'Result','log',time_path)


# 测试报告路径
report_path=os.path.join(path,'Result','report','test.html')


# 配置文件路径
config_path=os.path.join(path,'Common','Conf','conf.ini')
print(config_path)

# 图片路径
img_path=os.path.join(path,'Result','img','error.png')