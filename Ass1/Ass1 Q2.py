while True: #begins loop that stops on "-1" input, break condition
    acc_no = int(input("Enter account number (-1 to end): "))
    if acc_no == -1: #creates break condition
        break
    begin = float(input("Enter beginning balance: "))
    debit = float(input("Enter total charges: "))
    credit = float(input("Enter total credits: "))
    limit = float(input("Enter credit limit: ")) #requests user input for numbers to begin calculation
    balance = begin+debit-credit #equation to calculate current balance
    if balance > limit: #if condition in the event the balance is greater than the allowed limit
        print("Account: ", acc_no)
        print("Credit Limit: ", limit)
        print("Balance: ", balance)
        print("Credit Limit Exceeded.","\n") #prints account number, limit, balance and "Credit Limit Exceeded"
    else:
        print("\n") #additional line break between results.
