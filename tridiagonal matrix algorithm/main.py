import numpy as np
from colorama import init, Fore, Back, Style
from numpy.core.arrayprint import set_printoptions
from numpy.random.mtrand import random, uniform 

def make_array(n):
    return 200*np.random.rand(n) - 100

def stability_of_method(a, b, c):
    n = len(a)

    #Verification of stability conditions
    if c[0] == 0:
        return err("c[0] = 0")
    if c[n-1] == 0:
        return err("c[n] = 0")
    
    for i in range(n):
        if a[i] == 0:
            return err("a[",i,"] = 0")
            
        if b[i] == 0:
            return err("b[",i,"] = 0")


    if abs(c[0]) < abs(b[0]):
        return err("abs(c[0]) < abs(b[0])")
    if abs(c[n-1]) < abs(a[n-1]):
        return err("abs(c[n]) < abs(a[n])")

    for i in range(1,n-1):
        if abs(c[i]) < abs(a[i]) + abs(b[i]):
            return err("abs(c[i]) < abs(a[i]) + abs(b[i])")

    #At least one inequality is strictly
    if abs(c[0]) > abs(b[0]):
        print(Fore.GREEN + "The method is applicable and stable" + Fore.WHITE)
        return True
    if abs(c[n-1]) < abs(a[n-1]):
        print(Fore.GREEN + "The method is applicable and stable" + Fore.WHITE)
        return True
    for i in range(1,n):
        if abs(c[i]) > abs(a[i]) + abs(b[i]):
            print(Fore.GREEN + "The method is applicable and stable" + Fore.WHITE)
            return True

    return err("There is no strictly inequality")


def solve(a, b, c, f): #Ay = f, A = 3diag (-b, c, -a)
    n = len(a) - 1 
    alfa = np.arange(n)
    betta = np.arange(n+1)
    y = np.arange(n+1) * 1.

    alfa = np.append(None, alfa)
    betta = np.append(None, betta)

    alfa[1] = b[0]/c[0]
    betta[1] = f[0]/c[0]

    for i in range(1, n):
        alfa[i+1] = b[i] / (c[i] - a[i]* alfa[i])
        betta[i+1] = (f[i]+a[i]*betta[i])/(c[i]-a[i]*alfa[i])

    betta[n+1] = (f[n]+a[n]*betta[n])/(c[n]-a[n]*alfa[n])

    y[n] = betta[n+1]
    for i in range(n-1, -1, -1):
        y[i] = alfa[i+1]*y[i+1] + betta[i+1]

    return y

def err(e):
    print(Fore.RED + "Method is not stable: " + e + Fore.WHITE)
    return False


n = 3
k = 16

a = make_array(n)
a = np.append(None, a)
b = make_array(n)
b = np.append(b, None)
c = np.arange(n+1) * 1.0

y = np.arange(n+1) * 1.  + 1
f = np.arange(n+1) * 1.



for i in range(1,n):
    c[i] = abs(a[i]) + abs(b[i]) + uniform(k, 2*k)
    
    
c[0] = abs(b[0]) + uniform(k, 2*k)
c[n] = abs(a[n]) + uniform(k, 2*k)

for i in range(1,n):
    f[i] = -a[i]*y[i-1] + c[i]*y[i] - b[i]*y[i+1]

f[0] = c[0]*y[0] - b[0]*y[1]
f[n] = -a[n]*y[n-1] + c[n]*y[n]



print("---------------------------------------------------------------------------------------------------------------------")
print("b = ", b)
print("c = ", c)
print("a = ", a)
print("y = ", y)
print("f = ", f)
print("\n")


sy = solve(a,b,c,f)
stability_of_method(a, b, c)

set_printoptions(precision=20)
print("y = ",sy, "\n")
print("relative error = ", np.amax(np.absolute(y - sy)) / np.amax(np.absolute(y)), "\n")
    