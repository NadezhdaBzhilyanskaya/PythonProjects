'''
Created on Jul 14, 2014

@author: Dulia
'''

import numpy as np
import math

def calculate_dotproduct_vector(v1,v2):   
    """Calculates the dotproduct of 2 vectors given as v1 and v2"""
    dotproduct = 0
    for a, b in zip(v1, v2):
        dotproduct = dotproduct + (a*b)
    return dotproduct
    
def length(v):
    """Calculates length of given vector"""  
    length = math.sqrt(calculate_dotproduct_vector(v, v))
    return length
    
def get_number_of_Dimensions(v):
    """Returns number of dimensions of given vector"""
    return len(np.atleast_1d(v))

def calculate_angle_vector(v1,v2):   
    """Calculates the angle between 2 vectors given as v1 and v2 in radians"""
    dotproduct = calculate_dotproduct_vector(v1,v2)
    print("1.   ", dotproduct)
    lengths = length(v1) * length(v2)
    print("2.   ", lengths)
    
    angle = math.acos(dotproduct / lengths)
    return angle

def radians_to_degrees(r):
    return (r*(180/math.pi))

if __name__ == "__main__":
    print("\t\tWelcome to The vector program\n")
    
    vector1 = np.array([1,2])
    vector2 = np.array([5,6])
    
    print("Vector 1: ")
    print("Dimensions: ",get_number_of_Dimensions(vector1))
    print("Length: ", length(vector1),"\n")
    print("Vector 2: ")
    print("Dimensions: ",get_number_of_Dimensions(vector2))
    print("Length: ", length(vector2),"\n")
    print("Dotproduct: ", calculate_dotproduct_vector(vector1,vector2))
    angle = calculate_angle_vector(vector1,vector2)
    print("Angle (in radians): ", angle)
    print("Angle (in degrees): ", radians_to_degrees(angle))
    
   
    
    
