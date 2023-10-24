import socket
import pickle

def auth():
    while True:
        port = int(input("Введите ваш логин (5 цифр) "))
        if(len(str(port))==5): 
            return port
        else:
            print("\twrong login: try again")

def start_client():
    client_port = auth()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', client_port))
    server_address = ('localhost', 10000)
    sock.connect(server_address)
    data = b""
    while True:
        packet = sock.recv(1024)
        if not packet:
            break
        data += packet
    sock.close()
    transactions = pickle.loads(data)
    print(f"Received {len(transactions)} transactions")

if __name__ == "__main__":
    start_client()
