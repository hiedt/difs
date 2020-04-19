def factorial(x):
    if x == 0 or x ==1:
        return 1
    return x*factorial(x-1)
# Another traditional way
def facorial_old(x):
    result = 1
    while(x>0):
        result = result*x
        x -= 1
    return result
