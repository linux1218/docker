import time
import pymysql
import datetime


# DROP TABLE sample_tb;
# CREATE TABLE `sample_tb`(
#   `num`            BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
#   `create_date`    DATETIME,
#   `subject`        VARCHAR(128) NOT NULL,
#   `view_count`     NUMERIC
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
# ALTER TABLE sample_tb ADD INDEX IDX_sample_tb_1(create_date ASC);
# ALTER TABLE sample_tb ADD INDEX IDX_sample_tb_2(subject ASC);


global mydb
global mycursor
global currdate


def connect_stat_db():
    global mydb
    global mycursor
    
    mydb = pymysql.connect( host='127.0.0.1', port=3306, user='root', passwd='password',db='cho_db', charset='utf8')
    mycursor = mydb.cursor()

def disconnect_stat_db():
    mycursor.close()
    mydb.close()


def insert_curr_stat_info():
    global mydb
    global mycursor
    global currdate

    sql = "INSERT INTO sample_tb \
        (create_date, subject, view_count) \
            VALUES (%s, %s, %s)"
    val = (currdate, 'subject', 1)

    mycursor.execute(sql, val)
    mydb.commit()


if __name__ == "__main__":
    connect_stat_db()
    
    try:
        while True:
            now = datetime.datetime.now()
            currdate = now.strftime('%Y-%m-%d %H:%M:%S')
            insert_curr_stat_info()
            time.sleep(10)
    except Exception as err:
        print(err)
        disconnect_stat_db()