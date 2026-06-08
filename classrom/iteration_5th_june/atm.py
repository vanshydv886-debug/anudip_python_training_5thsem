transactions = [5000, -2000, 3000, -1000, -500, 7000]

balance = 0
deposits = []
withdrawals = []

# Calculate balance and separate deposits/withdrawals
for i in transactions:
    balance += i

    if i > 0:
        deposits.append(i)
    else:
        withdrawals.append(i)

# Largest Deposit
largest_deposit = deposits[0]
for i in deposits:
    if i > largest_deposit:
        largest_deposit = i

# Largest Withdrawal
largest_withdrawal = withdrawals[0]
for i in withdrawals:
    if i < largest_withdrawal:
        largest_withdrawal = i

print("Current Balance:", balance)
print("Deposits:", deposits)
print("Withdrawals:", withdrawals)
print("Largest Deposit:", largest_deposit)
print("Largest Withdrawal:", largest_withdrawal)