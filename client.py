import json
import socket


def main():
    HOST, PORT = "localhost", 9999
    send_data = json.dumps(
        {"id": "", "type": 200, "args": {"x": 100, "y": 100}})
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(send_data, "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(send_data))
    print("Received: {}".format(received))


if __name__ == '__main__':
    main()
