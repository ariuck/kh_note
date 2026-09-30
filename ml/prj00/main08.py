# 퍼셉트론 , MLP, 신경망
import numpy as np
from fontTools.misc.cython import returns


def step(x):
    if x > 0:
        return 1
    else:
        return 0

#신경망
def perceptron(x,w,b):
    # w1,w2,w3,b
    #result = w1 * x1 + w2 * x2 + w3 * x3 + b
    #y = 판단을 도와주는 함수(result)
    z = np.dot(x, w) + b
    y = step(z)
    return y

def AND(x1,x2):
    y = perceptron(np.array([x1,x2]),np.array([0.5,0.5]), -0.9)
    return y

def OR(x1,x2):
    y = perceptron(np.array([x1,x2]),np.array([0.5,0.5]), -0.4)
    return y

def NAND(x1,x2):
    y = not AND(x1,x2)
    return int(y)

def NOR(x1,x2):
    t1 = NAND(x1,x2)
    t2 = OR(x1,x2)
    y = AND(t1,t2)
    return int(y)
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))