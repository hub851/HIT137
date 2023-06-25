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

print("Longest substring in numeric ascending order is: ", current) #prints results of above calculations
print("Average: ", avg)
