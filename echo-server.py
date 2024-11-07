import socket

def create_server_socket(host, port):
    """Create and bind a server socket to the given host and port."""
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server is listening on {host}:{port}")
        return server_socket
    except socket.error as error:
        print(f"Error creating server socket: {error}")
        exit(1)

def handle_client_connection(connection):
    """Handle communication with the connected client."""
    with connection:
        print(f"Connected by {connection.getpeername()}")
        while True:
            data = connection.recv(1024)
            if not data:
                break
            # Process and send the response to the client
            response = data + b" Response from server."
            connection.sendall(response)

def main():
    host = "127.0.0.1"  # Localhost address
    port = 65432  # Port to listen on

    # Set up the server socket and accept incoming connections
    with create_server_socket(host, port) as server_socket:
        while True:
            client_connection, client_address = server_socket.accept()
            handle_client_connection(client_connection)

if __name__ == "__main__":
    main()
