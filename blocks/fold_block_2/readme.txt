This is also a block that performs pulsar folding (see description in fold_block_1's readme), but instead of using a custom embedded Python block, it uses built-in GNU Radio utilities to fold the timeseries of power.

Parameters:
	- samp_rate (float): sample rate of incoming stream (samples per second)
	- period (float): period of folding/pulsar (seconds)
	- integration_time (float): number of seconds of data to collect before folding
