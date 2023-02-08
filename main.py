import pymysql

conn = pymysql.connect(host='127.0.0.1', user='root', password='toor', db='py_db', charset='utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM userTable")

print("ID     이름    이메일          출생연도")
print("---------------------------------------")

while(True):
    row = cur.fetchone()
    if row == None:
        break
    id = row[0]
    name = row[1]
    email = row[2]
    birth = row[3]
    print(f'{id:5s} {name:5s} {email:17s} {birth:d}')

conn.commit()
conn.close()
