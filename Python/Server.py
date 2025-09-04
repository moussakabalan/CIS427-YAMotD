################
# Socket Programming - YAMotD
# Server.py - Demo of Server-sided request handling using Sockets (w/ YAMotD)
# Moussa Kabalan
# 06/12/25
################

from socket import *
import sys

SERVER_HOST = "" #> IP address of host. (localhost or 0.0.0.0/0 is default!)
SERVER_PORT = 12340 #> Your port of choice

DEFAULT_MOTD = "An apple a day keeps the doctor away." #> The default message of the day
SHUTDOWN_PASSWORD = "123!abc" #> The shutdown password! Just like your bank login, don't make this simple!

CURRENT_MOTD = DEFAULT_MOTD #> Don't touch this please, it's feelings are very senstive!

def _startServer():
    ## Create our TCP socket to accept requests
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((SERVER_HOST, SERVER_PORT))
    serverSocket.listen(1) #> Begin listening

    print(f"Server is ready to receive requests on port {SERVER_PORT}...")

    ## While-loop to continue taking connections + requests from clients
    while True:
        connectionSocket, addr = serverSocket.accept() #> Wait for connection from clients
        print(f"Connection successful to client: {addr[0]}:{addr[1]}!")

        isAwaitingMessage = False #> Used for MSGSTORE!

        while True:
            try: #> Try-Except wrapper to safe guard from any possible error; rimarily if the client forcibly closed the connection
                data = connectionSocket.recv(1024).decode().strip() #> Recieve data from client and read bytes
                if not data:
                    break #> If no valid data was recieved, break the loop
            
                if isAwaitingMessage: #> If MSGSTORE was requested from client, we should await for the client's next message
                    global CURRENT_MOTD
                    CURRENT_MOTD = data
                    
                    connectionSocket.send("200 OK\n".encode())
                    isAwaitingMessage = False

                    continue
            
                ## List of commands that the client can request from server
                if data == "MSGGET": #> Returns the current message of the day
                    connectionSocket.send("200 OK\n".encode())
                    connectionSocket.send(('"'+ CURRENT_MOTD + '"' + "\n").encode())

                elif data == "MSGSTORE": #> Updates the current message of the day
                    connectionSocket.send("200 OK\n".encode())
                    isAwaitingMessage = True

                elif data == "QUIT": #> Closes the connection with client
                    connectionSocket.send("200 OK\n".encode())
                    break
            
                elif data == "SHUTDOWN": #> Completely shuts down the server
                    connectionSocket.send("300 PASSWORD REQUIRED\n".encode())
                    password = connectionSocket.recv(1024).decode().strip()

                    if password == SHUTDOWN_PASSWORD:
                        connectionSocket.send("200 OK\n".encode())
                        connectionSocket.close()
                        serverSocket.close()
                        print("Server recieved request to shut down! Shutting down...")
                        sys.exit() #> Ends the process
                    else:
                        connectionSocket.send("301 WRONG PASSWORD\n".encode())
                else:
                    connectionSocket.send("400 BAD REQUEST\n".encode())
            except Exception as err:
                break
                
            ## Once the loop above breaks, we can safely close the host connection to connectionSocket.close()
            print(f"Successfully disconnected from client: {addr[0]}:{addr[1]}.")

#! This is where we run the above function.
if __name__ == "__main__":
    _startServer()
#end
