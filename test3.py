import threading, time
 
def DoSomething():
    for i in range(100):
        print(i)
        time.sleep(1)
 
if __name__=='__main__':
    t=threading.Thread(target=DoSomething)
    t.setDaemon(True)
    t.start()
    if t.isAlive():
        print("daemon is alive")
        t.join(12)
        print('stop!')
