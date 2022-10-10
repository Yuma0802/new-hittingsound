#ライブラリ読み込み
import numpy as np		#各種計算に使用
import importlib
import os
import sys
import glob
import soundfile as sf
from pydub import AudioSegment


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


def splitdata_convert(dirPath):
  files = glob.glob(dirPath+"/*")
  data_array = np.empty((0,2048), int)
  for filename in files:
    #waveファイルの読み込み
    data, rate = sf.read(filename)
    data_array = np.append(data_array, np.array([data]), axis=0)
  
  print(data_array.shape)
  return data_array


    
  
  

  
  