import time
import pymysql
import datetime
import os

global mydb
global mycursor
global currdate

def connect_db():
    global mydb
    global mycursor
    
    # mydb = pymysql.connect( host='127.0.0.1', port=5909, user='cho', passwd='Qwer1234!',db='cho_db', charset='utf8')
    mydb = pymysql.connect( host='DB', port=5909, user='cho', passwd='Qwer1234!',db='cho_db', charset='utf8')
    mycursor = mydb.cursor()

def disconnect_db():
    mycursor.close()
    mydb.close()

def insert_info():
    global mydb
    global mycursor
    global currdate
    
    sql = "INSERT INTO sample_tb \
        (create_date, hostname) \
            VALUES (%s, %s)"
    val = (currdate, os.name)

    print("insert sample_tb")
    mycursor.execute(sql, val)
    mydb.commit()


if __name__ == "__main__":
    connect_db()
    try:
        while True:
            now = datetime.datetime.now()
            currdate = now.strftime('%Y-%m-%d %H:%M:%S')
            insert_info()
            time.sleep(60)
    except Exception as err:
        print(err)
        disconnect_db()