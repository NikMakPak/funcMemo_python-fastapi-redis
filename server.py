import sqlite3
import socket
import time
import redis
# сериализация
import pickle

DB_NAME = 'transactions.db'
HOST = 'localhost'
PORT = 10000


def get_transactions_by_id(id):
    connection = sqlite3.connect(DB_NAME)  # Замените 'your_database.db' на путь к вашей базе данных SQLite
    cursor = connection.cursor()

    redis_client = redis.Redis()
    start_time = time.time()
    cache_val = redis_client.get(id)
    redis_time = time.time() - start_time
    if cache_val is not None:
        print(f'-> in Redis cache. Timecost: {round(redis_time,4)}')
        return cache_val

    start_time = time.time()
    query = f"SELECT transaction_hash, logger, amount, timestamp FROM Transactions WHERE sender LIKE '%{id}%'"
    cursor.execute(query)
    result = pickle.dumps(cursor.fetchall())
    sqlite_time = time.time() - start_time
    print(f"sqlite timecost: {round(sqlite_time,4)}")
    # ex in seconds
    redis_client.set(id, result, ex=60)

    redis_client.close()
    connection.close()
    return result

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server is listening on {HOST}:{PORT}")
    
    while True:
        conn, addr = server.accept()
        print(f"new request from id #{addr[1]}")
        client_id = addr[1]
        result = get_transactions_by_id(client_id)
        conn.sendall(result)
        conn.close()

if __name__ == "__main__":
    start_server()
