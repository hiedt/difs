"""
Given an array A and a number X. Find the pair of 2 elements Ai & Aj that their product Ai*Aj = X 

Example 1: 
- Input A: [5,6,4,2]
- Input X: 20
- Ouptut: [0, 2] as A[0] = 5, A[2] = 4 and A[0]*A[2]=20
"""

def multiply_2elements(array, product):
    pair_index = {}
    results = []
    # Create a dictionary to store pairs' indices
    for index, element in enumerate(array):
        if (product % element==0):
            pairer = int(product/element)
            pair_index[pairer] = index
        else:
            pass

    # print(pair_index)

    # Find the pairs
    for index, element in enumerate(array):
        if element in (pair_index.keys()):
            results.append((index, pair_index[element]))

    return results

    
if __name__ == '__main__':
    print(multiply_2elements([5,6,4,2,3,10], 20))
