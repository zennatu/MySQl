import threading
import pymysql
from dbutils.pooled_db import PooledDB

MYSQL_DB_POOL = PooledDB(
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

def task():
    # 去连接池获取一个连接
    conn = MYSQL_DB_POOL.connection()
    cursor = conn.cursor(pymysql.cursor.DictCursor)
    
    cursor.execute('select sleep(2)')
    result = cursor.fetchall()
    print(result)
    
    cursor.close()
    conn.close()
    
def run():
    for i in range(10):
        t = threading.Thread(target=task)
        t.start()
        
if __name__ == '__main__':
    run()