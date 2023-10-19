from db import db

v1 = db.fetchone("select * from users")
print(v1)

v2 = db.fetchone("select * from users where id = %(nid)s",nid = 3)
print(v2)