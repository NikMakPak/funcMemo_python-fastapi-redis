import socket
import pickle

def print_transactions(transactions):
    print(f"{'transaction_hash':<20} {'logger':<10} {'amount':<10} {'timestamp':<10}")
    for transaction in transactions:
        transaction_hash, logger, amount, timestamp = transaction
        print(f"{transaction_hash:<20} {logger:<10} {amount:<10} {timestamp:<10}")

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
    print(f"Received {len(transactions)} transactions for id #{client_port}")
    print_transactions(transactions[:5])

if __name__ == "__main__":
    start_client()
