# Question 1
# This program will prompt user to give string to find the longest substring in which the numbers are in ascending
# order. In the cases of ties for longest substring, it will take the first one. After which, it will calculate the
# average of each digit in the longest substring.

'''s = input("Enter a string of numbers: ") # Prompt user for number string

# Finding the longest substring
longest = "" # Counter for longest substring
current = "" # Counter used for when trying to find longest substring
for i in s: # For loop breaks down string into each iterable individual character
    if len(current) == 0 or i > current[-1]: # Condition if current substring is zero or the digit is greater than previous digit
        current += i # Adds the current individual digit to substring
    else: # Used every loop to check if substring grew longer
        if len(current) > len(longest): # Condition to see if new substring longer than previous substring
            longest = current # Replaces the current substring with new longest substring
        current = i # Begins reading the string again from current character
if len(current) > len(longest): # Condition if current substring longer than previously found longest substring
    longest = current

print("Longest substring in numeric ascending order is:", longest) # Prints the longest found substring

# Finding the average of each digit in longest string
sum = 0 # Counter for the sum of longest substring

for i in longest: # Takes each individual digit in longest substring
    sum += int(i) # Adds up each individual digit

print("Average:", (sum / len(longest))) # Calculates the average by diving sum counter by how many individual digits in substring and prints it
'''

# Question 2
# This program will use a loop check to see if the contents of two text files are the same. If not, the loop will
# break and the first different lines of both files will be shown.
# Caution: All characters are included in text, so be be wary of added spaces/paragraphs and such in text files.
"""
first_file = input("First file name: ") # Prompt user for name of file
second_file = input("Second file name: ")

with open(first_file, "r") as file_1: # Opens the file input from user
    with open(second_file, "r") as file_2:
        while True: # Intended while loop for the readline function until a break condition
            lines_1 = file_1.readline() # Reads the line of file
            lines_2 = file_2.readline()
            if (lines_1 or lines_2) == '': # If readline reaches end of file condition to break loop
                print("Yes")
                break
            if lines_1 != lines_2: # If lines are not equal condition to break loop
                print("No")
                print(lines_1) # Print the current line that is in file
                print(lines_2)
                break"""

# Question 3
# This program will run a loop, until termination condition is found, to determine if a customer has exceeded the
# credit limit on a charge account. The customer will input the following facts:
# Account number
# Balance at the beginning of the month
# Total of all items charged by this customer this month
# Total of all credits applied to customer this month
# Allowed credit limit
# After, the new balance will be calculated by adding the charges and deducting any credits from the balance.
# If, the new balance exceeds the credit limit, the program will print
# their account number, credit limit and balance along with message of exceeded.
"""
while True: # Loop the program until break condition
    account_number = int(input("Enter account number (-1 to end): ")) # Prompts integer input from user
    if account_number == -1: # Condition to break loop
        break
    beginning_balance = float(input("Enter beginning balance: ")) # Prompts float input from user
    total_charges = float(input("Enter total charges: "))
    total_credits = float(input("Enter total credits: "))
    credit_limit = float(input("Enter credit limit: "))
    new_balance = beginning_balance + total_charges - total_credits # Simple calculation using user input to find new balance
    if new_balance > credit_limit: # Condition if new balance is greater than credit limit
        print("Account:", account_number) # Prints information from user input
        print("Credit Limit:", credit_limit)
        print("Balance:", new_balance)
        print("Credit Limit Exceeded.")"""

# Question 4
# This program will take a string from user to reverse the order and encrypt the string with the distance value.
# After which, it will prompt user again for string and distance value (be it the encrypted string) to reverse order and
# decryption of the string.

# Prompt user for encryption and distance value
encrypt = input("Enter phrase to Encrypt (lowercase, no spaces): ") # Prompts user for input
dis = int(input("Enter distance value: "))
code = "" # Counter used in program for new string built by ASCII values

