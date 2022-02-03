from pkggraphics.cirfunction import *
from pkggraphics.recfunction import *
from pkggraphics.sphearfunction import *
choice=input("enter your choice")
l=int(input("enter length"))
b=int(input("enter breadth"))
print("area of rectangle",rectarea(l,b))
print("perimeter of rectangle",rectperimeter(l,b))
r=int(input("enter radius"))
print("area of circle",cirarea(r))
print("perimeter of circle",cirperimeter(r))
r=int(input("enter radius of sphere"))
print("area of sphere",spharea(r))
print("perimeter of sphere",sphperimeter(r))
