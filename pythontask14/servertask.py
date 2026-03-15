import socket

def start_server():
    # 1. Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Bind the socket to the address and port
    host = '127.0.0.1' # Localhost
    port = 12345
    server_socket.bind((host, port))

    # 3. Listen for incoming connections (allow 1 client in queue)
    server_socket.listen(1)
    print(f"Server started. Listening on {host}:{port}...")

    while True:
        # 4. Accept the connection
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # 5. Send a welcome message (Data must be encoded to bytes)
        message = "Welcome to the Python Server! Data transmitted successfully."
        client_socket.send(message.encode('utf-8'))

        # 6. Close the connection with this specific client
        client_socket.close()
        break # Exit loop for this demo

if __name__ == "__main__":
    start_server()