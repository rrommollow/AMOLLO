import numpy as np

P = np.array([[4,9],[7,13]])
print(P)

Q = np.array([[6,8],[1,0]])
print(Q)

add = P+Q
print(add)

mul = P*Q
print(mul)

result = np.dot(P, Q)
print(result)