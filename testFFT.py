#coding: utf-8
import wave
import sys
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
import pandas as pd
from helper.setFFT import setFFT
from helper.splitdata_convert import splitdata_convert
from scipy import signal	#FFTに使用

data0 = np.load("noFFTnumpy/noFFT_Xtrain.npy")
print(data0.shape)
data1 = data0[0]

split_dataB = data0
split_dataA = data1

#窓関数作成（ハミング窓）
ham = signal.hamming(len(split_dataA))

#FFT後のデータを記録するリストを作成
fft_data = np.empty((0,2048), dtype="int16")

#切り取ったデータに窓関数を掛け合わせる		
split_dataA = split_dataA * ham

#FFTを行う
fft = np.fft.fft(split_dataA)

#振幅ストペクルを求める
s = [np.sqrt(c.real**2 + c.imag**2) for c in fft]

data2 = np.round(s, 3)

print(data2.shape)

y = data2

x = np.array(range(0, 2048))

plt.plot(x, y)

plt.show()