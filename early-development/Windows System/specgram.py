import digital_rf as drf
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

filedir = r'C:\Users\vlpannel\Desktop\newpfbdata'
files = ['ch' + str(n) for n in range(31)]
files = files[16:] + files[:16]

data = []
for filename in files:
    data += [np.fromfile(filedir + '\\' + filename, dtype=np.complex64)]
data = np.array(data)

print(data)
print(data.shape)

plt.imshow(data, aspect='auto', norm=Normalize())
plt.show()