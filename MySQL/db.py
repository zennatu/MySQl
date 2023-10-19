import pymysql
from dbutils.pooled_db import PooledDB


class DBHelper(object):
    def __init__(self):
        self.pool = PooledDB(
            # 连接数据库的模块
            creator = pymysql,
            # 连接池允许的最大连接数
            maxconnections = 50,
            # 初始化时，连接池中最少闲置的链接，0表示不创建
            mincached = 2,
            # 初始化时，连接池中最多闲置的链接，0和None不限制
            maxcached = 3,
            # 连接池中如果没有可用连接后，是否阻塞等待。
            blocking = True,
            # 会话开始前执行命令列表。如：["set datestyle to ...", "set time zone ..."]
            setsession = [],
            # ping MySQL服务端，查看服务是否可用。如：
            # 0 = None = never,
            # 1 = default = whenever it is requested,
            # 2 = when a cursor is created,
            # 4 = when a query is executed,
            # 7 = always
            ping = 0,
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = '123456',
            database = 'usersdb',
            charset = 'utf8'
        )
        
    def get_conn_cursor(self):
        conn = self.pool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return conn, cursor
        
    def close_conn_cursor(self, *args):
        for item in args:
            item.close()
        
    def exec(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()
        
        cursor.execute(sql, kwargs)
        conn.commit()
        
        self.close_conn_cursor(conn, cursor)
        
    def fetch_one(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()
        
        cursor.execute(sql, kwargs)
        result = cursor.fetchone()
        
        self.close_conn_cursor(conn, cursor)
        return result
        
    def fetch_all(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()
        
        cursor.execute(sql, kwargs)
        result = cursor.fetchall()
        
        self.close_conn_cursor(conn, cursor)
        return result

db = DBHelper()