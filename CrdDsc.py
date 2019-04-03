import numpy as np
import pickle
import os
from sklearn import linear_model

if __name__ == "__main__":
    # Import Data
    xy = open('mystery.dat', 'r').read()
    no_of_data = len(xy.split("\n")) - 1

    XY_vec_str = []
    for i in xrange(no_of_data):
        XY_vec_str.append([])
        XY_vec_str[i] = xy.split("\n")[i].split(",")
     
    XY_vec = []
    for i in xrange(no_of_data):
        XY_vec.append([])
        for j in xrange(101):
            XY_vec[i].append(float(XY_vec_str[i][j]))

    X, Y = [], []
    for i in xrange(no_of_data):
        X.append([])
        Y.append([])
        X[i] = XY_vec[i][0:100]
        X[i].append(1)
        Y[i] = XY_vec[i][100]


    X, Y = np.array(X), np.array(Y)
    L = linear_model.Lasso(alpha = 0.5)
    L.fit(X,Y)
    idx = L.coef_.argsort()[-10:][::-1]
    print np.sort([idx[i]+1 for i in xrange(len(idx))])

