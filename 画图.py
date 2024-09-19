import matplotlib.pyplot as plt
import numpy as np
B = np.array([1,2],
              [2,3],
              [3,4],
              [4,5],
              [5,6])
print(B)
plt.plot(B[:,0],B[:,1],marker='o',color='r',linestyle='--',linewidth=2,label='line1')
plt.show()