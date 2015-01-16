import cProfile
import math
import numpy as np


def get_angle_numpy_run(v1,v2):   
    """Run get angle with numpy 100000 times"""
    for x in range(0, 100000):    
        get_angle_math(v1,v2)
    
def get_angle_math_run(v1,v2):   
    """Run get angle with math 100000 times"""
    for x in range(0, 100000):
        get_angle_math(v1,v2)
        
def get_angle_numpy(v1,v2):   
    """Run get angle with numpy"""
    x = np.dot(v1[0], v2[0]) / v1[1] / v2[1]
    x = min(1, x)
    x = max(-1, x)
    angle = np.arccos(x) * 180. / math.pi
    return angle
        
    
def get_angle_math(v1,v2):   
    """Run get angle with math"""
    x = np.dot(v1[0], v2[0]) / v1[1] / v2[1]
    x = min(1, x)
    x = max(-1, x)
    angle = math.acos(x) * 180. / math.pi
    return angle
        
 

def main():   
    """Initiates program"""
    print("Welcome to the Vector method comparison Program")
    print("\n")
    
    vector1 = np.array([1,2])
    vector2 = np.array([5,6])
    
    get_angle_numpy_run(vector1,vector2)
    get_angle_math_run(vector1,vector2)

if __name__ == "__main__":   
   
    cProfile.run('main()')
    print("Done")
    

    

