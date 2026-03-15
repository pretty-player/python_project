import socket

def start_client():
    # 1. Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Connect to the server
    host = '127.0.0.1'
    port = 12345
    print(f"Connecting to {host}:{port}...")
    client_socket.connect((host, port))

    # 3. Receive data (buffer size 1024 bytes)
    data = client_socket.recv(1024)
    
    # 4. Decode and display the message
    print(f"Message from Server: {data.decode('utf-8')}")

    # 5. Close the socket
    client_socket.close()

if __name__ == "__main__":
    start_client()