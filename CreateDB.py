#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sqlite3

# DB 생성 및 sqlite3의 커넥트, 커서 객체 생성
conn = sqlite3.connect("naverSilSiGan.db")
cursor = conn.cursor()

# sqlite 쿼리 작성
query = """CREATE TABLE `naver` (
	      `search`	TEXT NOT NULL,
	      `no`	INTEGER NOT NULL,
	      PRIMARY KEY(`no`)
          );"""

# 쿼리 실행
cursor.execute(query)
