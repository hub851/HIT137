import turtle
from turtle import*
turtle.speed(5)

turtle.right (90)
turtle.fd (30) #length of stem
turtle.left (90) #orients leaf to right
turtle.fd (25) #branch to leaf
turtle.left (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (-80,90) #(length of leaf, distance around or extent)
turtle.right (90) #reorients to right
turtle.circle (-80,90)
turtle.end_fill ()
turtle.right (135) #return to horizontal stem
turtle.fd (60) #creates vein within the leaf
turtle.left (180) #orients to left
turtle.fd (85) #return to vertical stem
turtle.left (90) #oreints to bottom
turtle.fd (80) #draws stem, oreinted down, toward next leaf

#turtle.right (90)
#turtle.right (45)
turtle.fd (30)
turtle.left (90)
turtle.fd (25)
turtle.left (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (-80,90)
turtle.right (90)
turtle.circle (-80,90)
turtle.end_fill ()
turtle.right (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (85)
turtle.left (90)
turtle.fd (80)

turtle.right (135)
#turtle.right (45)
turtle.fillcolor ("green")
turtle.begin_fill ()
turtle.circle (80,90)
turtle.left (90)
turtle.circle (80,90)
turtle.end_fill ()
turtle.left (135)
turtle.fd (60)
turtle.left (180)
turtle.fd (60)
turtle.right (90)
turtle.circle (200,60)
turtle.done()
