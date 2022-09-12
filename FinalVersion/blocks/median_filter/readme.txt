This block filters out time-variant interference by deeming any points in power too far away from the median power of the signal an "outlier" and replacing outliers with the median value. This will discard any spikes in power from local interference and will, if configured properly, not discard power spikes from the pulsar (since pulsar signal strenght is assumed to be relatively low). This block utilizes and embedded Python block with custom code to do this. It has the ability to take in and filter multiple (up to 32) streams of data. Each nth input port corresponds to the nth output port.

Parameters:
	- channels (list of ints): which channels are being filtered (MUST correspond to the channels that are connected to the in ports)
	- 
