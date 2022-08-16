# In this kata you will create a function that takes a list of non-negative integers and 
# strings and returns a new list with the strings filtered out.

# Example
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# ############NB
# isinstance method is used tocheck for every var type in python 
# eg.
# isinstance(1,int)
# isinstance(1,(int,float))
# isinstance(1,str))
# # where 1 is the var and int,float,str are the types of var
# ############NB

def filter_list(l):
    'return a new list with the strings filtered out'
    m = []
    for i in l:
        if isinstance(i, int):
            m.append(i)
            
    return m