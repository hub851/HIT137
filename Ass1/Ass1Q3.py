
a=b=True # loop for readline function to continue until break
first=open(input(print("Enter first file name: " )))
second=open(input(print("Enter second file name: " ))) #opens both files, requries input from users
while a or b: #concurently reads lines of file a or b to identify if their lines are different
     a=first.readline()
     b=second.readline()
     if a!=b: #if files are different
          print('Files are different')
          break
else: #concurently reads lines of file a or b to identify if their lines are teh same
     print('Files are the same')
first.close()
second.close() #closes both files
