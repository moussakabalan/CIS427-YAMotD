################
# Socket Programming - YAMotD
# Client.py - Demo of Client-sided requests sending using Sockets (w/ YAMotD)
# Moussa Kabalan
# 06/12/25
################

from socket import *
import sys

SERVER_PORT = 12340 #> Port you are trying to connect to!

def requestInputWithMenu():
    ## This function handles all client input (+ displays a Menu for the user)!
    print("\n==== Main Menu ====")
    print("- MSGGET: Get Message of the Day")
    print("- MSGSTORE: Upload New Message")
    print("- QUIT: Exit Client")
    print("- SHUTDOWN: Shut Down Server")

    Command = input("Enter command: ").strip().upper() #> Don't forget to force uppercase the input!

    if not Command: #> No command? No problem! We'll wait for another
        return None
    else:
        return Command

def _startClient():
    ## We must ask for server ip address to connect! (For testing, just use 'localhost'!)
    if len(sys.argv) != 2:
        print("IP address is missing from parameter! Please try again.")
        return
    
    SERVER_HOST = sys.argv[1]

    ## Initalize our connection to the server.
    clientSocket = socket(AF_INET, SOCK_STREAM)

    try: #> Try-Except wrapper to safe guard from any possible error when trying to connect to server.
        clientSocket.connect((SERVER_HOST, SERVER_PORT))
    except Exception as err:
        print(f"Unable to connect to server! \nLogs: {err}")
        return
    
    print("Successfully connected to server.")

    try: #> Try-Except wrapper to safe guard from any possible error; primarily keyboard interruption (i.e: CTRL + C)
        ## While-loop to continue taking input from user to send to server.
        while True:
            Command = requestInputWithMenu()

            if not Command:
                print("Empty input! Try again.")
                continue

            if Command == "MSGGET": #> Returns the current message of the day
                clientSocket.send("MSGGET\n".encode())
                
                print(clientSocket.recv(1024).decode(), end='') #> Reponse code
                print(clientSocket.recv(1024).decode(), end='') #> Message of the day

            elif Command == "MSGSTORE": #> Updates the current message of the day
                clientSocket.send("MSGSTORE\n".encode())
                Response = clientSocket.recv(1024).decode()

                print(Response, end='') #> Reponse code

                if Response.strip() == "200 OK":
                    newMessageInput = input("Enter the new message of the day: ")
                    clientSocket.send((newMessageInput + "\n").encode())

                    print(clientSocket.recv(1024).decode(), end='') #> Reponse code

            elif Command == "QUIT": #> Closes the connection with client
                clientSocket.send("QUIT\n".encode())

                print(clientSocket.recv(1024).decode(), end='') #> Reponse code
                break

            elif Command == "SHUTDOWN": #> Completely shuts down the server
                clientSocket.send("SHUTDOWN\n".encode())
                Response = clientSocket.recv(1024).decode()

                print(Response, end='')

                if Response.strip() == "300 PASSWORD REQUIRED":
                    PasswordInput = input("Enter server password: ")
                    clientSocket.send((PasswordInput + "\n").encode())

                    shutdownResponse = clientSocket.recv(1024).decode() #> Reponse code
                    print(shutdownResponse, end='')

                    if shutdownResponse.strip() == "200 OK":
                        break
            
            else:
                print("Invalid command! Please choose from the commands in the menu.")
    except KeyboardInterrupt:
        ## In some cases when a user presses certain key combos (like CTRL + C), we must force the connection to close to prevent freezing of the program.
        print("Interrupted by user!")

    finally:
        ## Once the loop above breaks, we can safely close the connection from the server.
        clientSocket.close()
        print("Connection was successfully closed by user.") #> let the user know!

#! This is where we run the above function.
if __name__ == "__main__":
    _startClient()
#end


