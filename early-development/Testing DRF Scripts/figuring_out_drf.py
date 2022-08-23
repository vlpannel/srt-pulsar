import digital_rf
import datetime
import dateutil.parser
import calendar

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

    tlen = 1/(29.7)

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
