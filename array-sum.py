def sum():
   arr = [1, 2, 3, 4, 5]
   sum1 = 0 
   
   for i in arr:
       sum1 += i
   print(sum1)
sum()   

# def sum(arr):
#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + sum(arr[1:])

# print(sum([1, 2, 3, 4, 5]))