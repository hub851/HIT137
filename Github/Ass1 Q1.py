s =  input("Enter a long string of numbers: ")

number_string = ""
for num in s:
    if(num.isnumeric()):
        number_string = number_string + num
print("String of numbers is: ", number_string)

length = ""
current = ""

for number in s:
    if len(current) == 0 or number > current[-1]:
        current += number
    else:
        if len(current) > len(length):
            length = current
        current = number
if len(current) > len(length):
    length = current

sum = 0
for i in length:
    sum += int(i)

avg = int(number) / int(length)

print("Longest substring in numeric ascending order is: ", current)
print("Average: ", avg)
