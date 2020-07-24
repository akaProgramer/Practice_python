import psutil

def checkIfProcessRunning(processName):
    '''(
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                # return True
                processID=proc.num_handles()
                print(processName , ' ::: ', processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

checkIfProcessRunning('zoom')

# if checkIfProcessRunning('zoom'):
#     print('Yes a zoom process was running')
# else:
#     print('No zoom process was running')
# for proc in psutil.process_iter():
#     if 'zoom' in proc.name().lower():
#         print(proc.name())
# for proc in psutil.process_iter():
#     print(proc)
# processName="zoom"
# for proc in psutil.process_iter():
#     try:
#         # Get process name & pid from process object.
#         if processName.lower() in proc.name().lower():
#         processName = proc.name()
#         processID = proc.is_running()
#         print(processName , ' ::: ', processID)
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass