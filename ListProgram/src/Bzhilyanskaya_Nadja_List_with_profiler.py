import cProfile
import re
cProfile.run('re.compile("foo|bar")')


def insert_at_0(list,a):   
    """Inserts variable at the beginning of the list"""
    list.insert(0, a)
    
def insert_at_end(list,a):   
    """Inserts variable at the end of the list"""
    list.append(a)
    
def insert_in_middle(list,a):   
    """Inserts variable in the middle of the list"""
    list.insert((int)(len(list)/2), a)

if __name__ == "__main__":   
    print("Welcome to the list Program")
    print("\n")

    list1 = []
    list2 = []
    list3 = []
    
    for x in range(0, 10000):
        list1.append(str(x))
        list2.append(str(x))
        list3.append(str(x))
    
    insert_at_0(list1,str(38574))
    insert_at_end(list2,str(38574))
    insert_in_middle(list3,str(38574))
    
    print("Done")
    

    

