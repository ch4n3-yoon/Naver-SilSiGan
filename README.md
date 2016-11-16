# Naver-SilSiGan
NaverSilSiGan.py
(for Koreans who want to know Naver's real time query)

기능 :
 1. 네이버의 실시간 검색어를 가져옵니다. 
 2. 그 후 DB에 저장하고 만약 이미 실검 순위에 있다면 no라는 값을 +1 합니다.
 3. 이 때, no를 +1 하는 이유는 실검 순위에 있었던 것을 +1 함으로써 count 하기 위함입니다. 
 4. 지금은 텀을 10초로 해서 통계를 내기 어렵지만, 오랫동안 데이터를 수집한다면 유용한 통계를 낼 수 있으리라 생각됩니다.

일단 DB를 create하는 파이썬 프로그램을 실행하십시오. 
