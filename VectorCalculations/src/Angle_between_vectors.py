'''
Created on Jul 14, 2014

@author: Dulia
'''

import numpy as np
import math

def calculate_dotproduct(v1,v2):   
    """Calculates the dotproduct of 2 vectors given as v1 and v2"""
    try:
        return np.dot(v1,v2) 
    except ValueError:                  
        print("Vectors must have the same number of dimensions")
    
def length(v):
    """Calculates length of given vector"""  
    return np.linalg.norm(v)
    
def get_number_of_dimensions(v):
    """Returns number of dimensions of given vector"""
    return len(np.atleast_1d(v))

def calculate_angle(v1,v2):   
    """Calculates the angle between 2 vectors given as v1 and v2 in radians"""
    try:
        dotproduct = calculate_dotproduct(v1,v2)
        lengths = length(v1) * length(v2)
    
        angle = math.acos(dotproduct / lengths)
        return angle
    except TypeError:
        print("Vectors must have the same number of dimensions")

def radians_to_degrees(r):
    if(r == None):
        return None
    return (r*(180/math.pi))

if __name__ == "__main__":
    print("\t\tWelcome to The vector program\n")
    
    vector1 = np.array([1,2])
    vector2 = np.array([5,6])

    print("Vector 1: ")
    print("Dimensions: ",get_number_of_dimensions(vector1))
    print("Length: ", length(vector1),"\n")
    print("Vector 2: ")
    print("Dimensions: ",get_number_of_dimensions(vector2))
    print("Length: ", length(vector2),"\n")
    print("Dotproduct: ", calculate_dotproduct(vector1,vector2))
    angle = calculate_angle(vector1,vector2)
    print("Angle (in radians): ", angle)
    print("Angle (in degrees): ", radians_to_degrees(angle))
    
   
    
    
