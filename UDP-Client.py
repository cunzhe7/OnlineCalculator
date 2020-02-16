import socket

filename = input("Input the file name: ")
f = open(filename)
count = 0

while True:
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = str.encode(f.readline())
    soc.sendto(msg,('127.0.0.1', 61111))

    msgback = bytes.decode(soc.recvfrom(1024)[0])
    print(msgback)
    soc.close()
    count = count + 1
    if(count == 6):
        break
