####
# STUDENT NAME: Alan Hubbard
# STUDENT NUMBER:S326012
####

userchoice = 1
while userchoice != 0:
    userchoice = input("Press 1 or 2 or 3 or 4 to run solution for 1 or 2 or 3 or 4 or press 0 to exit: ")
    if int(userchoice) == 1:
        s =  input("Enter a long string of numbers: ") #user input for number string
        number_string = "" #default number string to start as zero
        for num in s:
            if(num.isnumeric()): #confirms that the user input is a number
                number_string = number_string + num
        print("String of numbers is: ", number_string)
        length = "" #counter for length of longest string in ascending order
        current = "" #counter for length of curent of above
        for number in s:
            if len(current) == 0 or number > current[-1]: #if the ascending string is 0 or longer than previous string
                current += number #adds digits
            else: #confirms if string grew in subsequent loops
                if len(current) > len(length):
                    length = current #replaces previous ascending string "length" with "current"
                current = number
        if len(current) > len(length): #if current is greater than length, current length becomes current
            length = current
        sum = 0 #sum of longest string start
        for i in length: #identifies digits within longest ascending string
            sum += int(i) #calulates sum of digits
        avg = sum / len(length) #calulates average of digits from length of ascending string
        print("Longest substring in numeric ascending order is: ", length) #prints results of above calculations
        print("Average: ", int(avg))
    elif int(userchoice) == 2:
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
    elif int(userchoice) == 3:
        a=b=True # loop for readline function to continue until break
        first=open(input(print("Enter first file name: " )))
        second=open(input(print("Enter second file name: " ))) #opens both files, requries input from users
        while a or b: #concurently reads lines of file a or b to identify if their lines are different
             a=first.readline()
             b=second.readline()
             if a!=b: #if files are different
                  print('Files are different')
                  print(a) #prints the current line that is identified as different
                  print(b) #prints the current line that is identified as different
                  break
        else: #concurently reads lines of file a or b to identify if their lines are teh same
             print('Files are the same')
        first.close()
        second.close() #closes both files
    elif int(userchoice) == 4:
        encrypt = input("Enter text to encrypt (lowercase, no spaces only): ") #prompt for user input to encrypt
        distance = int(input("Input distance value to use for encryption: ")) #prompt for user input for distance vaule for encryption
        #print(encrypt) #TO BE DELETED
        #print(distance)#TO BE DELETED
        code = "" #counter to introduce ACSII value
        #[::-1] #reverses string order
        for ch in encrypt[::-1]: #reverses string order
            #ordvalue=ord(ch), removed code for testing and trial purposes
            #print(ordvalue), removed code for testing and trial purposes
            ciphervalue=ord(ch)+distance #converts characters (after reversal) to ACSII values
            if ciphervalue>ord('z'): #if cipher value is greater than z, encrypts that value
                #x=ciphervalue-ord('z') has been inserted to line below to reduce lines of code
                ciphervalue=ord('a')+ciphervalue-ord('z')-1
            code+=chr(ciphervalue) #reconstructs text as encrypted
        print("encrypted text is ", code )
        decrypt = input("Enter text to encrypt (lowercase, no spaces only): ") #prompt for user input to encrypt
        distance = int(input("Input distance value to use for encryption: ")) #prompt for user input for distance vaule for encryption
        code=""
        for ch in decrypt[::-1]:
            #ordvalue=ord(ch), removed code for testing and trial purposes
            ciphervalue=ord(ch)-distance #converts characters (after reversal) to ACSII values
            if ciphervalue<ord("a"): #if cipher value is less than a, encrypts that value
                #x=ord('a')-ciphervalue, coped to below line
                ciphervalue=ord('z')-ord('a')-ciphervalue+1
            code+=chr(ciphervalue)
        print('decypted text is ', code)
    elif int(userchoice) == 0:
        print("Thanks!")
        break
    else:
        print("Wrong Choice, Please try 1,2,3,4 or press 0 to exit!")
