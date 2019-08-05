"""

working with bytes
bytes are similar to str type, but they are a sequence of
bytes instead of unicode code points.

use for raw binary data, fixed-widtd, single byte: ASCII

use the byte() constructor
"""

d = b'data'

print(d, type(d))

info = b'some bytes here'

#split the bytes using split() method for bytes

print(info.split())


# encoding alr + 162 = ó

message = "vamos al zoológico"

print(message)

data = message.encode("utf-8")
print(data)

message_decode = data.decode("utf-8")
print(message_decode)

