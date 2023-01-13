from functools import reduce

n = 20

fibonacci = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0,1])

print(fibonacci)

"""
We use the reduce() function with three arguments that correspond to reduce(function, iterable, initializer) to consecutively add the new Fibonacci number to an aggregator object that incorporates one value at a time from the iterable object as specified by the function.
Here,  a simple list is used as the aggregator object with the two initial Fibonacci numbers [0, 1]. The aggregator object is handed as the first argument to the function, here x.
The second argument is the next element from the iterable. We  initialized the iterable with (n-2) dummy values in order to force the reduce() function to execute function (n-2) times 
We use the throwaway parameter _ to indicate that we are not interested in the dummy values of the iterable. Instead, we simply append the new Fibonacci number to the aggregator list x, calculated as the sum of the pre-vious two Fibonacci numbers.
"""

fib = lambda n:reduce(lambda x,n:[x[1],x[0]+x[1]], range(n),[0,1])[0]
print(fib)


import numpy

def mm_fib(n):
    return (numpy.matrix([[2,1],[1,1]])**(n//2))[0,(n+1)%2]

list = [mm_fib(i) for i in range(10)]
print(list)

x = (lambda i, x=[0,1]: [(x.append(x[y+1]+x[y]), x[y+1]+x[y])[1] for y in range(i)])(100)


