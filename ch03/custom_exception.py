# 3.4.3 Defining New Excpetions

class NetworkError(Exception):
    pass

class HostnameError(NetworkError):
    pass

class TimeoutError(NetworkError):
    pass

class DeviceError(Exception):
    def __init__(self, errno, msg):
        self.args = (errno, msg)
        self.errno = errno
        self.errmsg = msg
        
def error1():
    raise HostnameError('Unknown host')
        
if __name__ == '__main__':
    try:
        raise DeviceError(1, 'Not Responding')
    except Exception as e:
        print(f"Error: {e}")
        
    print()
        
    try:
        error1()
    except NetworkError as e:
        if type(e) is HostnameError:
            print(f"Error: {e}")
            print('Custom handling of HostnameError...')
    
    