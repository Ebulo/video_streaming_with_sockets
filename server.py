import cv2, socket, struct

ip = socket.gethostbyname(socket.gethostname())
port = 1001

soc = socket.socket()

soc.bind((ip, port))

soc.listen(5)

addr, ip_ = soc.accept()

print(addr, ip_)