# Binary search - Search a sorted array by repeatedly dividing the 
# search interval in half.
# Time complexity - O(logn)

# 1. Recursive Binary Search
def binary_search(arr, left, right, num):

    # Check base case
    if right >= left:

        mid = int(left + (right - left)/2)

        # If element is present at the middle itself
        if arr[mid] == num:
            return mid

        # If element is smaller than mid, then it can only
        # be presennt in left subarray
        elif arr[mid] > num:
            return binary_search(arr, left, mid - 1, num)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, right, num)

    else:
        # Element is not present in the array
        return -1

# Test array
arr1 = [2, 3, 4, 10, 40]
x1 = 10

# Function call
result = binary_search(arr1, 0, len(arr1) - 1, x1)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")
