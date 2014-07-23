'''
Created on Jul 14, 2014

@author: Dulia
'''

import numpy as np


def num_columns(m):
    dimensions = m.shape
    return dimensions.__getitem__(1)
    
    
def num_rows(m):
    return len(np.atleast_1d(m))

def product(m1,m2):
    answer = np.dot(m1,m2)
    return answer         
    

if __name__ == "__main__":
    print("\t\tWelcome to The matrix program\n")
    
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
                         [14, 15],])
    
    
    print("Matrix 1:")
    print("Rows: ", num_rows(matrix1))
    print("Columns: ", num_columns(matrix1))
    print(matrix1,"\n")
    print("Matrix 2:")
    print("Rows: ", num_rows(matrix2))
    print("Columns: ", num_columns(matrix2))
    print(matrix2,"\n\n")
    print("Product: \n",product(matrix1,matrix2))
    
   
   
    
    
