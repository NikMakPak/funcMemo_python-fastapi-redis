import sqlite3
import random
import string

DB_NAME = 'transactions.db'
def create_db(rows):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Transactions
                    (id INTEGER PRIMARY KEY,
                    transaction_hash TEXT,
                    sender TEXT,
                    logger TEXT,
                    amount REAL,
                    timestamp INTEGER)''')
    senders = ['00100', '12345', '99900']
    for _ in range(rows):
        transaction_hash = '0x' + ''.join(random.choices(string.ascii_letters + string.digits, k=18))
        sender = '0x' + random.choice(senders) + ''.join(random.choices(string.ascii_letters, k=6))
        logger = '_' + ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        amount = round(random.uniform(0.1, 10.0), 2)
        timestamp = random.randint(1635000000, 1636000000)
        
        cursor.execute('''INSERT INTO Transactions (transaction_hash, sender, logger, amount, timestamp)
                        VALUES (?, ?, ?, ?, ?)''', (transaction_hash, sender, logger, amount, timestamp))

    conn.commit()
    conn.close()

    print(f"succes! {rows} rows were added to database.")

def read_db(limit):
    print(f"Shown rows: 1-{limit}")
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = f"SELECT * FROM Transactions LIMIT {limit}"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# create_db(20)
read_db(10)
