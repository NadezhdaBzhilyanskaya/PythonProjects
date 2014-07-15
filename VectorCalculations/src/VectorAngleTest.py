'''
Created on Jun 17, 2014

@author: Dulia
'''
import unittest
import numpy as np
import Angle_between_vectors as abv

class TestQudratic(unittest.TestCase):
    
    
    
    def testDotproduct(self):
        vector1 = np.array([1,2,3])
        vector2 = np.array([4,-5,6])
        vector3 = np.array([-4,-9])
        vector4 = np.array([-1,2])
        result = abv.calculate_dotproduct(vector1,vector2)
        result2 = abv.calculate_dotproduct(vector3,vector4)
        
        self.assertEqual(result, 12, "Error finding dotproduct of 3d array")
        self.assertEqual(result2, -14, "Error finding dotproduct of 2d array")
        
    
    def testLength(self):
        vector1 = np.array([6,8])
        vector2 = np.array([1,2,3])
        result = abv.length(vector1)
        result2 = round(abv.length(vector2),2)
        
        self.assertEqual(result, 10, "Error finding length 2d array")
        self.assertEqual(result2, 3.74, "Error finding length 3d array")

    def testDimensions(self):
        vector1 = np.array([8])
        vector2 = np.array([1,2,3])
        vector3 = np.array([1,2,3,4,6,3,5,6,4,4])
        result = abv.get_number_of_Dimensions(vector1)
        result2 = abv.get_number_of_Dimensions(vector2)
        result3 = abv.get_number_of_Dimensions(vector3)
        
        self.assertEqual(result, 1, "Error finding dimensions 1d array")
        self.assertEqual(result2, 3, "Error finding dimensions 3d array")
        self.assertEqual(result3, 10, "Error finding dimensions 10d array")


    def testRadiansToDegrees(self) :      #num is number of roots
        result = round(abv.radians_to_degrees(1),1)
        result2 = round(abv.radians_to_degrees(54),2)
        result3 = round(abv.radians_to_degrees(-32),2)
        
        self.assertEqual(result, 57.3, "Error converting radians to degrees")
        self.assertEqual(result2, 3093.97, "Error converting radians to degrees")
        self.assertEqual(result3, -1833.46, "Error converting radians to degrees")

    def testAngle(self) :
        vector1 = np.array([1,2,3])
        vector2 = np.array([4,5,6])
        vector3 = np.array([3,5])
        vector4 = np.array([-2,3])
        result = round(abv.calculate_angle(vector1, vector2),3)
        result2 = round(abv.calculate_angle(vector3, vector4),2)
        
        self.assertEqual(result, 0.226, "Error finding angle between 2, 3d vectors")
        self.assertEqual(result2, 1.13, "Error finding angle between 2, 2d vectors")


    