import socket
host = "scanme.nmap.org"
port = 21
s = socket.socket()
Result = s.connect_ex((host,port))

if Result == 0:
    print(f"port {port} is open")
else:
    print(f"port {port} is closed")    
s.close()