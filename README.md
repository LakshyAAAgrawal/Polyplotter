# Polyplotter
A program to visualize polygons, circles and ellipses and applying various geometrical transformations to them
To run as a program:
run main.py
```
python3 main.py
```
Usage:
>
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
  
  
 Alternatively, it could be used as a library by importing Polygon.py :
 ```python3
 from Polygon import Polygon
 ```
 It has the following definition:
 >
 
    This module defines a class Polygon which represents a Polygon object by its vertices. 
    It has 2 constructors, one of which can be used to define a polygon by giving the coordinates of its vertices. 
    In the other, the polygon can be constructed representing a circle.
    It can perform the 3 basic transformations, namely, Scaling, Rotation and Translation. 
    And given the reference to a matplotlib.pyplot object, it can plot the polygon onto it.


Usage:
>
         Polygon(x_list, y_list)
         By calling the constructor this way, 
         a polygon is constructed whose vertices are given as pairs of elemts from x_list and corresponding elements from y_list.
            
         Polygon(center_x, center_y, radius)
         By calling the constructor this way, 
         A Circle in the form of Polygon is stored, defined by the coordinates of center of circle and the radius of circle.

Method Definitions:
>      
        transform(type, x, y)
            Polygon.transform("R", theta)
            By calling this way, the object is rotated about the origin by the angle given by theta in degrees. 
            Rotation is done anticlockwise.
            
            Polygon.transform("S", x_factor, y_factor)
            This scales the Object with respect to the standard axis given by the factors x_factor for x-axis and y_favctor for y-axis. 
            Both accept floating point numbers
            
            Polygon.transform("T", x_add, y_add)
            This translates the object by x_add units in the x-axis direction and y_add units in the y-axis direction.
            
            All of the three transformations are performed as matrix multiplications in homogeneous coordinates in 2 dimensions represented as (n+1)-tuples.
>
        Polygon.plot(plt)
          here plt is the reference to a matplotlib.pyplot object. 
          The function plots the object represented in object into the plt keeping the origin centered in the screen
