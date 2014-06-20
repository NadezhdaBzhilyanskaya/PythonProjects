'''
Created on Jun 17, 2014

@author: Dulia
'''
import unittest

from Bzhilyanskaya_Nadja_Qudratic import Qudratic

class TestQudratic(unittest.TestCase):
    
    
    #search for Set up in test units
    
    def testGetDiscriminant(self):
        qud = Qudratic(1,2,3)
        qud2 = Qudratic(1,2,1)
        qud3 = Qudratic(1,-3,2)
        result = qud.getDiscriminant()
        result2 = qud2.getDiscriminant()
        result3 = qud3.getDiscriminant()
        
        self.assertEqual(result, -8, "Error finding Discriminant less than 0")
        self.assertEqual(result2, 0, "Error finding Discriminant equal to 0")
        self.assertEqual(result3, 1, "Error finding Discriminant more than 0")
        
    
    def testGetNumberOfRoots(self):
        qud = Qudratic(1,2,3)
        qud2 = Qudratic(1,2,1)
        qud3 = Qudratic(1,-3,2)
        result = qud.getNumberOfRoots()
        result2 = qud2.getNumberOfRoots()
        result3 = qud3.getNumberOfRoots()
        
        self.assertEqual(result, 0, "Error finding 0 roots")
        self.assertEqual(result2, 1, "Error finding 1 root")
        self.assertEqual(result3, 2, "Error finding 2 roots")

    def testIsRealRoot(self):
        qud = Qudratic(1,2,3)
        qud2 = Qudratic(1,2,1)
        qud3 = Qudratic(1,-3,2)
        result = qud.isRealRoot()
        result2 = qud2.isRealRoot()
        result3 = qud3.isRealRoot()
        
        self.assertFalse(result, "Error false positive for real root")
        self.assertTrue(result2, "Error false negative for 1 real root")
        self.assertTrue(result3, "Error false negative for 2 real root")


    def testGetRoot1(self) :      #num is number of roots
        qud = Qudratic(1,2,3)
        qud2 = Qudratic(1,2,1)
        qud3 = Qudratic(1,-3,2)
        result = qud.getRoot1()
        result2 = qud2.getRoot1()
        result3 = qud3.getRoot1()
        
        self.assertEqual(result, None, "Error finding root1 with 0 roots")
        self.assertEqual(result2, -1, "Error finding root1 with 1 root")
        self.assertEqual(result3, 2, "Error finding root1 with 2 roots")

    def testGetRoot2(self) :
        qud = Qudratic(1,2,3)
        qud2 = Qudratic(1,2,1)
        qud3 = Qudratic(1,-3,2)
        result = qud.getRoot2()
        result2 = qud2.getRoot2()
        result3 = qud3.getRoot2()
        
        self.assertEqual(result, None, "Error finding root2 with 0 roots")
        self.assertEqual(result2, None, "Error finding root2 with 1 root")
        self.assertEqual(result3, 1, "Error finding root2 with 2 roots")



    