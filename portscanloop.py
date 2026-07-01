import socket
s = socket.socket()
host = "microsoft.com"
count = 1
while count<=10:
    port = int(input("enter port no you want to check.."))
    result = s.connect_ex((host,port))
    if result == 0:
        print(f" port no {port} is open")
    else:
         print(f" port no {port} is close")  

    count = count +1 
s.close()
