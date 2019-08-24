import numpy as np
import matplotlib.pyplot as plt

def Polynomial(t, X,Y):
    A=Y
    B=Y
    n=len(A)
    C = []
    for j in range(1,n):
        A = list(B)
        C.append(B[j-1])
        for i in range(j,n):
            B[i]=(A[i]-A[i-1])/(X[i]-X[i-j])
        C.append(B[n-1])
        S=0
        P=1
    for k in range(n):
            S=S+P*C[k]
            P=P*(t-X[k])
    return S

R = int(input("Enter for X & Y axis element: "))
X = list(map(float,input("\nEnter the numbers : ").strip().split()))[:R]
Y = list(map(float,input("\nEnter the numbers : ").strip().split()))[:R]
print('\n',X)
print('\n',Y)
I = np.arange(-2,10,0.1)
plt.plot(X,Y, "ro")
plt.plot(I,Polynomial(I,X,Y),"b")
plt.show()

