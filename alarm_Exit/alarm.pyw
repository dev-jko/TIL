import time
import os

def getCurrentTIme():
    current_time = {
        'hour':time.localtime().tm_hour,
        'minute':time.localtime().tm_min
    }
    return current_time

def alarm(alarm_time):
    while True:
        current_time = getCurrentTIme()
        if alarm_time['hour'] == current_time['hour']:
            os.startfile(file_path)
            while True:
                current_time = getCurrentTIme()
                if alarm_time['minute'] == current_time['minute']:
                    os.startfile(file_path)
                    return
                time.sleep(10)
        time.sleep(10)


alarm_time = {
    'hour':18,
    'minute':3
}
file_path = 'C:\\Users\\student\\TIL\\alarm_Exit\\alarm_img.png'
alarm(alarm_time)