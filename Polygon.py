#Author : Lakshya A Agrawal

'''
This module defines a class Polygon which represents a Polygon object by its vertices. It has 2 constructors, one of which can be used to define a polygon by giving the coordinates of its vertices. In the other, the polygon can be constructed representing a circle.

It can perform the 3 basic transformations, namely, Scaling, Rotation and Translation. And given the reference to a matplotlib.pyplot object, t can plot the polygon onto it.
'''

from math import cos
from math import sin
from math import pi
from matrix_multiply import matrix_multiply
from math import inf

def dist(p1, p2):
    return(((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5)

class Polygon(object):
    
    # Constructur for Polygon
    def __init__(self, x_list, y_list, radius="A"):
        '''
        usage:
            Polygon(x_list, y_list)
            By calling the constructor this way, a polygon is constructed whose vertices are given as pairs of elemts from x_list and corresponding elements from y_list.
            
            Polygon(center_x, center_y, radius)
            By calling the constructor this way, A Circle in the form of Polygon is stored, defined by the coordinates of center of circle and the radius of circle.
        '''
        self.max_x=0
        self.max_y=0
        if radius=="A":
            self.type=True #True implies Polygon, False implies ellipse
            self.coordinates={"x":x_list+[x_list[0]], "y":y_list+[y_list[0]]}
            for i in range(len(x_list)):
                if abs(x_list[i])>self.max_x:
                    self.max_x=abs(x_list[i])
                if abs(y_list[i])>self.max_y:
                    self.max_y=abs(y_list[i])
        else:
            cx=x_list
            cy=y_list
            self.special_points={"P":[cx+radius*cos(0),cy+radius*sin(0)], "Q":[cx+radius*cos(pi/2),cy+radius*sin(pi/2)], "C":[cx, cy]}
            self.type=False # False implies ellipse
            x_list=[]
            y_list=[]
            linewidth=1
            d_theta=1/100
            theta=0
            while not (theta>=(2*pi)):
                nx=cx+radius*cos(theta)
                ny=cy+radius*sin(theta)
                if abs(nx)>self.max_x:
                    self.max_x=abs(nx)
                if abs(ny)>self.max_y:
                    self.max_y=abs(ny)
                x_list.append(nx)
                y_list.append(ny)
                theta=theta+d_theta
            x_list.append(cx+radius)
            y_list.append(cy)
            self.coordinates={"x":x_list, "y":y_list}


    def type(self):
        '''
            Returns the type of object represented
        '''
        if self.type:
            return("Polygon")
        else:
            return("Ellipse")

    def plot(self, plt):
        '''
        usage
        Polygon.plot(plt)
        
        here plt is the reference to a matplotlib.pyplot object. The function plots the object represented in object into the plt keeping the origin centered in the screen
        '''
        t=1.1*max(self.max_x, self.max_y)
        
        #Set the axis scale on both in such a way so as to fully display the figure, keeping the origin at the center of the plot and scale of both the axes same.
        plt.axis([-t,t,-t,t])
        plt.plot(self.coordinates["x"], self.coordinates["y"])
        
    def print_attr(self):
        '''
        This function prints the attributes of the object it represents
        '''
        if self.type:
            print(str(self.coordinates["x"][:-1])[1:-1].replace(',', ''))
            print(str(self.coordinates["y"][:-1])[1:-1].replace(',', ''))
        else:
            maj=dist(self.special_points["C"], self.special_points["P"])
            min=dist(self.special_points["C"], self.special_points["Q"])
            if not maj==min:
                print(self.special_points["C"][0], self.special_points["C"][1], maj, min)
            else:
                print(self.special_points["C"][0], self.special_points["C"][1], maj)
    
    def transform(self, type, x, y="R"):
        '''
        Usage:
            Polygon.transform("R", theta)
            By calling this way, the object is rotated about the origin by the angle given by theta in degrees. Rotation is done anticlockwise.
            
            Polygon.transform("S", x_factor, y_factor)
            This scales the Object with respect to the standard axis given by the factors x_factor for x-axis and y_favctor for y-axis. Both accept floating point numbers
            
            Polygon.transform("T", x_add, y_add)
            This translates the object by x_add units in the x-axis direction and y_add units in the y-axis direction.
            
            All of the three transformations are performed as matrix multiplications in homogeneous coordinates in 2 dimensions represented as (n+1)-tuples.
        '''
        if y=="R":
            #Rotation
            transform_matrix=[[cos(x), -sin(x), 0], [sin(x), cos(x), 0], [0, 0, 1]]
        else:
            if type=="S":
                #Scaling
                transform_matrix=[[x, 0, 0], [0, y, 0], [0, 0, 1]]
            elif type=="T":
                #Transformation
                transform_matrix=[[1, 0, x], [0, 1, y], [0, 0, 1]]
        x_list=[]
        y_list=[]
        
        
        self.max_x=-inf
        self.max_y=-inf
        
        #perform transformation on eevery point in the polygon
        for i in range(len(self.coordinates["x"])):
            coord_matrix=[[self.coordinates["x"][i]], [self.coordinates["y"][i]], [1]]
            updated_coord_matrix=matrix_multiply(transform_matrix, coord_matrix)
            x_list.append(updated_coord_matrix[0][0])
            y_list.append(updated_coord_matrix[1][0])
            
            #Update the max values of x and y coordinates to display the polygon to be used for plotting.
            if abs(updated_coord_matrix[0][0])>self.max_x:
                    self.max_x=abs(updated_coord_matrix[0][0])
            if abs(updated_coord_matrix[1][0])>self.max_y:
                    self.max_y=abs(updated_coord_matrix[1][0])
        
        #For Circle type object, which is a special case of ellipse, three points, namely, the center, the major axis vertex and the minor axis vertex need to be calculated to keep track of the major axis and minor axis values between transformations
        if not self.type:
            coord_matrix=[[self.special_points["P"][0]], [self.special_points["P"][1]], [1]]
            updated_coord_matrix=matrix_multiply(transform_matrix, coord_matrix)
            self.special_points["P"]=[updated_coord_matrix[0][0], updated_coord_matrix[1][0]]
            
            coord_matrix=[[self.special_points["Q"][0]], [self.special_points["Q"][1]], [1]]
            updated_coord_matrix=matrix_multiply(transform_matrix, coord_matrix)
            self.special_points["Q"]=[updated_coord_matrix[0][0], updated_coord_matrix[1][0]]
            
            coord_matrix=[[self.special_points["C"][0]], [self.special_points["C"][1]], [1]]
            updated_coord_matrix=matrix_multiply(transform_matrix, coord_matrix)
            self.special_points["C"]=[updated_coord_matrix[0][0], updated_coord_matrix[1][0]]
        
        self.coordinates["x"]=x_list
        self.coordinates["y"]=y_list
