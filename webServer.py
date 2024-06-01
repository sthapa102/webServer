# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    # Creates server's TCP socket using IPv4 Network.
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Prepare a server socket to associate server port number to this socket.
    serverSocket.bind(("", port)) # welcoming socket for three-way handshake.
    # Server listens for TCP connection requests from the client, with max queued connection of 1.
    serverSocket.listen(1)
    # Fill in start

    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        # The program invokes the accept() method for serverSocket, which creates a new socket in the server, called connectionSocket,
        # dedicated to this particular client. The client and server then complete the handshaking, creating a TCP connection between
        # the client’s clientSocket and the server’s connectionSocket.
        connectionSocket, addr = serverSocket.accept()  # Fill in start - accepting connections  # Fill in end
        try:
            # Buffer size 2048 as input. **This buffer size works for most purposes**
            # It takes the line sent by the client converts the message to a string.
            message = connectionSocket.recv(2048).decode() # Fill in start - client sending a message  # Fill in end
            filename = message.split()[1]
            # Opens the client requested file.
            # Plenty of guidance online on how to open and read a file in python. How should you read it though if you plan on sending it through a socket?
            f = open(filename[1:], 'rb')  # fill in start # fill in end)
                     # fill in end
            outputdata = b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n"
            # Fill in start - This variable can store your headers you want to send for any valid or invalid request.
            # Content-Type above is an example on how to send a header as bytes
            # Fill in end
            # Send an HTTP header line into socket for a valid request. What header should be sent for a response that is ok?
            # 200 OK: Request succeeded and the information is returned in the response.
            # Note that a complete header must end with a blank line, creating the four-byte sequence "\r\n\r\n"
            # Fill in start

            # Fill in end

            # Send the content of the requested file to the client
            for i in f:  # for line in file
                outputdata += i
            connectionSocket.send(outputdata)
            # Fill in start - send your HTML file contents # Fill in end
            connectionSocket.close()  # closing the connection socket

        except Exception as e:
            connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
            connectionSocket.send("404 Not Found".encode())
    # Send response message for invalid request due to the file not being found (404)
    # Fill in start

    # Fill in end

    # Close client socket
            connectionSocket.close()
    # Fill in start

    # Fill in end

    # Commenting out the below, as it's technically not required and some have moved it erroneously in the while loop. DO NOT DO THAT OR YOU'RE GONNA HAVE A BAD TIME.
    # serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
