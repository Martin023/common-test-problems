def linear_search(list, target):
    '''
    Returns the index position of the target if found, else return None
    '''
    for item in range(0,len(list)):
        # len() is a built in func with constant time
        if list[item] == target:

            return item
    return None

print(linear_search([1,2,3,4,5,7],4))