"""
Given an array. Calculate a new array with the same length, its i-th element = multiplication of all other elements

Example 1:
- Input: [1, 2, 3]
- Output: [6, 3, 2]

Example 2:
- Input: [3,2,4,1]
- Ouptut: [8, 12, 6, 24]
"""

def multiply_other_elements(array):
    l = len(array)
    left = [1]*l 
    right = [1]*l
    result = [1]*l
    # Calculate the multiplication of all elements to the left of the current i-th position
    for i in range(l):
        if i == 0:
            pass
        else:
            left[i] = left[i-1]*array[i-1]

    # Calculate the multiplication of all elements to the right of the current i-th position
    for j in reversed(range(l)):
        if j == l-1:
            pass
        else:
            right[j] = right[j+1]*array[j+1]

    # Final results[i] = left[i]*right[i]
    for k in range(l):
        result[k] = left[k]*right[k]

    return result


if __name__ == '__main__':
    result = multiply_other_elements([3,2,1,5])
    print(result)

