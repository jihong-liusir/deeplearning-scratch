import numpy as np

def AND1(x1, x2): #与门
    w1, w2, theta = 0.5, 0.5, 0.7
    temp = x1*w1 + x2*w2
    if temp <= theta:
        return 0
    elif temp > theta:
        return 1

def AND(x1, x2): # 与门
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2): # 与非门
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # 仅权重和偏置与AND不同
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2): # 或门
    x = np.array([x1, x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))
