import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([2, 2, 5, 8])


# def getAB(x, y):
#     f0 = np.ones(len(x))
#     f1 = x
#     A = np.transpose(np.array([f0, f1]))
#     #B = np.transpose(np.array([y]))
#     B = y.reshape(len(y),1)
#     return A, B
#
# # b <- getAB(X,Y)[1]
#

def getAB(x, y):
    f0 = np.ones(len(x))
    f1 = x
    f2 = x**2
    A = np.transpose(np.array([f0, f1, f2]))
    #B = np.transpose(np.array([y]))
    B = y.reshape(len(y),1)
    return A, B

A, B = getAB(x, y)
print("a")
print(A)
print("b")
print(B)
theta_hat = np.linalg.inv(A.T @ A) @ (A.T @ B)
r = np.linalg.norm(A @ theta_hat - B)
print("theta:")
print(theta_hat)
print("r")
print(r)

plt.plot(x,y,"o",color = 'blue')


t = np.linspace(min(x),max(x),50)
print(t)
#model = [theta_hat[0] + theta_hat[1] * ti for ti in t ]
model = [theta_hat[0] + theta_hat[1] * ti + theta_hat[2]*(ti**2) for ti in t ]
plt.plot(t,model,color = 'red')
plt.show()

#----------------------------

#mul_matrix
# def mulMatrix(A,B):
#     res = []
#     if(len(A[0]) != len(B)):
#         return 'Invalid'
#     for i in range(len(A)):
#         for j in range(len(B[0])):
#             res += A[i][j] * B[i][j]
#     return res

def mulMatrix(A,B):
    if(len(A[0]) != len(B)):
        return 'Invalid'
    C = [[0 for m in range(len(A))] for n in range(len(B[0]))]
    for i in range(len(A)):
        res = 0
    for _ in range(len(B)):
        for j in range(len(B[0])):
            res += A[i][_] * B[_][j]

    return res

res = mulMatrix(A,B)
print("Multi Matrix: ")
print(res)

#luy thua
