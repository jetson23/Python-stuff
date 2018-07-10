#!/bin/python3

import socket
import struct

def send_data(sock,data): #Implement a networking protocol
    data_len = len(data)
    sock.send(struct.pack("!I",data_len))
    sock.send(data)
    return

if __name__ == '__main__':
    # Client program to connect to server and do commands
    
    # List of commands to perform on server
    command_list = ["ethtool",
                    "ifconfig",
                    "wrfile",
                    "rdfile",
                    "close"]
    
    # Create a socket object
    s = socket.socket()         
 
    # Define the port on which you want to connect
    port = 12345               
 
    # connect to the server on local computer
    s.connect(('127.0.0.1', port))
 
    cont = True
    
    while (cont == True):
        # ask for a command
        command = input("Enter a command: ")
        print (command)

        if command == "close":
            s.shutdown(1)
            cont = False
        elif command == "ifconfig":
            # receive data from the server
            #data_len = len(command)
            #sock.send(struct.pack("!I",data_len))
            s.send(command.encode())
            #send_data(s, command.encode())
            print ("recv result") 
            result = b''
            while result == b'':
                result = s.recv(2048)
                print (result)
                
            print (resuolt.decode())
        elif "ethtool" in command:
            device = input("Device: ")
            cmd = "ethtool " + device
            print (cmd)
            s.send(cmd.encode())
            print ("recv ethtool")
            
            
        else:
            print("invalid command")
    
    # close the connection
    s.close()       
    print("closed; end")