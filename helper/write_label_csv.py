# -*- coding: utf-8 -*-

import csv			#CSVファイルの出力に使用
import numpy as np		#各種計算に使用

def Write_Label_CSV(write_file_name, gdata, ngdata) :
	
	#ラベルデータをCSVファイルに書き込む
	f = open(write_file_name, 'w')
	writer = csv.writer(f)
	
	#1行目に0を書き込む
	writer.writerow([0])
	
	#gデータの数分0を書き込む
	i = 0
	while i < gdata:
		writer.writerow([0])
		i += 1
	
	#ngデータの数分1を書き込む
	i = 0
	while i < ngdata:
		writer.writerow([1])
		i += 1

	#f.close()
	
	return
