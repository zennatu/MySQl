import pymysql 

# 前置任务
# create database usersdb default charset utf8 collate utf8_general_ci;
# Query OK, 1 row affected (0.00 sec)

# mysql> use usersdb;
# Database changed
# mysql> create table users(
#     -> id int not null primary key auto_increment,
#     -> name varchar(32),
#     -> password varchar(64)
#     -> )default charset=utf8;

def register():
    print("用户注册")
    
    user = input("请输入用户名：")
    password = input("请输入密码：")
    
    # 连接指定数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', charset="utf8", db="usersdb")
    cursor = conn.cursor()
    
    # 执行SQL语句（有可能被SQL注入）
    sql = 'insert into users(name, password) values("{}","{}")'.format(user, password)
    
    cursor.execute(sql)
    conn.commit()
    
    # 关闭数据库连接
    cursor.close()
    conn.close()
    
    print("注册成功，用户名：{}, 密码：{}".format(user,password))
    
def login():
    print("用户登录")
    
    
    user = input("请输入用户名：")
    password = input("请输入密码：")
    
    # 连接指定数据
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', charset="utf8", db="usersdb")
    cursor = conn.cursor()
    
    # 执行SQL语句（有可能被SQL注入）
    sql = "select * from users where name='{}' and password='{}'".format(user, password)
    cursor.execute(sql)
    
    # 防止SQL注入可使用替代语句
    # cursor.execute("select * from users where name=%s and password=%s", [user,password])
    # 或
    # cursor.execute("select * from users where name=%(name)s and password=%(password)s", {"name":user,"password":password})
    
    result = cursor.fetchone()
    
    # 关闭数据库连接
    cursor.close()
    conn.close()
    
    if result:
        print("登陆成功！",result)
    else:
        print("登录失败",result)
        
def run():
    choice = input("1注册 2登录")
    if choice == '1':
        register()
    elif choice == '2':
        login()
    else:
        print("输入错误！")
        
if __name__ == '__main__':
    run()