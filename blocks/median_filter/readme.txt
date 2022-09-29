This block filters out time-variant interference by deeming any points in power too far away from the median power of the signal an "outlier" and replacing outliers with the median value. This will discard any spikes in power from local interference and will, if configured properly, not discard power spikes from the pulsar (since pulsar signal strenght is assumed to be relatively low). This block utilizes and embedded Python block with custom code to do this.

Parameters:
	- samp_rate (float): sample rate of incoming samples--make sure to take into account any decimation which occurs before this block (samples per second)
	- deviations (float): number of deviations a data point may vary from the median power before the data point is considered an outlier and thrown away
	- baseline_time (float): amount of time to consider data before calculating median power value (seconds)
