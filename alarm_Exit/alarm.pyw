import time
import os
from pywinauto.application import Application
from pywinauto.win32functions import SetForegroundWindow
from pywinauto.win32functions import SetFocus

def getCurrentTIme():
    current_time = {
        'hour':time.localtime().tm_hour,
        'minute':time.localtime().tm_min
    }
    return current_time

def openfile(file_path):
    # os.startfile(path)
    # app = Application().connect(path=file_path)
    app = Application().start('mspaint.exe' + ' ' + file_path)
    w = app.top_window()
    # Application().win
    # SetFocus(w.wrapper_object())
    # SetForegroundWindow(w.wrapper_object())
    

def alarm(alarm_time, start_file_path, end_file_path):
    time.sleep(2)
    openfile(start_file_path)
    while True:
        current_time = getCurrentTIme()
        if alarm_time['hour'] == current_time['hour']:
            openfile(end_file_path)
            while True:
                current_time = getCurrentTIme()
                if alarm_time['minute'] == current_time['minute']:
                    openfile(end_file_path)
                    return
                time.sleep(10)
        time.sleep(10)


alarm_time = {
    'hour':18,
    'minute':3
}
start_file_path = r'C:\\Users\\student\\TIL\\alarm_Exit\\start_alarm_img.png'
end_file_path = r'C:\\Users\\student\\TIL\\alarm_Exit\\end_alarm_img.png'
alarm(alarm_time, start_file_path, end_file_path)