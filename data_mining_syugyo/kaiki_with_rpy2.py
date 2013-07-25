#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scipy
import numpy
from sklearn import datasets
import rpy2.robjects as rob
import pylab as pl

iris = datasets.load_iris()
X = iris.data[:, :2] #全ての行、２列
Y = iris.target #被説明変数

pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)
pl.xlabel('Length')
pl.ylabel('Width')
pl.suptitle("iristest scatter", fontsize=26)
pl.legend(Y ,'upper left')
pl.show()