import numpy as np		#各種計算に使用
import pandas as pd
import matplotlib.pyplot as plt
import glob
import os
import sys

#グラフを表示する領域を，figオブジェクトとして作成．
fig = plt.figure(figsize = (24,16), facecolor='lightblue')

for p in range(41):
  i = p
  x = np.array(range(0, 2048))

  y = train_data[i]


  c = 'blue'
  l = i

  xl = 'x'
  yl = i

  #グラフを描画するsubplot領域を作成。
  num = p +1
  ax = fig.add_subplot(6, 7, num)

  #各subplot領域にデータを渡す
  ax.plot(x, y, color=c, label=l)
  #各subplotにxラベルを追加
  ax.set_xlabel(xl)

  #各subplotにyラベルを追加
  ax.set_ylabel(yl)

  # 凡例表示
  ax.legend(loc = 'upper right') 

plt.subplots_adjust(left=0.125,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.2, 
                    hspace=0.35)
fig.savefig('plot1.png')
