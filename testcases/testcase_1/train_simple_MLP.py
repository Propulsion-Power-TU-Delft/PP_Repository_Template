#!/usr/bin/env python3

# Title: train_simple_MLP.py
# Description: demonstration test case problem that demonstrates the regression test workflow
# Author: E.C.Bunschoten
# Date: 23-10-2024

# Import modules and set seed values for reproducability.
seed_value = 2
import os
os.environ['PYTHONASHSEED'] = str(seed_value)
seed_value += 1
import random
random.seed(seed_value)
seed_value += 1
import numpy as np
np.random.seed(seed_value)
seed_value += 1 
import tensorflow as tf
tf.random.set_seed(seed_value)
import csv 
from sklearn.preprocessing import StandardScaler
from MLP_functions import * 

u,v,y = write_input_data()

# Define controlling variables and dependend variables.
X_dim = np.hstack((u[:,np.newaxis], v[:,np.newaxis]))
Y_dim_ref = y[:,np.newaxis] 


# Scale input and output data
scaler_x = StandardScaler()
scaler_y = StandardScaler()

X_norm, Y_norm = scale_input_data(X_dim, Y_dim_ref, scaler_x, scaler_y)

# Define tensorflow model
model = define_tensorflow_model()

# Commence training
n_epochs = 100
history = model.fit(X_norm, Y_norm, epochs=n_epochs,shuffle=True)

# Evaluate MLP prediction
Y_norm_pred = model.predict(X_norm)
Y_dim_pred = scaler_y.inverse_transform(Y_norm_pred)

# Write MLP prediction to output file
output_data= np.hstack((X_dim, Y_dim_ref, Y_dim_pred))
output_vars = "u,v,y_ref,y_pred"
with open("test_data.csv","w+") as fid:
    fid.write(output_vars+"\n")
    csvwriter = csv.writer(fid,delimiter=',')
    csvwriter.writerows(output_data)