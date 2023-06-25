s =  input("Enter a long string of numbers: ")

number_string = ""
for num in s:
    if(num.isnumeric()):
        number_string = number_string + num
print("String of numbers is: ", number_string)

max_digit = ""
max_length = 0
max_number = 0

cur_max_digit = ""
cur_max_length = 0
total_number = 0

ini_number = 0
for cur_number in number_string:
    if int(ini_number) < int(cur_number):
        ini_number = cur_number
        cur_max_digit = cur_max_digit + cur_number
        cur_max_length = cur_max_length + 1
        total_number += int(cur_number)
    else:
        ini_number = cur_number
        cur_max_digit = cur_number
        cur_max_length = 1
        total_number = int(cur_number)

    if max_length < cur_max_length:
       max_digit = cur_max_digit
       max_length = cur_max_length
       max_number = total_number

avg = int(max_number) / int(max_length)

print("Longest substring in numeric ascending order is: ", max_digit)
print("Average: ", avg)
