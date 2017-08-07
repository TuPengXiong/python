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

# 使用execute方法执行SQL语句
cursor.execute("SELECT * from wx_text limit 0,1")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()
#data = cursor.fetchmany()
print  data

cursor.close()

# 关闭数据库连接
db.close()
