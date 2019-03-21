# Author : Lakshya A Agrawal

'''
    This is a wrapper program for the Polygon class, which initiates a Polygon object, and gives an interace to visualize the transformations by issuing commands.
    
    Usage:
        after running the program, type the type of object to be created
            polygon
            for polygon of n vertices
            the next 2 lines contain space separated list of x and y coordinates of the vertices respectively.
            
            disc
            for circle
            the next line contains space separated circle attributes:
                center_x center_y radius
        
        After this, enter any of the following commands in any order any number of times:
            S x y
            This Scales the object about the x-axis by x and y-axis by y
            
            T x y
            This translates the object by x units in the x-direction and y units in the y-direction
            
            R θ
            This rotates the entire figure by θ in anti clockwise direction about the origin.
        After each command, the attributed of the transformed object are printed:
            polygon:
                list of x coordinates
                list of y coordinates
            disc:
                center_x center_y major_axis minor_axis
        
        To exit the program, type 'quit' and enter
        
'''
import matplotlib.pyplot as plt
from Polygon import Polygon
from math import pi
plt.ion()
plt.axis("equal")
type=input()
Poly=None
if type=="polygon":
    x_list=list(map(float, input().split()))
    y_list=list(map(float, input().split()))
    Poly=Polygon(x_list, y_list)
elif type=="disc":
    cx, cy, r=map(float, input().split())
    Poly=Polygon(cx, cy, r)
else:
    raise("Not Valid Type")
Poly.plot(plt)
c=input()
while not c=="quit":
    l=c.split()
    if l[0]=="R":
        try:
            theta=(float(l[1])/360)*2*pi
        except:
            print("Invalid Input, enter again")
            c=input()
            continue
        Poly.transform("R", theta)
    elif l[0]=="S" or l[0]=="T":
        try:
            cx=float(l[1])
            cy=float(l[2])
        except:
            print("Invalid Input, enter again")
            c=input()
            continue
        Poly.transform(l[0], cx, cy)
    plt.cla()
    Poly.plot(plt)
    Poly.print_attr()
    c=input()
