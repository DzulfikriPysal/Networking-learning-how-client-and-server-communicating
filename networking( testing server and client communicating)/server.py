#!/usr/bin/python # This is server.py file

import socket # Import socket module

s = socket.socket() # Create a socket object
host = socket.gethostname() # Get local machine name
port = 666 # Reserve a port for your service.
s.bind((host, port)) # Bind to the port

s.listen(5) # Now wait for client connection.

print("Waiting for Client Connecting to the server...")

a = True

while a == True:
	c, addr = s.accept() # Establish connection with client.
	
	output = "You send something to me, wait i check it now!!"
	c.sendall(output.encode('utf-8'))
	
	print ("Got connection from", addr) #check who connect to the server now
	 
	client_request = c.recv(1024).decode() # get request from client
	print (client_request)
	
	if( client_request == "request 1" ):	#server give response based on what client requesting
		output = "localhost"
		c.sendall(output.encode('utf-8'))
	else:
		output = "Request Not Available"
		c.sendall(output.encode('utf-8'))
	

	c.close()
	a = False # end the server when receive one request