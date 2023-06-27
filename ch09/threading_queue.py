# 9.15.25 threading Module
# If threads are going to communicate, use a Queue
import threading
import queue

def producer(q):
    for i in range(1, 11):
        print('Producing:', i)
        q.put(i)
    
    q.put(None)
    
    for i in range(11, 16):
        print('Producing:', i)
        q.put(i)
        
    print('Producer finished')

def consumer(q):
    while not q.empty():
        item = q.get()
        if item is None:
            break
        print('Consuming:', item)
    print('Consumer finished')
    
if __name__ == "__main__":
    q = queue.Queue()
    threading.Thread(target=producer, args=[q]).start()
    threading.Thread(target=consumer, args=[q]).start()