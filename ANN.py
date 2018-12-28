import math as m
import numpy as n
from functools import reduce as r

TO1 = 0.01          #Target Output 1
TO2 = 0.99          #Target Output 2


def sigmoid(x):
    return (1 / (1 + n.exp(-x)))

def total_error(O1, O2, TO1 = TO1, TO2 = TO2):
    EO1 = 0.5 * ((TO1 - O1) ** 2)
    EO2 = 0.5 * ((TO2 - O2) ** 2)
    return EO1 + EO2

def d_sigmoid(y):
    return y * (1.0 - y)
    

hidden = [0.03, 0.04]
output = [0.43, 0.53]
sig_hid = list(map(sigmoid, hidden))
sig_out = list(map(sigmoid, output))

print("Hidden Sigmoid Result - > ", sig_hid)
print("Output Sigmoid Result - > ", sig_out)
print("Total Error - > ", total_error(sig_out[0], sig_out[1]))

print(list(map(d_sigmoid, sig_out)))

