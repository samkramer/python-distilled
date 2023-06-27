# 9.15.25 threading Module
import threading
import time

def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)
        
if __name__ == "__main__":
    t = threading.Thread(target=countdown, args=[5])
    t.start()
    t.join() # Wait for the thread to finish