import pymysql
from faker import Faker
import random

# Faker 객체 초기화
fake = Faker()

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='127.0.0.1',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='ans!!941105',  # 데이터베이스 비밀번호
    db='airbnb',       # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

with conn.cursor() as cursor:
    # 문제 1
    # sql = f'INSERT INTO Products(productName, price, stockQuantity) VALUES (%s, %s, %s)'
    # cursor.execute(sql, ('Python Book', 10000, 10))
    # conn.commit()
    # cursor.execute('')

    # # 문제 2
    # cursor.execute('SELECT * FROM Products')
    # for book in cursor.fetchall():
    #     print()

    # 문제 3
    # sql = "UPDATE Products SET stockQuantity = stockQuantity - %s WHERE productID = %s"
    # cursor.execute(sql, (1, 2))
    # conn.commit()

    # 문제 4
    # sql = "SELECT customerID, SUM(totalAmount) FROM Orders GROUP BY customerID"
    # cursor.execute(sql)
    # datas = cursor.fetchall()
    # print(datas)

    # 문제 5
    # customer_ID = str(input('수정할 고객님의 이메일을 입력해주세요 : '))
    # sql = "UPDATE Customers SET email=%s WHERE customerID = %s"
    # cursor.execute(sql, (customer_ID, 1))
    # conn.commit()

    # 문제 6
    # sql = "DELETE FROM Orders WHERE orderID = %s"
    # cursor.execute(sql, 14)
    # conn.commit()

    # 문제 7
    # sql = "SELECT * FROM Products WHERE productName LIKE %s"
    # cursor.execute(sql, ('%Beat%'))
    # datas = cursor.fetchall()

    # for data in datas:
    #     print(data['productName'])

    # 문제 8
    # sql = "SELECT * FROM Orders WHERE customerID = %s"
    # cursor.execute(sql, (1))
    # costomer_data = cursor.fetchall()
    
    # for data in costomer_data:
    #     print(data)

    # 문제 9
    sql = """
    SELECT customerID, COUNT(*) as orderCount 
    FROM Orders 
    GROUP BY customerID 
    ORDER BY orderCount 
    DESC 
    LIMIT 1"""
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)

conn.close()