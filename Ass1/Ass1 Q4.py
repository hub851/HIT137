encrypt = input("Enter text to encrypt (lowercase, no spaces only): ") #prompt for user input to encrypt
distance = int(input("Input distance value to use for encryption: ")) #prompt for user input for distance vaule for encryption
#print(encrypt) #TO BE DELETED
#print(distance)#TO BE DELETED
code = "" #counter to introduce ACSII value
#[::-1] #reverses string order
for ch in encrypt[::-1]: #reverses string order
    #ordvalue=ord(ch)
    #print(ordvalue)
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
    #ordvalue=ord(ch)
    ciphervalue=ord(ch)-distance #converts characters (after reversal) to ACSII values
    if ciphervalue<ord("a"): #if cipher value is less than a, encrypts that value
        #x=ord('a')-ciphervalue, coped to below line
        ciphervalue=ord('z')-ord('a')-ciphervalue+1
    code+=chr(ciphervalue)
print('decypted text is ', code)
