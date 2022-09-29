# this module will be imported in the into your flowgraph

def dedisperse(center_freq, bandwidth, num_channels, channel, dm, samp_rate):
    '''
    Delay channel be specified amount given frequencies and dispersion measure. Assumes standard channel mapping and even number of channels. Aligns all channels with lowest channel (for delay purposes).

    Parameters
    ----------

    center_freq : float
        Center frequency in MHz

    bandwidth : float
        Total bandwidth of signal reception in MHz

    num_channels : int
        Number of channels into which bandwidth is divided (equally)

    channel : int
        Which channel is being dedispersed (0 is at center frequency)

    dm : float
        Dispersion measure of pulsar

    samp_rate : float
        Sample rate of incoming samples (samples per second)
    '''

    kdm = 4.149 * 1000    # dispersion measure constant (converted from GHz^2 to MHz^2 and ms to s)

    # find frequencies of lowest channel and current channel
    channel_width = bandwidth / num_channels
    v2 = center_freq - (bandwidth/2)     # lowest frequency
    if channel <= num_channels/2:       # current channel
        v1 = center_freq + (channel)*channel_width
    else:
        v1 = center_freq - (num_channels - channel)*channel_width

    # find amount of dispersion
    time_delta = kdm * dm * ((1/(v2**2)) - (1/(v1**2)))
    return int(time_delta * samp_rate)
