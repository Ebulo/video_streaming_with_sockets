import cv2, socket, struct, random

ip = socket.gethostbyname(socket.gethostname())
port = 1002

soc = socket.socket()

soc.connect((ip, port))

def createMsg():
  print("Creating A Message")
  list_of_words =["Hey buddy","","Greetings!","Hey there!","What a surprise! Welcome bud","Hey there! Nice to meet you","How are you doing!","Hey"]
  msg = list_of_words[random.randInt(0, len(list_of_words)-1)]
  return msg
