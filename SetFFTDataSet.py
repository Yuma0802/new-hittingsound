#coding: utf-8
import numpy as np
from helper.setFFT import setFFT

data0 = np.load("noFFTnumpy/noFFT_Xtrain.npy")
data1 = np.load("noFFTnumpy/noFFT_Xtest.npy")

data2 = setFFT(data0)
data3 = setFFT(data1)

print(data2.shape)
print(data3.shape)

np.save("fftNumpy/FFT_Xtrain", data2)
np.save("fftNumpy/FFT_Xtest", data3)

print("Success!")