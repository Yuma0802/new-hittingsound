import numpy as np		#各種計算に使用
import pandas as pd
import numpy as np		#各種計算に使用
import pandas as pd
import matplotlib.pyplot as plt
from helper.make_graph import make_graph
import fftNumpy

data0 = np.load('fftNumpy/FFT_Xtrain.npy')


# fig = plt.figure(figsize = (24,16), facecolor='lightblue')
# Cdata1 = data0[554]
# Cdata2 = data0[555]
# Cdata3 = data0[556]
# Cdata4 = data0[557]

# x = np.array(range(0,2048))

# c = 'blue'
# l1 = 554
# l2 = 555
# l3 = 556
# l4 = 557

# xl = 'x'
# y1 = 554
# y2 = 555
# y3 = 556
# y4 = 557

# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)
# ax1.plot(x, Cdata1, color=c, label=l1)
# ax2.plot(x, Cdata2, color=c, label=l2)
# ax3.plot(x, Cdata3, color=c, label=l3)
# ax4.plot(x, Cdata4, color=c, label=l4)

# # plt.subplots_adjust(left=0.125,
# #                     bottom=0.1, 
# #                     right=0.9, 
# #                     top=0.9, 
# #                     wspace=0.2, 
# #                     hspace=0.35)

# plt.show()