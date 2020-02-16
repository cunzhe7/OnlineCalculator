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

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind(('127.0.0.1', 61111))
print ("The TCP server is ready to receive")
soc.listen()
while True:
    conn, addr = soc.accept()
    # print('connect with ', addr)
    data = bytes.decode(conn.recv(1024))
    if(isValid(data)):
        x = data.split()
        result = "Status Code: 200, the result of " + x[1] +" " + x[0] + " " + x[2] + " is: "+ str(calculate(data))
        conn.send(str.encode(result))
    else:
        conn.send(b"Status Code: 300, Something Wrong, result: -1")   
    conn.close()
soc.close()