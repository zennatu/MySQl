from db_context import Connect

with Connect() as obj:
    ret = obj.fetch_one("select * from users")
    print(ret)
    
    ret = obj.fetch_one("select * from users where id = %(id)s", id = 3)
    print(ret)
    
    
    
with Connect() as obj:
    ret = obj.fetch_one("select * from users")
    print(ret)
    
    ret = obj.fetch_one("select * from users where id = %(id)s", id = 4)
    print(ret)