import socket
import struct

from HatonMatrix import *
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

hexStr = HatonMatrix().createUDPHex(inPort=29, outPort=5)
print(hexStr)
print('01303157524D303034303143334604')
data = bytearray.fromhex(hexStr)


# 构造数据

# 发送数据
s.sendto(data, ('10.53.3.34', 5000))

# 打印回传
print(s.recvfrom(1024)[0].hex())

# 关闭连接
s.close()
