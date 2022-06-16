import digital_rf
import datetime
import dateutil.parser
import calendar

import os, traceback, h5py, pmt, six
from digital_rf import DigitalRFReader, util
import numpy as np

# H5 READING STUFF TO VALIDATE ITEM TYPE
H5T_LOOKUP = {
    # (class, itemsize, is_complex): {name, dtype, missingvalue}
    (h5py.h5t.INTEGER, 1, False): dict(
        name="s8", dtype=np.int8, missingvalue=np.iinfo(np.int8).min
    ),
    (h5py.h5t.INTEGER, 2, False): dict(
        name="s16", dtype=np.int16, missingvalue=np.iinfo(np.int16).min
    ),
    (h5py.h5t.INTEGER, 4, False): dict(
        name="s32", dtype=np.int32, missingvalue=np.iinfo(np.int32).min
    ),
    (h5py.h5t.INTEGER, 8, False): dict(
        name="s64", dtype=np.int64, missingvalue=np.iinfo(np.int64).min
    ),
    (h5py.h5t.FLOAT, 4, False): dict(name="f32", dtype=np.float32, missingvalue=np.nan),
    (h5py.h5t.FLOAT, 8, False): dict(name="f64", dtype=np.float64, missingvalue=np.nan),
    (h5py.h5t.INTEGER, 1, True): dict(
        name="sc8",
        dtype=np.dtype([("r", np.int8), ("i", np.int8)]),
        missingvalue=(np.iinfo(np.int8).min,) * 2,
    ),
    (h5py.h5t.INTEGER, 2, True): dict(
        name="sc16",
        dtype=np.dtype([("r", np.int16), ("i", np.int16)]),
        missingvalue=(np.iinfo(np.int16).min,) * 2,
    ),
    (h5py.h5t.INTEGER, 4, True): dict(
        name="sc32",
        dtype=np.dtype([("r", np.int32), ("i", np.int32)]),
        missingvalue=(np.iinfo(np.int32).min,) * 2,
    ),
    (h5py.h5t.INTEGER, 8, True): dict(
        name="sc64",
        dtype=np.dtype([("r", np.int64), ("i", np.int64)]),
        missingvalue=(np.iinfo(np.int64).min,) * 2,
    ),
    (h5py.h5t.FLOAT, 4, True): dict(
        name="fc32", dtype=np.complex64, missingvalue=(np.nan + np.nan * 1j)
    ),
    (h5py.h5t.FLOAT, 8, True): dict(
        name="fc64", dtype=np.complex128, missingvalue=(np.nan + np.nan * 1j)
    ),
}

def get_h5type(cls, size, is_complex):
    try:
        typedict = H5T_LOOKUP[(cls, size, is_complex)]
    except KeyError:
        raise ValueError("HDF5 data type not supported for reading.")
    return typedict

target = dateutil.parser.parse('2022-05-26T20:00:00')
ut_target = calendar.timegm(target.timetuple())
tlen = 1/100.0

do = digital_rf.DigitalRFReader('/Volumes/NO NAME/pulsar/2022-05-26/rf_data')  # digital_rf object from folder 'example'
print('Channels: %s' % (do.get_channels())) # prints list of channels

for chan in do.get_channels():  # for every channel (string in list)
    s, e = do.get_bounds(chan)
    prop = do.get_properties(chan)
    sr = prop['sample_rate_numerator']
    denom = prop['sample_rate_denominator']
    print(f'\ns = {s}\ne = {e}\nsr = {sr}\ndenom = {denom}')   # printing all the properties (start, end, properties, sample rate num, sample rate denom)
    print('\nPROPERTIES: ') # print properties
    for p in prop:
        print('\t' + p + ' : ' + str(prop[p]))

    sd = datetime.datetime.utcfromtimestamp(s/sr)
    ed = datetime.datetime.utcfromtimestamp(e/sr)
    print('\nChannel %s...\tSample Rate: %s\tStart: %s\tEnd: %s' % (chan, sr/denom, sd.isoformat(), ed.isoformat()))  # prints channel's sample rate, start and end times

    tlen = 1/(30.0)

    nsamp = int(tlen*sr)
    #nsamp = e - s + 1    # assuming nsamp is number of samples
    sindex = int(ut_target*sr)
    #sindex = s     # assuming sindex is start index (first to put in vector dvec)
    print(f'\ntarget ({type(target)}): {target}')
    print(f'ut_target ({type(ut_target)}): {ut_target}')
    print(f'tlen ({type(tlen)}): {tlen}')

    print(f'\nnsamp: {nsamp}\t\tsindex: {sindex}')

    dvec = do.read_vector_c81d(sindex, nsamp, chan)
    print(f'\nRESULT: {dvec} {type(dvec)}  {dvec.dtype}\n\tlength: {len(dvec)} (shape: {dvec.shape})\n\n')

    print(f'\n\nType Class: {prop["H5Tget_class"]}\t\tItem Size: {prop["H5Tget_size"]}\t\tIs Complex: {prop["is_complex"]}')
    item_type = get_h5type(prop['H5Tget_class'], prop['H5Tget_size'], prop['is_complex'])['dtype']
    out_type = get_h5type(prop['H5Tget_class'], prop['H5Tget_size'], prop['is_complex'])['name']
    print(f'Item Type: {item_type}\t\tOut Type: {out_type}')
