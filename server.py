#!/bin/python3

import os
import socket
import struct
import subprocess

if __name__ == '__main__':
    # Server to listen for connections and process commands
     
    # List of commands to perform on server
    command_list = ["ethtool",
                    "ifconfig",
                    "wrfile",
                    "rdfile",
                    "close"]

    # next create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
 
    # reserve a port on your computer in our
    # case it is 12345 but it can be anything
    port = 12345               
 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests man 
    # coming from other computers on the network
    
    # Add IP address
    s.bind(('127.0.0.1', port))        
    print ("socket binded to", port)
 
    # put the socket into listening mode
    s.listen(5)     
    print ("socket is listening")          
 
    # Establish connection with client.
    conn, addr = s.accept()     
    print ('Got connection from', addr)

    # a forever loop until we stop or an error occurs
    cont = True
    while (cont == True):
        # get command from the client. 
        print ("b4 recv")
        cmd = conn.recv(1024)
        #data_len, = struct.unpack("!I",s.recv(4))
        #cmd = s.recv(data_len)
        
        print (cmd)
        if cmd == b'':
            print ("shutdown")
            s.shutdown(1)
            s.close()
            break
        
        print ("deccode")
        cmds = cmd.decode().strip()
        #cmds = str(cmdd)
        print (cmds)
        

        #if cmd.decode("utf-8").strip() == "IFCONFIG":
        if cmds == 'ifconfig':
            print ("ifconfig")
            p = subprocess.Popen("ifconfig", stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            print (output.decode())
            conn.send(output)  # already encoded here
            
        elif 'ethtool' in cmds:
            print ("ethtool")
            print (cmds)
            
            p = subprocess.Popen(cmds, stdout=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            print (output.decode())
            conn.send(output)  # already encoded here
            
        elif cmds == 'close':
            cont = False
        else:
            print ("command not recognized")
            cont = False
           
		
    # Close the connection with the client
    conn.close()
    print ("Conn closed")