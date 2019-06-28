# '작심평생' Backend-server 

## 개발 환경
- python 3.6
- Flask
- Sokect.io

프로젝트 개요
------------------------

#### 앱 '작심평생'의 Backend-server
 '작심평생'은 작심삼일로 끝나기 쉬운 단기 또는 장기 목표를 다른 이용자들과 함께 서로 목표를 이뤄나가는 과정에서
  과금과 상금을 통해서 목표를 이룰 수 있도록 장려하는 어플입니다.
 
 
사용법
-------------------------
```
python app.py
```

API
---------------------

- 회원가입
    ```
    [POST] /regist < = ( id, password, username )
    ```
- 중복 검사
    ```
    [POST] /checkID < = ( id )
    ```
- 로그인
    ```
    [POST] /login < = ( id, password )
    ```
- 현재 참여중인 목표 목록
    ```
    [POST] /getMyList < = ( id )
    ```    
- 모집중인 목표 목록
    ```
    [POST] /getWaitingList < = ( duration )
    ```
    duration(기간)별로 검색
- 목표 공유방 생성
    ```
    [POST] /addRoom < = ( id, goalName, goalDescription, duration, money, userNum )
    ```
- 목표 공유방 참석
    ```
    [POST] /joinRoom < = ( id, goal_id )
    ```
- 목표 공유방 랭킹 조회
    ```
    [POST] /getRank < = ( goal_id )
    ```
- 목표 공유방 상세정보 검색
    ```
    [POST] /getGoalInfo < = ( goal_id )
    ```
- 목표 공유 시작
    ```
    [POST] /start < = ( goal_id )
    ```
    Socket.IO로 대체해야 함 

개선 방향
---------------------

- 실시간 통신이 필요한 부분 Socket.IO 또는 다른 프레임워크를 사용하여 개선
- 통신 중 불필요한 데이터, 보안이 필요한 데이터 개선 
