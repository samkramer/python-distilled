# 9.15.25 threading Module
# If one thread must wait for another thread to do something, use an Event
import threading
import time

def step1(evt):
    print('Step 1')
    time.sleep(1)
    evt.set()
    
def step2(evt):
    evt.wait()
    print('Step 2')
    
if __name__ == "__main__":
    evt = threading.Event()
    threading.Thread(target=step1, args=[evt]).start()
    threading.Thread(target=step2, args=[evt]).start()