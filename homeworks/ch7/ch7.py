
import numpy
import time


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
def g(a,b):
    if a<=0 or b<=0:
        return 1
    return g(a-2,b+1) + g(a+1,b-2) + g(a-1,b-1)

@Memoized
def z(t):
    if t <=2:
        return 1
    return 1.2*z(t-1)+0.2*z(t-2)+z(t-3)

missoula_population = 69000
t = 1
full_zombie = False
while full_zombie == False:
    if z(t) >= missoula_population:
        print ("days: ", t, " Pop: ", z(t), " Prev: ", z(t-1))
        full_zombie = True
    t += 1


# Fibonacci characteristic matrix:
A=numpy.matrix([[1,1,1],[1,1,0],[1,0,0]])

# Eigenvalues
lambda1, lambda2, lambda3 = numpy.linalg.eigvals(A)
# Solve for coefficeints d1,d2:
# z(t) = d1*lambda1**(t-1) + d2*lambda2**(t-1):
# <--> M*[[d1],[d2]] = [1,1]
M=numpy.matrix([[lambda1**-1,lambda2**-1,lambda3**-1],
                [lambda1**0,lambda2**0,lambda3**0],
                [lambda1**1,lambda2**1,lambda3**1]])
d = numpy.linalg.solve(M, [[1],[1],[1]])
d1,d2,d3 = d.T[0]

print(d1, " ")


def zz(t):
    return d1*lambda1**(t-1) + d2*lambda2**(t-1)

for t in range(10):
    print (zz(t))
