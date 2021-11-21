import numpy as np
from numpy import random

eps = 1e-7
dim = 10
k = 5000
v = 9

def normalize(a):
    return np.amax(np.absolute(a))

def make_matrix(dim): 
    A = np.zeros((dim, dim));
    for i in range(dim):
        for j in range(i+1,dim):
            A[i][j] = A[j][i] = random.uniform(-100, 100)

    sum = np.sum(np.absolute(A), axis=1)
    for i in range(dim):
        A[i][i] = random.uniform(sum[i] + v, sum[i] + 10*v)   
    
    return A

#Successive over-relaxation method
def SOR(A, f, x0, w0, x_solve):
    q = 0
    while(True):    
        q += 1  
        x = np.copy(x0) 
        for i in range(dim):
            sum = 0
            for j in range(i):
                sum += A[i][j] * x0[j] / A[i][i]
            for j in range(i+1, dim):
                sum += A[i][j] * x0[j] / A[i][i]

            x0[i] = (1 - w0)*x0[i] - w0*sum +   w0 * f[i] / A[i][i]

        if normalize(x - x0) < eps:
            break
        if q > k:
            print-("iteration step greater then k_max = ", k)
            return None
    print("w=", w0, "   q=", q, "\t||Ax(q) - f||=", normalize(np.dot(A, x0) - f), "\t||x - x(q)||=",normalize(x_solve - x0))

#minimal residual method
def MRM(A, f, x0, x_solve):
    q = 0
    while True:
        q += 1
        rk = np.dot(A, x0) - f
        Ark = np.dot(A, rk)
        x = x0 - (np.dot(Ark, rk) / np.dot(Ark, Ark))*rk
        if normalize(x - x0) < eps:
            break
        if q > k:
            print-("iteration step greater then k_max = ", k)
            return None
        x0 = x
    
    print("q=", q,"\tx` = ",x, "\t||Ax` - f||=", normalize(np.dot(A, x) - f), "||x - x`|| = ", normalize(x_solve - x))



A = make_matrix(dim)
x = np.arange(1, dim+1, 1.)
f = np.dot(A, x)
w = np.array([0.2, 0.5, 0.8, 1., 1.3, 1.5, 1.8])
x0 = np.copy(f) 

print("----------------------------------------task----------------------------------------")
print("------------------------------------------------------------------------------------\n\n")
print("A =\n", A)
print("x =\t", x)
print("f =\t", f)
print("x0 =\t", x0)

    

print("----------------------------------------minimal residual method----------------------------------------")
MRM(A, f, x0, x)


print("\n\n-----------------------------------successive over-relaxation method-----------------------------------")
for i in w:
    SOR(A, f, np.copy(x0), i, x)



