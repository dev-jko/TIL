import time
import os

alarm_time = {
    'hour':10,
    'minute':2
}
current_time = {
    'hour':time.localtime().tm_hour,
    'minute':time.localtime().tm_minute
}
file_path = 'C:\\Users\\student\\TIL\\alarm_Exit\\alarm_img.png'

def alarm():
    while True:
        if alarm_time['hour'] == current_time['hour']:
            os.startfile(file_path)
            while True:
                if alarm_time['minute'] == current_time['minute']:
                    os.startfile(file_path)
                    return


alarm()