#!/bin/python3

import socket

if __name__ == '__main__':
    # Server to listen for connections and process commands
              
    # next create a socket object
    s = socket.socket()         
    print "Socket successfully created"
 
    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 12345               
 
    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests 
    # coming from other computers on the network
    
    # Add IP address
    s.bind(('127.0.0.1', port))        
    print "socket binded to %s" %(port)
 
    # put the socket into listening mode
    s.listen(5)     
    print "socket is listening"           
 
    # a forever loop until we interrupt it or 
    # an error occurs
    while True:
 
        # Establish connection with client.
        conn, addr = s.accept()     
        print 'Got connection from', addr
 
        # send a thank you message to the client. 
        conn.send('Thank you for connecting')
 
        # Close the connection with the client
        conn.close()