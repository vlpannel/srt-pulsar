import digital_rf
import datetime
import dateutil.parser
import calendar
import numpy as np

target = dateutil.parser.parse('2022-08-02T20:10:00')
ut_target = calendar.timegm(target.timetuple())
tlen = 1/100.0

do = digital_rf.DigitalRFReader('C:\\Users\\vlpannel\\Desktop\\raw')
print('Channels: %s' % (do.get_channels()))

chan = 'ch0'
s, e = do.get_bounds(chan)
prop = do.get_properties(chan)

print(s, ',',  e)
print(prop)
sr = prop['samples_per_second']

print(type(s), '\t', type(e), '\t', type(sr))
#prop['samples_per_second'] = float(prop['samples_per_second'])
#sr = prop['samples_per_second']
#print(type(sr))

#sd = datetime.datetime.utcfromtimestamp(s/(sr))
#ed = datetime.datetime.utcfromtimestamp(e/(sr))

tlen = 1/29.7
nsamp = int(tlen*sr)
sindex = int(ut_target*sr)

dvec = do.read_vector(s + 1000, 2000, chan)
print(dvec)
print(np.delete(dvec, np.where(np.isnan(dvec))))