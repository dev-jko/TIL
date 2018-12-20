import time
import os
import win32gui, win32con

def getCurrentTIme():
    current_time = {
        'hour':time.localtime().tm_hour,
        'minute':time.localtime().tm_min
    }
    return current_time

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        if ('사진' in win32gui.GetWindowText(hwnd)):
            win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
            # win32gui.SetForegroundWindow(hwnd)

def openfile(file_path):
    os.startfile(file_path)
    time.sleep(0.5)
    win32gui.EnumWindows(enumHandler, None)
    

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