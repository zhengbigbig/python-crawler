import pymysql

# 1. 使用pymysql.connet方法链接数据库
db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root", database="csdn_crawler")
# 2. 如果想要操作数据库，还需要获取db上面的cursor对象
cursor = db.cursor()
# 3. 使用cursor.execute来执行sql语句
cursor.execute("select * from article")
result = cursor.fetchone()
print(result)

# 增
title = '444'
content = '555'
sql = "insert into article(id,title,content) values(null,%s,%s)"
cursor.execute(sql, (title, content))

db.commit()
db.close()

# 删
# delete from [表名] 条件
sql = "delete from article where id>3"
cursor.execute(sql)
db.commit()
db.close()

# 改
# update [表名] 更新操作 条件
sql = "update article set title='钢铁是怎样练成的' where id=3"
cursor.execute(sql)

db.commit()
db.close()

# 查

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="root", database="csdn_crawler")
cursor = db.cursor()

sql = "select id,title from article where id>3"
cursor.execute(sql)
# result = cursor.fetchone()
# result = cursor.fetchall()
result = cursor.fetchmany(7)
print(result)

db.close()
