# -*- coding: utf-8 -*-

import numpy as np		#各種計算に使用

def Split_Data(data, rate, split_range_y) :
	i = 0
	while i < 3:
		print("split_range_y = "+str(split_range_y))
		split_data, error = Split_Data_Main(data, rate, split_range_y)
		if len(split_data) > len(data)/(44100/3) :
			break
		else :
			split_range_y -= 0.1
		if i == 2 :
			error = 1

		i += 1
	return split_data, error

def Split_Data_Main(data, rate, split_range_y) :
	#dataの中で大きく振幅が変化したところを分割していく

	#切り取り後のデータが入るリストを作成
	split_data = [np.zeros(0, dtype="int16")]

	split_data_range = 1024		#切り取るデータの範囲(サンプル数)
	split_range_x = 100		#探索範囲x
	#split_range_y = 0.6		#探索範囲y
	max_down = 10			#下がってもいい回数
	split_count = 0			#カウンター
	split_pos = []

	#dataの要素数分ループ
	j = split_data_range
	while j < (len(data) - split_data_range):

		if split_count > 0:
			split_count += 1
			#切り取る範囲が重複しないようにする
			if split_count > split_data_range:
				split_count = 0

		elif data[j] < -split_range_y/2.0:
			#振幅が大きく下がった場所を見つけた場合
			#そこから前方を探索
			k = 1
			count = 0
			while k < split_range_x:

				#max_down回下がった場合ループを抜ける
				if data[j+k] <= data[j+k-1]:
					count += 1
					if count > max_down:
						break

				#範囲内に振幅が大きく上がる場所があった場合
				if (data[j+k] - data[j]) > split_range_y:
					#切り取る位置を記録
					split_pos.append(j)
					split_count = 1
					#切り取る範囲内のデータを記録し，リストに追加
					split_data.append(np.copy(data[j-split_data_range:j+split_data_range]))
					break
				k += 1
		j += 1


	#エラー検知
	error = 0
	if len(split_data) <= 1:
		#print("error:can not split data")
		error = 1

	return split_data, error
