import socket

filename = input("Input the file name: ")
f = open(filename)
count = 0

while True:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(('127.0.0.1',61111))
    msg = f.readline()
    soc.send(str.encode(msg))

    data = bytes.decode(soc.recv(1024))
    print(data)
    soc.close()
    count = count + 1
    if(count == 6):
        break
