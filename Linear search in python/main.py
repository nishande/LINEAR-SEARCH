# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
"""
Input : arr[] = {10, 20, 80, 30, 60, 50,
                     110, 100, 130, 170}
          x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50,
                     110, 100, 130, 170}
           x = 175;
Output : -1
Element x is not present in arr[].
"""
# code

def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1


arr = [ 2, 3, 4, 10, 40 ]
x = 10
n = len(arr)
result = search(arr, n, x)
if(result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)