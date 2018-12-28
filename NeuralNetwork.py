import numpy as n

TARGET = n.array([0.35, 0.67])  #Target Values
INPUT = n.random.randn(1,2)     #Input Values
HIDDEN1 = 2                     #N nodes in hidden layer 1
BIAS = n.array([1, 1])          #Bias Values
LEARN = 0.5                     #Learning Rate

global weights1, weights2

#Random Weigths
weights1 = n.random.randn(n.shape(INPUT)[1], HIDDEN1)
weights2 = n.random.randn(HIDDEN1, len(TARGET))

#Sigmoid Function
def sigmoid(x):
    return (1 / (1 + n.exp(-x)))

def feed_forward():
    global netH, outH, netH, netO, outO, error
    #Hidden Layer's net and out values
    netH = n.dot(INPUT, weights1) + BIAS[0]
    outH = sigmoid(netH)

    #Output's Net and Out Values
    netO = n.dot(outH, weights2) + BIAS[1]
    outO = sigmoid(netO)

    #error Calculation
    error = ((TARGET - outO)**2) * 0.5

def back_propagation():
    global weights1, weights2
    #1st Layer
    dnetO_dW2 = outH
    doutO_dnetO = outO * (1 - outO)
    dE_doutO = outO - TARGET
    dE_dW2 = dnetO_dW2 * doutO_dnetO * dE_doutO
    weights2 += (-LEARN * dE_dW2)    #weights2 Update
    
    #2nd Layer
    dnetO_doutH = weights2
    doutH_dnetH = outH * (1 - outH)
    dnetH_dW1 = INPUT
    dE_dW1 = dE_doutO * doutO_dnetO * dnetO_doutH * doutH_dnetH * dnetH_dW1
    weights1 += (-LEARN * dE_dW1)   #weights1 Update

feed_forward()
print("Input values", INPUT, '\n')
print("Target Values ", TARGET, '\n')
print("Values of Weights (random)\n", weights1, '\n\n', weights2, '\n')
print("1st Output Values ", outO, '\n')
print("Training the network...")
iterations = range(0, 700000)
for i in  iterations:
    back_propagation()
    feed_forward()
print("Result after", len(iterations)," iterations ", outO)


 


        



