import cProfile
import time

def insert_at_0(list,a):   
    """Inserts variable at the beginning of the list"""
    list.insert(0, a)
    
def insert_at_end(list,a):   
    """Inserts variable at the end of the list"""
    list.append(a)
    
def insert_in_middle(list,a):   
    """Inserts variable in the middle of the list"""
    list.insert((int)(len(list)/2), a)
    
def sleep():
    """SLeeps for 1 unit"""
    time.sleep(1)

def main():   
    """Initiates program"""
    print("Welcome to the list Program")
    print("\n")
    
    list = []
    
    for x in range(0, 5000000):
        list.append(str(x))
    
    insert_at_0(list,str(38574))
    insert_at_end(list,str(38574))
    insert_in_middle(list,str(38574))
    sleep()
    
    

if __name__ == "__main__":   
   
    cProfile.run('main()')
    print("Done")
    

    

