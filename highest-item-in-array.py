# Complete the function to find the count of the most frequent item of an array. 
# You can assume that input is an array of integers. For an empty array return 0

# Example
# input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# ouptut: 5 

def most_frequent_item_count(collection):
    highest = 0
    for element in collection:
        if collection.count(element) >= highest:
            highest = collection.count(element)
    print(highest)
most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])
 

