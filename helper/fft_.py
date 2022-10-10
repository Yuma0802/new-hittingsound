# -*- coding: utf-8 -*-

from scipy import signal	#FFTに使用
import numpy as np		#各種計算に使用

#窓関数を作成し，切り取ったデータに掛け合わせ，FFTを行う	

def FFT(split_data) :
	#窓関数作成（ハミング窓）
	ham = signal.hamming(len(split_data[1]))

	#FFT後のデータを記録するリストを作成
	fft_data = [np.zeros(0, dtype="int16")]

	fft_data.append(0)

	#切り取ったデータの数分ループ
	j = 1
	while j < len(split_data):

		#切り取ったデータに窓関数を掛け合わせる		
		split_data[j] = split_data[j] * ham

		#FFTを行う
		fft = np.fft.fft(split_data[j])

		#振幅ストペクルを求める
		s = [np.sqrt(c.real**2 + c.imag**2) for c in fft]

		#小数部を3桁にする
		fft_data.append(np.round(s, 3))

		j += 1

	fft_data.pop(0)

	#FFT後の振幅の最大値を求める
	maxval = 0.0			#データの最大値
	j = 1
	while j < len(fft_data):
		val = max(fft_data[j])
		if val > maxval:
			maxval = val
		j += 1

	return fft_data, maxval
