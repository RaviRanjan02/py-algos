def binary_search(arr, left, right, num):
    while left <= right:
        mid = int(left + (right - 1)/2)

        # Check if num is present at mid
        if arr[mid] == num:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < num:
            left = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1

# Test array
arr = [2, 3, 4, 10, 40]
num = 10

# Function call
result = binary_search(arr, 0, len(arr) - 1, num)

if result != -1:
    print("Element is present at {}".format(result))
else:
    print("Element is not present in array")