import webbrowser
import subprocess
import pyautogui
import time
import psutil
import datetime
import socket

class class_joiner():
    
    current_time = datetime.datetime.today().strftime("%H:%M:%S")


    def is_connected(self):
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

    def lec_no(self):
    current_time = datetime.datetime.today().strftime("%H:%M:%S")
    #print(current_time)
    if self.current_time <= "10:15:00" and self.current_time >= "09:55:00":
        return 1
    elif self.current_time <= "10:45:00" and self.current_time >= "10:30:00":
        return 2
    elif self.current_time <= "11:20:00" and self.current_time >= "11:05:00":
        return 3
    elif self.current_time <= "11:55:00" and self.current_time >= "11:40:00":
        return 4
    elif self.current_time <= "12:35:00" and self.current_time >= "12:15:00":
        return 5
    else:
        return "Timming is not correct"
    
    def checkIfProcessRunning(self,processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                process_handles=proc.num_handles()
                if process_handles >900:
                    if process_handles >=1150:
                        return True
                    elif process_handles <= 1150 and process_handles >=980:
                        proc.terminate()
                        return False
                    else:
                        return False
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

    