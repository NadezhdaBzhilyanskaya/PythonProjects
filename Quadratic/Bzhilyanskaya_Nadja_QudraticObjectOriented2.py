import math

class Qudratic:
    def __init__(self, a,b,c):   #formula: ax^2+bx+c=0
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        a = str(self.a) + "x^2 + " + str(self.b) + "x + " + str(self.c)
        return a;

    def displayFormula(self):                    #find name of toString for python
        print (self.a,"x^2 +",self.b,"x +",self.c)

    def getDiscriminant(self):    #Discriminant: b^2+4ac
        a = self.a 
        b = self.b
        c = self.c
        
        d=(b**2)-(4*a*c)
        return d

    def getNumberOfRoots(self):
        if d > 0:
            return 2
        elif d < 0:
            return 0
        else:
            return 1

    def isRealRoot(self):
        d = self.getDiscriminant()
        
        if d < 0:
            return False
        else:
            return True


    def getRoot1(self) :      #num is number of roots
        a = self.a 
        b = self.b
        c = self.c
        num = self.getNumberOfRoots()
        
        if num == 0 :
            return None
        elif num == 0 :
            answer= ((-1)*b) /(2*a)
        else :
            answer = ((-1)*b + math.sqrt((b**2)-(4*a*c)))/(2*a)
            return answer

    def getRoot2(self) :
        a = self.a 
        b = self.b
        c = self.c
        num = self.getNumberOfRoots()
        
        if num < 2 :
            return None
        else :
            answer = ((-1)*b - math.sqrt((b**2)-(4*a*c)))/(2*a)
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

