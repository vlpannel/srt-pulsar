This block takes multiple channels from a polyphase filterbank and uses the equation which connects dispersion measure and frequency to dedisperse, or realign, the frequency channels such that each channel's pulsar-resultant spike in power occurs "at the same point in time". It utilizes a custom Python module to do the calculation and can dedispers up to 32 channels given the right parameters.

This block relies on traditional polyphase filterbank indexing (0 is at center frequency, index increases as frequency increase until at top edge of bandwidth, then goes to low edge of bandwidth before continuing to increase index).

Parameters:
	- center_freq (float): center frequency (MHz)
	- bandwidth (float): bandwidth (MHz)
	- dm (float): dispersion measure of pulsar
	- num_channels (int): number of frequency channels
	- channels (array-like): list of channels actually being input/used
	- samp_rate (float): sample rate of incoming samples--consider decimation (samples per second)
