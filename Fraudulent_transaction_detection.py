from datetime import datetime

DATE_FMT = "%Y-%m-%d %H:%M:%S"

def find_fraud():
    n = int(input())
    transactions = []

    # 1. Read all transactions
    for i in range(n):
        parts = input().split()
        tx_id = parts[0]
        user_id = parts[1]
        amount = float(parts[2])
        timestamp = datetime.strptime(parts[3] + " " + parts[4], DATE_FMT)
        transactions.append([tx_id, user_id, amount, timestamp])

    print(transactions)
    flagged = set()

    # 2. Rule 1: Threshold check (simple loop)
    for tx in transactions:
        if tx[2] > 10000:
            flagged.add(tx[0])

    # 3. Rule 2: Velocity check . It uses a lambda function to access index 3 of each transaction tuple,
    #  which holds the timestamp string ("YYYY-MM-DD HH:MM:SS").this correctly orders the transactions from earliest to latest.
    transactions.sort(key=lambda tx: tx[3])

    for i, (tx_id_i, user_i, amt_i, time_i) in enumerate(transactions):
        count = 0
        for j, (tx_id_j, user_j, amt_j, time_j) in enumerate(transactions[:i + 1]):
            if user_j == user_i:
                diff = (time_i - time_j).total_seconds()
                if 0 <= diff <= 300:
                    count += 1
        if count > 2:
            flagged.add(tx_id_i)

    # 4. Print result
    print("fraudulant transanctions are : ")
    if not flagged:
        print("None")
    else:
        for tx_id in flagged:
            print(tx_id)

find_fraud()

# example i/p - directly to be entered into the terminal
# 5
# TX1 U1 100 2026-03-20 10:00:00
# TX2 U1 200 2026-03-20 10:01:00
# TX3 U1 300 2026-03-20 10:02:00
# TX4 U1 400 2026-03-20 10:04:00
# TX5 U2 50000 2026-03-20 10:00:00