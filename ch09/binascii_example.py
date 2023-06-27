# 9.15.2 binascii Module
# https://docs.python.org/3/library/binascii.html

## Type following commands into python console:
    
# >>> import binascii
# >>> binascii.b2a_hex(b'hello')
# Out: b'68656c6c6f'
# >>> binascii.a2b_hex(_)
# Out: b'hello'
# >>> binascii.b2a_base64(b'hello')
# Out: b'aGVsbG8=\n'
# >>> binascii.a2b_base64(_)
# Out: b'hello'

# >>> a = b'hello'
# >>> a.hex()
# Out: '68656c6c6f'
# >>> bytes.fromhex(_)
# Out: b'hello'
# >>> import base64
# >>> base64.b64encode(a)
# Out: b'aGVsbG8='