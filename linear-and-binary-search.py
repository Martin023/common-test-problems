# def linear_search(list, target):
#     '''
#     Returns the index position of the target if found, else return None
#     '''
#     for item in range(0,len(list)):
#         # len() is a built in func with constant time
#         if list[item] == target:

#             return item
#     return None

# print(linear_search([1,2,3,4,5,7],4))



def binary_search(list, target):
    '''
    Input should be sorted for bin to work
    '''
    first =0
    last = len(list)-1

    while first <= last:
        midpoint = (first+last)//2

        if list[midpoint]==target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint +1 
        else:
            last = midpoint-1

    return None

