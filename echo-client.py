import socket
import sys

def create_socket_connection(host, port):
    """Create and return a socket connection to the server."""
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        return client_socket
    except socket.error as error:
        print(f"Error connecting to the server: {error}")
        sys.exit(1)

def send_message(socket, message):
    """Send a message to the server and receive the response."""
    try:
        socket.sendall(message)
        response = socket.recv(1024)
        return response
    except socket.error as error:
        print(f"Error during message transmission: {error}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python echo-client.py <message>")
        sys.exit(1)

    message = sys.argv[1].encode("utf-8")  # Encoding the message to bytes
    host = "127.0.0.1"  # The server's IP address (localhost)
    port = 65432  # The port used by the server

    # Create the socket connection and send the message
    with create_socket_connection(host, port) as client_socket:
        response = send_message(client_socket, message)

    print(f"Received: {response.decode('utf-8')}")  # Decoding the response to a string

if __name__ == "__main__":
    main()
