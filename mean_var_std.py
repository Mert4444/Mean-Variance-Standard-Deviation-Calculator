import numpy as np


def calculate(x):
    if (type(x) ==list and len(x)==9):
        mtrx = np.array(x)
        mtrx = mtrx.reshape(3,3)
        dictn = {"mean":[list(mtrx.mean(axis=0)),list(mtrx.mean(axis=1)),mtrx.mean()],
             "variance":[list(mtrx.var(axis=0)),list(mtrx.var(axis=1)),mtrx.var()],
             "standard deviation":[list(mtrx.std(axis=0)),list(mtrx.std(axis=1)),mtrx.std()],
             "max":[list(mtrx.max(axis=0)),list(mtrx.max(axis=1)),mtrx.max()],
             "min":[list(mtrx.min(axis=0)),list(mtrx.min(axis=1)),mtrx.min()],
             "sum":[list(mtrx.sum(axis=0)),list(mtrx.sum(axis=1)),mtrx.sum()]
             
             }
        return dictn
    else:
        print("List must contain nine numbers." )

