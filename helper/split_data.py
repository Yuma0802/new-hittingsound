#ライブラリ読み込み
import numpy as np		#各種計算に使用
import importlib
import os
import sys
import glob
from pydub import AudioSegment

#pyファイル読み込み
import read_wave
import helper.make_data as make_data
import helper.fft_ as fft_
import helper.write_data_csv as write_data_csv
import helper.write_label_csv as write_label_csv
importlib.reload(read_wave)
importlib.reload(make_data)
importlib.reload(fft_)
importlib.reload(write_data_csv)
importlib.reload(write_label_csv)

def split_data_main(dirPath, split_range_y, csv_name):
	files = glob.glob(dirPath+"/*")
	fileno = 0
	for filename in files:
		#waveファイルの読み込み
		data, rate = read_wave.Read_Wave(filename)

		#dataの中で大きく振幅が変化したところを分割していく
		split_data, split_error = make_data.Split_Data(data, rate, split_range_y)
		if split_error == 1:
			print("error: split_range_yの値を下げてください")
			fileno += 1
			continue

		#split_dataをcsvファイルに書き込む
		write_data_csv.Write_Data_CSV(csv_name, split_data, fileno)

		#進捗を出力
		print("complated data_"+str(fileno)+", "+str(len(split_data))+" files")

		#リストを初期化
		split_data.clear()
		fileno += 1
		
		
