import matplotlib.pyplot as plt
import importlib
import os
import random
import numpy as np
import pandas as pd

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

data0 = pd.read_csv('train_g_data.csv', encoding='utf-8', header=0)
data1 = pd.read_csv('test_g_data.csv', encoding='utf-8', header=0)
train_ngdata = np.load("split_train_ng.npy")
test_ngdata = np.load("split_test_ng.npy")
train_gdata = np.array(data0.iloc[:,:])
test_gdata = np.array(data1.iloc[:,:])

print(train_gdata.shape)
print(train_ngdata.shape)
print(test_gdata.shape)
print(test_ngdata.shape)

write_label_csv.Write_Label_CSV("train_label.csv", len(train_gdata),len(train_ngdata))
write_label_csv.Write_Label_CSV("test_label.csv", len(test_gdata),len(test_ngdata))

data2 = pd.read_csv('train_label.csv', encoding='utf-8', header=0)
data3 = pd.read_csv('test_label.csv', encoding='utf-8', header=0)
train_label = np.array(data2.iloc[:,:])
test_label = np.array(data3.iloc[:,:])

print(train_label.shape)
print(test_label.shape)

trainData = np.concatenate([train_gdata,train_ngdata])
testData = np.concatenate([test_gdata,test_ngdata])

print(trainData.shape)
print(testData.shape)

np.save("noFFT_Xtrain", trainData)
np.save("noFFT_Ytrain", train_label)
np.save("noFFT_Xtest", testData)
np.save("noFFT_Ytest", test_label)





