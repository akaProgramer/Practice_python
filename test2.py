from threading import Timer
timeout = 6
t = Timer(timeout, print, ['Sorry, times up'])
t.start()
prompt = input("You have %d seconds to choose the correct answer...\n" % timeout)
t.cancel()