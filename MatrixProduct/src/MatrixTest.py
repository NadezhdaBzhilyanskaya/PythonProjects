'''
Created on Jun 17, 2014

@author: Dulia
'''
import unittest
import numpy as np
import Matrix_Calculations as mc

class TestQudratic(unittest.TestCase):
    
    
    def testRows(self):
        matrix1 = np.matrix([[1, 2, 3, 4], 
                             [5, 6, 4, 5]])
    
        matrix2 = np.matrix([[5, 6, 4], 
                             [7, 8, 8],
                             [4, 6, 3],
                             [7, 1, 0]])
        result = mc.num_rows(matrix1)
        result2 = mc.num_rows(matrix2)
        
        self.assertEqual(result, 2, "Error finding number of rows")
        self.assertEqual(result2, 4, "Error finding number of rows")
        
    
    def testColumns(self):
        matrix1 = np.matrix([[1, 2, 3, 4], 
                             [5, 6, 4, 5]])
    
        matrix2 = np.matrix([[5, 6, 4], 
                             [7, 8, 8],
                             [4, 6, 3],
                             [7, 1, 0]])
        result = mc.num_columns(matrix1)
        result2 = mc.num_columns(matrix2)
        
        self.assertEqual(result, 4, "Error finding number of columns")
        self.assertEqual(result2, 3, "Error finding number of columns")

    def testProduct(self):
        matrix1 = np.matrix([[1, 2, 3, 4], 
                             [5, 6, 4, 5]])
    
        matrix2 = np.matrix([[5, 6, 4], 
                             [7, 8, 8],
                             [4, 6, 3],
                             [7, 1, 0]])
        
        matrix3 = np.matrix([[1, 2, 3], 
                             [4, 5, 6],
                             [7, 8, 9]])
    
        matrix4 = np.matrix([[10, 11], 
                             [12, 13],
                             [14, 15]])
        
        answer12 = np.matrix([[59, 44, 29],
                              [118, 107, 80]])
    
        answer34 = np.matrix([[76, 82],
                              [184, 199],
                              [292, 316]])
        
        result = mc.product(matrix1, matrix2)
        result2 = mc.product(matrix3, matrix4)
        
        self.assertTrue(np.array_equal(result, answer12), "Error finding product")
        self.assertTrue(np.array_equal(result2, answer34), "Error finding product")
        