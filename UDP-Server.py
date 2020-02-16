import socket

def isInt(str):
    try:
        int(str)
        return True
    except ValueError:
        return False 

def isValid(d):
    x = d.split()
    if(len(x) is not 3):
        return False
    if(x[0] not in ['+','-','*','/']):
        return False
    if(isInt(x[1]) is False or isInt(x[2]) is False):
        return False
    if(x[0] is '/' and x[2] is "0"):
        return False
    return True
def calculate(d):
    x = d.split()
    if(x[0] is '+'):
        return int(x[1]) + int(x[2])
    if(x[0] is '-'):
        return int(x[1]) - int(x[2])
    if(x[0] is '*'):
        return int(x[1]) * int(x[2])
    else:
        return int(x[1]) / int(x[2])

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind(('127.0.0.1', 61111))
print ("The UDP server is ready to receive")
while True:
    data, addr = soc.recvfrom(1024)
    data = bytes.decode(data)
    if(isValid(data)):
        x = data.split()
        result = "Status Code: 200, the result of " + x[1] +" " + x[0] + " " + x[2] + " is: "+ str(calculate(data))
        soc.sendto(str.encode(result),addr)
    else:
        soc.sendto(str.encode("Status Code: 300, Something Wrong, result: -1"),addr) 
soc.close()