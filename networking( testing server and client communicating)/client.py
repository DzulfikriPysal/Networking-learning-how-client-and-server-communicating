import socket               # Import socket module 
import webbrowser

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 666                # Reserve a port for your service.

s.connect((host, port)) 

input = "1"

if( input == "1"): 
	output = 'request 1' 
	s.sendall(output.encode('utf-8')) # send to the server the type of request
	From_server = s.recv(1024).decode()
	print (From_server)
	From_server2 = s.recv(1024).decode()
	print (From_server2)
	webbrowser.open_new_tab(From_server2)
	#webbrowser.open(From_server2, new=2)
else: 
	output = 'request 2' 
	s.sendall(output.encode('utf-8')) # send to the server the type of request
	From_server = s.recv(1024).decode()
	print (From_server)
	From_server2 = s.recv(1024).decode()
	print (From_server2)
	
 
s.close                     # Close the socket when done.
