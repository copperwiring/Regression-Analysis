#!/usr/bin/env python

import assignment1 as a1
import numpy as np
import matplotlib.pyplot as plt

(countries, features, values) = a1.load_unicef_data()

targets = values[:,1]

#features because they need to be from 8th column
x = values[:,7:]

x = a1.normalize_data(x)

N_TRAIN = 100
x_train = x[0:N_TRAIN,:]
x_test = x[N_TRAIN:,:]
t_train = targets[0:N_TRAIN]
t_test = targets[N_TRAIN:]

# Complete the linear_regression and evaluate_regression functions of the assignment1.py
# Pass the required parameters to these functions

(w, tr_err) = a1.linear_regression(x_train, t_train,'polynomial', reg_lambda=0, degree=0, mu=0, s=1)
(t_est, te_err) = a1.evaluate_regression(w, x_test,t_test)



train_err = tr_err
test_err = te_err



# Produce a plot of results.
plt.rcParams.update({'font.size': 15})
plt.plot(train_err.keys(), train_err.values())
#plt.plot(test_err.keys(), test_err.values())
plt.ylabel('RMS')
plt.legend(['Training error','Testing error'])
plt.title('Fit with polynomials, no regularization')
plt.xlabel('Polynomial degree')
plt.show()
