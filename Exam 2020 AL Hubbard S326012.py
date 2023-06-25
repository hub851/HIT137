"""
QU1
Assume Str is a String.
Create your own string (Str), where "length" of the string should be 18.
(The string should be in the form of Str = "ui683ji095ytrd79687df675")
Write a program to print the substring of numbers (n). After printing the subst
ring (n), "sort" them in descending order (d). Then subtract (d-s).
Example:
If Str = qwe598jhk90
substring (n)= 59890
descending order (d)=99850
subtract (d-n)=99850-59890=39960
"""
s = 'ui683ji095ytrd79687df675'
x=int(s.translate({ord(i): None for i in
'ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'}))
print ("substring (n)=", x)
descending = "".join(sorted(str(x), reverse=True))
print("descending order (d)= ", descending)
y=int(descending)
z=y-x
print("subtract (d-n)= ",z)


"""
Question 2
Encrypted Message = »äßÓÚÙ
Decrypted Message = Python
(Use "Unicode Table" from "https://cdn.img.onl/thomasorlita.cz/projects/unicode
-table.jpg")or given below.
Write a program to showcase the "formula" used for encryption and decryption.
"""
#couln't find the appropriate protocol for using UNICODE in python.


"""
Question 3
Write your initials (First characters of your Name) using turtle graphics.
"""
import turtle

turtle.color('black')
style = ('times new roman', 30)
turtle.write('AH', font=style, align='center')
turtle.hideturtle()


"""
Question 4
Write a program to create an empty "new file.txt" and store it on the same
folder as your python file.
Ask the user to input the "name of file".
Ask the user to input some content into the file and "print the input after
writing in the file". (Content should only have Upper Case letters)
Finally, replace the content in the file with "unused alphabets (A-Z)" and
write into the file.
Example: If content in the file is "HELLO".
 Replace it with "ABCDFGIJKMNPQRSTUVWXYZ"
"""

filename = input("filename: ")
with open(filename, "w+") as f:
  f.write(input("Enter text in UPPER case ONLY: "))
#file_contents = f.read()
with open(filename, "r") as file:
    print(file.read())


text = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
print(filename.replace(text, ""))

"""
Question 5
Using Object Oriented Programming create a program that consists of 'Band', 'Al
bum', 'Song', 'Genre'. You can create '4 separate classes' (or 'subclasses'). P
rogram should follow the questions (a, b, c, d) below. Create at least 3 entrie
s
a. Ask user to input a 'Song'. The output should be 'Band', 'Album' and 'Genre'
.
b. Create a method, so that a new song can be added to the 'Album'. (Hint: Use
List[]).
c. Add a new 'Song' to the 'Album'.
d. Ask user to input a 'Album'. The output should be the updated 'Album'.
"""
class album(object):
    def __init__(self, Band, Album, Song, Genre):
        self.Band = Band
        self.Album = Album
        self.Song = Song
        self.Genre = Genre

    def create_from_rawinput():
        return album(
        input("Song: "),
        input("Album: "),
        input("Band: "),
        input("Genre: "),
        )

new_song = album.create_from_rawinput()
x=input("Enter a song title: ")
song_detail = album(x)
list = []
list.append(new_song)
for obj in list:
    print( obj.Song, obj.Album, obj.Band, obj.Genre, sep =' ' )
