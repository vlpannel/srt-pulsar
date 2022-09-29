This is the block that performs folding a timeseries of power (float32 values) in order to find the average  power of the signal per phase. It utilizes psrdynspec and a custom embedded Python block to do this, taking in a single stream of float32s and outputting a float vector of length 1024 representing the power in each of 1024 phase bins.

Parameters:
	- samp_rate (float): sample rate of incoming stream (samples per second)
	- period (float): period of folding/pulsar (seconds)
	- integration_time (float): number of seconds of data to collect before folding
