import numpy as np


def ninzero(A):
    for a in range(len(A)):
        for b in range(len(A[a])):
            if A[a][b]!=0 :
                return a,b
            
            






A = np.zeros((100,100))
A[56,70] = 1
print(ninzero(A))