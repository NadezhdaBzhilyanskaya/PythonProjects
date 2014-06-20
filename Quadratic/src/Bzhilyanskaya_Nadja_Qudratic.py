import math


class Qudratic:
    def __init__(self, a,b,c):   
        """Creates a qudratic using the formula: ax^2+bx+c=0"""
        self.a = a
        self.b = b 
        self.c = c
        self.d = (b**2)-(4*a*c)

    def __str__(self):
        a = str(self.a) + "x^2 + " + str(self.b) + "x + " + str(self.c)
        return a;

    def displayFormula(self):    
        """Prints out the formula of the qudratic"""               
        print (self)

    def getDiscriminant(self):    
        """Finds and returns the discriminant: b^2-4ac"""
        return self.d

    def getNumberOfRoots(self):
        """Determines how many roots the qudratic has using the discriminant"""
        if self.d > 0:
            return 2
        elif self.d < 0:
            return 0
        else:
            return 1

    def isRealRoot(self):
        """Determines if root/roots are real or imaginary"""

        if self.d < 0:
            return False
        else:
            return True


    def getRoot1(self) :      
        """Gets first root:
        If 2 real roots exists finds and returns the root in which the radical is subtracted.
        If 1 real root exists finds and returns that 1 root.
        If no real roots exist returns None"""
        a = self.a 
        b = self.b
        num = self.getNumberOfRoots()
        
        if num == 0 :
            return None
        elif num == 0 :
            answer= ((-1)*b) /(2*a)
        else :
            answer = ((-1)*b + math.sqrt(self.d))/(2*a)
            return answer

    def getRoot2(self) :
        """Gets second root:
        If 2 real roots exists finds and returns the root in which the radical is added.
        If 1 real root exists returns None.
        If no real roots exist returns None"""
        a = self.a 
        b = self.b
        num = self.getNumberOfRoots()
        
        if num < 2 :
            return None
        else :
            answer = ((-1)*b - math.sqrt(self.d))/(2*a)
            return answer
      

if __name__ == "__main__":   
    print("Welcome to the qudratic formula Program")
    print("         Formula: ax^2+bx+c=0")
    print("\n")

    aIN=int(input("Value for a: "))
    bIN=int(input("Value for b: "))
    cIN=int(input("Value for c: "))
    print("\n")

    qud1= Qudratic(aIN,bIN,cIN)
    print(qud1)
    d = qud1.getDiscriminant()
    num = qud1.getNumberOfRoots()
    print("\n")
    print("Discrimanent: ",d)
    print("\n")
    print("# of Roots: ",num)
    print("\n")
    print("Is root real: ",qud1.isRealRoot())
    print("\n")
    print("Root 1: ",qud1.getRoot1())
    print("\n")
    print("Root 2: ",qud1.getRoot2())

