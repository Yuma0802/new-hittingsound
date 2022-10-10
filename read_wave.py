# -*- coding: utf-8 -*-

import wave			#waveファイルを扱うために使用
import numpy as np		#各種計算に使用

def Read_Wave(read_file_path):
	#waveファイル読み込み
	wf = wave.open(read_file_path, "r")

	#バイナリデータ読み込み
	buf = wf.readframes(wf.getnframes())
	
	#音声データのサンプリング周波数取得
	rate = wf.getframerate()
	size = float(wf.getnframes())

	#バイナリデータを整数データに変換
	data = np.frombuffer(buf, dtype="int16")

	#振幅の最大値を求める
	amp = (2**8) ** wf.getsampwidth() / 2

	#正規化前のデータを保持
	intdata = np.copy(data)

	#データを振幅の最大値で割り正規化
	data = data / amp

	#waveファイルを閉じる
	wf.close()

	return data, rate
