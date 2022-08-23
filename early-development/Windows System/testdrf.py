import numpy as np
import digital_rf as drf

def printall(arr):
    printed = 0
    for elem in arr:
        print(elem, end='\t\t')
        printed += 1
        if printed >= 8:
            print()
            printed = 0
    print()

savefile = r'C:\Users\vlpannel\Desktop\drftest'
savedata = np.fromfile(savefile, dtype=np.complex64)
norepeats = []
for i in range(savedata.size):
    if i == 0 or savedata[i-1] != savedata[i]:
        norepeats += [savedata[i]]
norepeats = np.array(norepeats)

original = r'E:\pulsar\2022-05-26\usrp-rx0-r_20220526T200000_20220526T210800\rf_data'
do = drf.DigitalRFReader(original)
chan = 'misa-l2'
s, e = do.get_bounds(chan)
prop = do.get_properties(chan)
originaldata = do.read_vector(s, norepeats.size, chan)
print(f'Bounds: {s, e}\n\n')

print(f'Saved: {savedata}')
#printall(savedata[0:1000])
print()
print(f'Original: {originaldata}')
#printall(originaldata[0:1000])
print(savedata == originaldata)
print()

for i in range(max(norepeats.size, originaldata.size)):
    print(norepeats[i], '\t', originaldata[i])
print(norepeats == originaldata)