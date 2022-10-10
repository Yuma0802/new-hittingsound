# -*- coding: utf-8 -*-

import csv			#CSVファイルの出力に使用
import numpy as np		#各種計算に使用

def Write_Data_CSV(write_file_name, fft_data, fileno) :
	#FFT後のデータをCSVファイルに書き込む

	#1番目のファイルだった場合
	if fileno == 1:

		#書き込み先のcsvファイルをオープン
		f = open(write_file_name, 'w')
		writer = csv.writer(f)
		
		#1行目に番号を書き込み
		num = []
		j = 0
		while j < len(fft_data[1]):
			num.append(j)
			j += 1
		fft_data[0] = num

	else:
		#書き込み先のcsvファイルをオープン
		f = open(write_file_name, 'a')
		writer = csv.writer(f)

		#2番目以降は1行目を削除
		fft_data.pop(0)

	
	#ファイルに書き込み
	writer.writerows(fft_data)

	f.close()

	return
