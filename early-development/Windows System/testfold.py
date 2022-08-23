import psrdynspec
from psrdynspec import fold as fld
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *

ts = np.zeros(10)
ts[np.array([2, 4, 6, 8])] = 1
times = np.arange(ts.size) / 5
per = .8
Nbins = 1024
rc = True
print(f'ts = {ts}\ntimes = {times}')
folded = fld.fold_ts(ts, times, per, Nbins, rc)
print(folded)

plt.plot(folded[0])
plt.show()