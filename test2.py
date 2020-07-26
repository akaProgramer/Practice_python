from threading import Timer
timeout = 4
t = Timer(timeout, print, ['Sorry, times up'])
print(t)
t.start()
prompt = input("You have %d seconds to choose the correct answer...\n" % timeout)
t.cancel()