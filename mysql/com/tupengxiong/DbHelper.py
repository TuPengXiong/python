import MySQLdb;


class DbHelper:
    'DbHelper'
    host = '127.0.0.1'
    user = 'root'
    password = ''
    dbName = ''
    port = 3306
    db = ''
    cursor = ''

    def __init__(self, host, user, password, dbName, port):
        self.host = host
        self.password = password
        self.user = user
        self.dbName = dbName
        self.port = port
        self.connect()

    def connect(self):
        if self.db == '':
            self.db = MySQLdb.connect(self.host, self.user, self.password, self.dbName)

    def disconnect(self):
        self.db.close()


dbHelper = DbHelper("192.168.18.253", "aidaijava888", "admin_123", "dc_user", 3306)
#dbHelper = DbHelper("127.0.0.1", "root", "mysql", "weixin", 3306)
#dbHelper.connect()
cursor = dbHelper.db.cursor()
cursor.execute("select * from dw_user limit 0,1")
print cursor.fetchone()
cursor.close()
dbHelper.disconnect()
