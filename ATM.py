balance = 500

witdrawal = int(input("How much money do you want to withdraw:"))

if witdrawal <= 0:
    print("Invalid amount, you must withdraw more that R0")
elif witdrawal <= balance:
    left = balance - witdrawal
    print(f"Withdrawal successful! Remaining balance: R{left}")
else:
 print( "Declined. Insufficient funds")
