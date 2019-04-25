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

