from abc import ABC, abstractmethod

class Stream(ABC):
    @abstractmethod
    def receive(self):
        pass
    
    @abstractmethod
    def send(self):
        pass
    
    @abstractmethod
    def close(self):
        pass
    
# Method signatures checked at runtime
class SocketStream(Stream):
    def receive(self):
        print("called SocketStream::receive()")
    
    def send(self):
        print("called SocketStream::send()")
        
    def close(self):
        print("called SocketStream::close()")
    
if __name__ == '__main__':
    # TypeError: Can't instantiate abstract class Stream
    # s = Stream()
    
    s = SocketStream()
    s.send()
    