# -*- coding : UTF-8 -*-
from requests import *
from bs4 import BeautifulSoup
import sqlite3
import time as sleep

i = 0
'''
여기서 i의 쓰임은 두가지입니다.
 1. 실검을 parsing 할 때 사용함.
 2. 실검 달성 횟수를 출력할 때 쓰임.
'''

dbname = "naverSilSiGan.db"     # 데이터를 저장할 DB 서버와 연결할 DB 네임 설정
time = 0        # 몇 초 돌렸는지 확인하기 위해

# 여기서 무한루프 실행
while True:

    # 밑의 아래 5줄의 코드는 실검을 받아오기 위한 작업임.
    url = "http://www.naver.com/"
    r = get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    options = soup.find_all('option')
    silsigan = []



    # 실검을 리스트형으로 저장함
    # 리스트 형으로 저장하는 이유는 for 문에서 사용하기 위함임.
    for op in options:
        op = op.string
        op = str(op)
        if op.find("위") > 0:
            i = i + 1
            str_num = op.find(":")
            op = op[str_num+2:]
            #print(str(i) + " 위 ==> "+ op)          #디버깅 용도의  print()
            silsigan.append(op)

    #print(silsigan)                                 #디버깅 용도의 print()


    for s in silsigan:
        query = "SELECT * FROM naver WHERE search='%s'" % s
        conn = sqlite3.connect(dbname)
        c = conn.cursor()
        row = c.execute(query).fetchall()
        #print(len(row))                            #디버깅 용도의 print()


        if len(row) == 0:   #DB에 값이 없을 때
            query = "INSERT INTO naver (search, no) VALUES ('%s', 1)" % s
            insertConn = sqlite3.connect(dbname)
            insertCursor = insertConn.cursor()
            insertCursor.execute(query)
            insertConn.commit()
            insertCursor.close()
            insertConn.close()

        elif len(row) > 0:     #DB에 값이 있을 때
            set = row[0][1] + 1
            print(str(set))
            query = "UPDATE naver SET no=%d WHERE search LIKE '%s' " % (set, s)
            updateConn = sqlite3.connect(dbname)
            updateCursor = updateConn.cursor()
            updateCursor.execute(query)
            updateConn.commit()
            updateCursor.close()
            updateConn.close()



    # 실검 달성 횟수를 내림차순으로 출력하는 코드
    i = 1
    print("\n\n")
    query = "SELECT * FROM naver ORDER BY no DESC LIMIT 10"
    for row in sqlite3.connect(dbname).cursor().execute(query).fetchall():
        print("현재 %d위 : %s                  (총 실검 달성 횟수 : %s)" % (i, row[0], row[1]))
        i += 1

    timeMinute = time / 60
    timeHour = timeMinute / 60
    print("\n#### 10초 기다림 #### ( 현재 통계 사용 시간 : %d 시간 %d 분 %d 초 )" % (timeHour, timeMinute, time), end="")
    time += 10          # 사용시간 10초 추가!
    sleep.sleep(10)
