#!/usr/bin/python
# -*- coding: UTF-8 -*-
print "你好，世界";
if True:
    print "nonono"
else:
    print "hihao"

import time;
localtime = time.localtime(time.time())
print "本地时间为 :", localtime[0]

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("127.0.0.1","root","mysql","weixin" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()


cursor.execute("SELECT * from wx_text limit 0,1")


data = cursor.fetchone()
#data = cursor.fetchmany()
print  data

cursor.close()



import DbHelper
#dbHelper = DbHelper("192.168.18.253", "aidaijava888", "admin_123", "dc_user", 3306)
dbHelper = DbHelper("127.0.0.1", "root", "mysql", "weixin", 3306)
cursor = dbHelper.db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("select * from wx_text limit 0,1")
# 使用 fetchone() 方法获取一条数据库。
print cursor.fetchone()
# 关闭数据库连接
cursor.close()
dbHelper.disconnect()