# Reverse order and encryption of string
for char in encrypt[::-1]: # Takes string and turns into each iterable individual character in string and reverses it
    cipher_value = ord(char) + dis # Converts each individual character to ASCII value and adds the input distance to form cipher value variable
    if cipher_value > ord('z'): # Condition if the cipher value variable is greater than value of ASCII code for letter 'z'
        cipher_value = ord('a') + cipher_value - ord('z') - 1
    code += chr(cipher_value) # Puts each ASCII value together and converts it back to corresponding character
print("Result:", code) # Result

# Prompt user for decryption and distance value
decrypt = input("Enter phrase to Decrypt (lowercase, no spaces): ")
dis = int(input("Enter distance value: "))
code = ""

# Reverse order and decryption of string
for char in decrypt[::-1]:
    cipher_value = ord(char) - dis # Converts each individual character to ASCII value and subtracts the input distance to form cipher value variable
    if cipher_value < ord('a'): # Condition if the cipher value variable is less than value of ASCII code for letter 'a'
        cipher_value = ord('z') - ord('a') - cipher_value + 1
    code += chr(cipher_value)
print("Result:", code)

# Question 5
# This program will take a string from user to analyse and it will be accepted if it fulfills all of the conditions:
# String length 9
# 3 small alphabet (3 lowercase letter)
# 3 number (3 digit)
# 3 big alphabet (3 uppercase letters)
# 1st alphabet should be capital
# Last character should be a number
# Two consecutive alphabets cannot be lowercase letters
# If it does not fulfill all of the above conditions, the string will be rejected.

# Each condition has been broken down into a sub-function for easier readability and comprehension.
"""
# Prompt user for a string to analyse
def main():
    string = input("Enter a string to be analysed: ")  # Prompts user for string input
    if check_length(string) \
        and check_lowercase(string) \
        and check_digit(string) \
        and check_uppercase(string) \
        and check_first_letter_capital(string) \
        and check_last_character_number(string) \
        and not check_two_consecutive_small_letter(string): # If all these conditions are fulfilled
        print("Accept")
    else:  # If any of the conditions above not fulfilled
        print("Reject")


# Check if the length of string is 9
def check_length(string):
    return len(string) == 9  # True or false boolean if the string is 9 characters


# Check if 3 lowercase letters present
def check_lowercase(string):
    lower = 0  # Counter for lowercase letters
    for i in string:  # For loop breaks down the string input from user into its iterable individual character
        if i.islower():  # Condition if character is lowercase letter
            lower += 1  # Adds to counter for lowercase letters
    if lower == 3:  # Condition if lowercase letter counter is three
        return True  # Return True value to function
    return False  # Return False value to function


# Check if 3 digits present
def check_digit(string):
    digit = 0  # Counter for digits
    for i in string:
        if i.isdigit():  # Condition if character is digit
            digit += 1  # Adds to counter for digits
    if digit == 3:  # Condition if digit counter is three
        return True
    return False


# Check if 3 uppercase letters present
def check_uppercase(string):
    upper = 0  # Counter for uppercase letters
    for i in string:
        if i.isupper():  # Condition if character is uppercase letter
            upper += 1  # Adds to counter for uppercase letters
    if upper == 3:  # Condition if uppercase letter counter is three
        return True
    return False


# Check if first letter is capital
def check_first_letter_capital(string):
    for i in string:
        if i.isalpha():  # Condition if character is a letter in alphabet
            if i.isupper():  # Condition if the letter is uppercase
                return True
            if i.islower():  # Condition if the letter is lowercase
                return False


# Check if last character is digit
def check_last_character_number(string):
    return string[-1].isdigit()  # True or false boolean if last character is digit


# Check if two consecutive lowercase letters present
def check_two_consecutive_small_letter(string):
    for i in range(len(string) - 1):  # Takes each individual character in string and assigns a number value to it
        if string[i].islower() and string[
            i + 1].islower():  # Condition if a character and the next character after it are both lowercase letters
            return True
    return False


main()"""  # Main Function
