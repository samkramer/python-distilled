# 9.15.25 threading Module
import threading
import random

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1

    def decrement(self):
        with self.lock:
            self.value -= 1
    
    def get_value(self):
        with self.lock:
            return self.value
            
        
def test_counter(counter, ntimes):
    
    n = 0
    while n < ntimes:
        rand_val = random.randrange(0,2)
        if rand_val == 0:
            counter.decrement()
        elif rand_val == 1:
            counter.increment()
        n += 1


if __name__ == "__main__":
    counter = Counter()
    t1 = threading.Thread(target=test_counter, args=[counter, 100])
    t2 = threading.Thread(target=test_counter, args=[counter, 100])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"Counter value: {counter.get_value()}")