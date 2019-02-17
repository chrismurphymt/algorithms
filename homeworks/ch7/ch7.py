
import numpy
import time
# Fibonacci characteristic matrix:
A=numpy.matrix([[1,1],[1,0]])
# Eigenvalues

lambda1, lambda2 = numpy.linalg.eigvals(A)
# Solve for coefficeints d1,d2:
# z(t) = d1*lambda1**(t-1) + d2*lambda2**(t-1):
# <--> M*[[d1],[d2]] = [1,1]
M=numpy.matrix([[lambda1**-1,lambda2**-1],[lambda1**0,lambda2**0]])
d = numpy.linalg.solve(M, [[1],[1]])
d1,d2 = d.T[0]
def z(t):
    return d1*lambda1**(t-1) + d2*lambda2**(t-1)

for t in range(10):
    print(z(t))


# class used as function "decorator":
class Memoized:
    def __init__(self, function):
        self._function = function
        self._cache = {}
    def __call__(self, *args):
        if args not in self._cache:
        # not in the cache: call the function and store the result in
        # the cache
            self._cache[args] = self._function(*args)
        # the result must now be in the cache:
        return self._cache[args]


@Memoized
def fib_memoized(n):
    if n==0 or n==1:
        return 1
    return fib(n-1) + fib(n-2)

def fib(n):
    if n==0 or n==1:
        return 1
    return fib(n-1) + fib(n-2)

numFib = 20
t1 = time.time()
print("im those ", fib(numFib))
t2 = time.time()
print("taken: ", t2-t1)
t2=time.time()
print("im moemo ", fib_memoized(numFib))
t1 = time.time()
print("taken memo: ", t1-t2)
