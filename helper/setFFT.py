#ライブラリ読み込み
import numpy as np		#各種計算に使用
import importlib
import os
import sys
import glob
from pydub import AudioSegment
from scipy import signal	#FFTに使用

#pyファイル読み込み
import helper.read_wave as read_wave
import helper.make_data as make_data
import helper.fft_ as fft_
import helper.write_data_csv as write_data_csv
import helper.write_label_csv as write_label_csv
importlib.reload(read_wave)
importlib.reload(make_data)
importlib.reload(fft_)
importlib.reload(write_data_csv)
importlib.reload(write_label_csv)

def setFFT(data_arry):
  #窓関数作成（ハミング窓）
	ham = signal.hamming(len(data_arry[1]))
  #FFT後のデータを記録するリストを作成
	fft_data = np.empty((0,2048), dtype="int16")

	for data in data_arry:
		#切り取ったデータに窓関数を掛け合わせる
		data = data * ham
    
    #FFTを行う
		fft = np.fft.fft(data)

    #振幅ストペクルを求める
		s = [np.sqrt(c.real**2 + c.imag**2) for c in fft]

		data1 = np.round(s, 3)
		fft_data = np.append(fft_data, np.array([data1]), axis=0)

	print(fft_data.shape)
	return fft_data





