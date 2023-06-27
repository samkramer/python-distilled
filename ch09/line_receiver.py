# 9.12 Consuming Input

# Enhanced generator that receives byte fragments
# and assembles them into lines
def line_receiver():
    data = bytearray()
    line = None
    linecount = 0
    while True:
        part = yield line
        linecount += part.count(b'\n')
        data.extend(part)
        if linecount > 0:
            index = data.index(b'\n')
            line = bytes(data[:index+1])
            data = data[index+1:]
            linecount -= 1
        else:
            line = None
    
# import line_receiver
# r = line_receiver.line_receiver()
# r.send(None)    # Necessary first step
# r.send(b'hello')
# r.send(b'world\nit ')
# Out: b'helloworld\n'
# r.send(b'works!')
# r.send(b'\n')
# Out: b'works!\n'