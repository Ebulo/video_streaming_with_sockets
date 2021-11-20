import cv2, socket, struct

ip = socket.gethostbyname(socket.gethostname())
port = 1001

soc = socket.socket()

soc.connect((ip, port))