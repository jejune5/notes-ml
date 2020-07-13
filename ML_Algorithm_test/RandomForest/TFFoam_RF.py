import numpy as np
from ML_Algorithm_test.RandomForest.randomforest import model_RandomForest as RF

training_inputs = np.load('training_inputs.npy')
print(training_inputs.shape)

training_outputs = np.load('training_outputs.npy')
print(training_outputs.shape)

RF(training_inputs,training_outputs,save=1)
