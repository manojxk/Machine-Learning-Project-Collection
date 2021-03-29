# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 22:27:21 2021

@author: Manoj Kumar
"""

class MPNeuron:
    def __init__(self, n= 3, inputs = [1,1,1], weights = [1,1,1], threshold = 2.5):
        self.n = n
        self.inputs = inputs
        self.weights = weights
        self.threshold = threshold
    def MP_Neuron_Input(self, n, inputs, weights, threshold):
        self.n = n
        self.inputs = inputs
        self.weights = weights
        self.threshold = threshold
    
    def MP_Neuron_Evaluate(self):
        wx = [self.inputs[i] * self.weights[i] for i in range(len(self.inputs))]
        weighted_sum = sum(wx)
        if(weighted_sum < self.threshold):
            return 0
        else:
            return 1

a = MPNeuron()
a.MP_Neuron_Input(5, [1,23,4,5,8], [1,1,1,1,1], 5)
a.MP_Neuron_Evaluate()