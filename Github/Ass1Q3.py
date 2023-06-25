
a=b=True
first=open(input(print("Enter first file name: " )))
second=open(input(print("Enter second file name: " )))
while a or b:
     a=first.readline()
     b=second.readline()
     if a!=b:
          print('Files are different')
          break
else:
     print('Files are the same')
first.close()
second.close()
