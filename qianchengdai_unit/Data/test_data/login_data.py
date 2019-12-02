# -*- coding:utf-8 -*-

success_data=[{'Caseid':6,'module':'登录','title':'正常登录','username':'18684720553','password':'python','expect':'我的帐户[wolf]'}]


alter_error=[{'Caseid':4,'module':'登录','title':'错误密码登录','username':'18684720553','password':'12','expect':'帐号或密码错误!'},
             {'Caseid':5,'module':'登录','title':'未注册账号登录','username':'13541781424','password':'123456','expect':'此账号没有经过授权，请联系管理员!'}]

error_info=[{'Caseid':1,'module':'登录','title':'不输入用户名','username':'','password':'123654','expect':'请输入手机号'},
            {'Caseid':2,'module':'登录','title':'不输入密码','username':'18684720553','password':'','expect':'请输入密码'},
            {'Caseid':3,'module':'登录','title':'输入不符规则的用户名','username':'123654','password':'222','expect':'请输入正确的手机号'}]