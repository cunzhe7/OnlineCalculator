import socket

filename = input("Input the file name: ")
f = open(filename)
count = 0
d = 0.1
while True:
    soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    d = 0.1
    msg = str.encode(f.readline())
    while True:
        if(d>2):
            soc.close()
            print("super timeout, d is greater than 2 now, I'm goint to next line")
            break
        soc.settimeout(d)
        soc.sendto(msg,('127.0.0.1', 61111))
        try:
            msgback = bytes.decode(soc.recvfrom(1024)[0])
        except socket.timeout:
            d = d*2
            continue
        print(msgback)
        soc.close()
        break
        
    count = count + 1
    if(count == 6):
        break
