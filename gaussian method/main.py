import numpy as np
from numpy import array

def make_matrix(n, m):
    return 200*np.random.rand(n, m) - 100

def max_ind(a, column):
    abs_a = np.absolute(a)
    c = abs_a.transpose()[column]
    return array(c).argmax()
    
def solve(a, b): # Ax = B
    n = a.shape[0]
    m = b.shape[1]
    
    if a.shape[0] != b.shape[0]:
        print("impossible to solve the equation")
        return None
    x = b * 0

    #straight run     
    for i in range(n):
        max_index = max_ind(a, i)
        a[[i,max_index]] = a[[max_index,i]]
        b[[i, max_index]] = b[[max_index, i]]

        b[i] = b[i] / a[i][i]
        a[i] = a[i] / a[i][i]   
        for j in range(i+1, n):
            b[j] = b[j] - b[i]*a[j][i]
            a[j] = a[j] - a[i]*a[j][i]
    
    #reverse run
    for i in range(m):
        for j in range(n-1,-1,-1):
            x[j][i] = b[j][i]
            for k in range(1, n-j):
                x[j][i] -= a[j][n-k] * x[n-k][i]
    
    return x

def reverse(a):
    if a.shape[0] != a.shape[1]:
        print("matrix is not square")
        return None
    n = a.shape[0]
    return solve(a, np.eye(n))


print("--------task #1--------")

n = 10

a = make_matrix(n,n)  
print("a = \n", a)

x = np.arange(1, n+1, 1.)
f = np.dot(a, x.reshape((n, 1)))
sx = solve(array(a), f).reshape((1,n))

print("x = (by definition) ", x)
print("x = ( after solve )", sx)
abs_x = np.absolute(x)
abs_sx = np.absolute(sx)

print("relative error = ", np.amax(abs_x - abs_sx) / np.amax(abs_x))


print("--------task #2--------")

rev_a = reverse(array(a))
print("matrix  a = \n", a)
print("reverse a = \n" ,rev_a)
print("a * reverse a = \n", np.dot(a, rev_a))

print("--------task #3--------")
k = 16
print("dim\trelative error")
for i in range(k+1, k + 102):
    a = make_matrix(i,i)
    x = np.arange(1, i+1, 1.)
    f = np.dot(a, x.reshape((i, 1)))
    sx = solve(array(a), f).reshape((1,i))
    abs_x = np.absolute(x)
    abs_sx = np.absolute(sx)
    print(i, "\t", np.amax(abs_x - abs_sx) / np.amax(abs_x) )