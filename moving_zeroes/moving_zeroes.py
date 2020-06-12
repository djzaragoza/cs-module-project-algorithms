'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # Objective --
    # shift zeroes left of the array then return the altered array
    # if no zeroes, print array as is

    moved = 0

    for x in range(len(arr)):
        if arr[x] != 0 and arr[moved] == 0:
            arr[x], arr[moved] = arr[moved], arr[x]
        if arr[moved] != 0:
            moved += 1
    return arr

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
