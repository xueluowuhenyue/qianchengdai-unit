# -*- coding:utf-8 -*-
import logging
import time
from Common.Public import project_path
from Common.Public.read_ini import configuration

class Mylog:
    '''这是一个日志类'''
    # new=time.strftime('%Y-%m-%d')
    # path=new+'.txt'                        #日志名字取当前日期
    def __init__(self):
        self.logger_level=configuration(project_path.config_path).read_str('LOG','logger_level')
        self.file_level=configuration(project_path.config_path).read_str('LOG','file_level')
        self.file_name=configuration(project_path.config_path).read_str('LOG','file_name')
        self.formatter=configuration(project_path.config_path).read_str('LOG','formatter')
    def mylog(self,level,msg):
        #定义一个日志收集器
        my_logger=logging.getLogger(self.file_name)
        #设置日志的级别
        my_logger.setLevel(self.logger_level)
        #设置输出输出格式
        formatter = logging.Formatter(self.formatter)
        #设置输出渠道
        fh=logging.FileHandler(project_path.log_path,encoding='utf-8')
        #设置输出日志级别
        fh.setLevel(self.file_level)
        #设置格式
        fh.setFormatter(formatter)
        #输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(self.file_level)#设置级别
        ch.setFormatter(formatter)#设置格式

        #对接
        my_logger.addHandler(fh)
        my_logger.addHandler(ch)

        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)
    def debug(self,msg):
        self. mylog('DEBUG',msg)
    def info(self,msg):
        self. mylog('INFO',msg)
    def warning(self,msg):
        self. mylog('WARNING',msg)
    def error(self,msg):
        self. mylog('ERROR',msg)
    def critical(self,msg):
        self. mylog('CRITICAL',msg)

if __name__ == '__main__':
    p=Mylog()
    p.error('睡觉啦！！！')