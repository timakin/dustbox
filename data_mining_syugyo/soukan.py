import rpy2.robjects as robjects

ctl = robjects.FloatVector([4.17,5.58,5.18,6.11,4.50,4.61,5.17,4.53,5.33,5.14])
trt = robjects.FloatVector([4.81,4.17,4.41,3.59,5.87,3.83,6.03,4.89,4.32,4.69])

soukan = robjects.r('function(x,y) cor.test(x,y)')
rtn = soukan(ctl, trt)
print rtn