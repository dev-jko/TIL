# 채팅 어플리케이션

## framework & library
- 서버
    - django(python)
    - mosquitto(MQTT broker)
    - paho(MQTT pub)
- 클라이언트
    - android(kotlin)
    - paho(MQTT sub)

## 통신
- 클라이언트에서 서버로 채팅 메세지를 보낼 때 -> HTTP
- 서버에서 클라이언트로 채팅 메세지를 보낼 때
    - 포어그라운드 : socket
    - 백그라운드 : MQTT(pub/sub), longPolling, FMS

    ### URLs
    1. `accounts/`
        - `signup/` POST, 회원가입
        - `<int:user_id>/` GET, 유저 정보 가져오기
        - `<int:user_id>/friends/` GET, 유저의 친구 목록 가져오기
        - `<int:user_id>/friends/<int:friend_id>/` POST, 친구 추가/삭제하기
        - `<int:user_id>/chats/` GET, 유저의 채팅방 목록 가져오기
    2. `chats/`
        - `''` POST, 채팅방 추가하기
        - `<int:chat_id>/` DELETE, 채팅방 삭제하기
        - `<int:chat_id>/messages/` GET, 채팅방의 메세지 가져오기
        - `<int:chat_id>/messages/` POST, 채팅방에 메세지 보내기
        - `<int:chat_id>/messages/<int:message_id>/` PATCH, 메세지 삭제하기('삭제된 메세지 입니다.'로 내용 변경)
        - `<int:chat_id>/users/` GET, 채팅방에 있는 유저 목록 가져오기
        - `<int:chat_id>/users/<int:user_id>/` POST, 채팅방에 유저 추가하기
        - `<int:chat_id>/users/<int:user_id>/` DELETE, 채팅방에 유저 나가기/강제 퇴장 시키기
        - `<int:chat_id>/users/<int:user_id>/messages/<int:message_id>/` PATCH, 채팅방에서 유저가 확인한 마지막 메세지 갱신하기


## Authentication
- token 방식
- accounts.User
    - username(unique)
    - password


## DB
1. User

    | User     |          |
    |----------|----------|
    | id       | int, PK, AUTOINCREMENT |
    | username | char, UNIQUE |
    | password | char     |

2. Token

    | Token     |          |
    |----------|----------|
    | token       | char, PK |
    | user_id | int, FK(User, id) |

3. Friend, Block 

    | Friend, Block     |          |
    |----------|----------|
    | id       | int, PK, AUTOINCREMENT |
    | user_id | int, FK(User, id) |
    | target_id | int, FK(User, id) |
    | type(1친구, 2차단)->type 테이블 나누기 | int |

4. Chat

    | Chat     |          |
    |----------|----------|
    | id       | int, PK |

5. Message

    | Message     |          |
    |----------|----------|
    | id       | int, PK |
    | content | char |

6. User-Chat

    | User-Chat     |          |
    |----------|----------|
    | id       | int, PK, AUTOINCREMENT |
    | user_id | int, FK(User, id) |
    | chat_id | int, FK(Chat, id) |
    | last_message_id(마지막으로 읽은 메세지) | int, FK(Message, id) |
