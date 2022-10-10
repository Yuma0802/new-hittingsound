#coding: utf-8
import wave
import sys
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import pandas as pd
from helper.setFFT import setFFT
import helper.split_data as split_data
from helper.splitdata_convert import splitdata_convert

dir_name = 'train_g_data'
split_range = 0.8
csv_name = "test_g_data.csv"

# data = splitdata_convert(dir_name)

# np.save('split_test_ng', data)

# split_data.split_data_main(dir_name, split_range)

data0 = np.load("noFFTnumpy/noFFT_Xtrain.npy")
print(data0.shape)

data1 = setFFT(data0)

# data0 = pd.read_csv('train_gdata_test.csv', encoding='utf-8', header=0)
# data1 = np.array(data0.iloc[:,:])

# maxval = data1.flatten()[np.argmax(data1.flatten())]
# data2 = data1 / maxval 

print(data1[0].shape)
y = data1[0]

x = np.array(range(0, 2048))

plt.plot(x, y)

plt.show()