import socket
s = socket.socket()
try:
    host = input("enter host  ")
    port = int(input("enter port no  "))

    result = s.connect_ex((host, port))
    if result == 0:
        print(f"port no {port} is open")
    else:
        print(f"port no {port} is close")
except ValueError:
    print("plz enter valid input")
except socket.gaierror:
    print("plz enter valid host name")    
finally:
    s.close()

    