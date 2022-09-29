# Basic Utilities of these Flowgraphs

The GRC flowgraphs here are created mainly for performing pulsar processing, but they may be freely adapted in other necessary applications.

This repo contains both GRC flowgraphs that generate hierarchical blocks as well as example flowgraphs which perform pulsar processing. Because this software is designed for use with the MIT Haystack Small Radio Telescope, it is intended to work with ZeroMQ and to take in complex raw data samples to produce either vectors of floats or a stream of floats to be saved or displayed via QT GUI. The final output is the average power of the received signal over phase (split into 1024 phase bins).

## Complete Processing

If intending to perform the entire processing pipeline, the flowgraphs under "examples" ways of using the created capabilities to do this.

The GRC hierarchical blocks designed for pulsar processing (under "blocks") may help in the pipeline (make sure to generate before use), as they can perform specific steps in the processing, but using hierarchical blocks can be avoided as well when copying a specific custom block or recreating a sequence of blocks in another flowgraph may be just as effective.

## Processing Steps

The entire pulsar pipeline is as follows:
1. Collect raw complex data (whatever source block is used)
2. Channelize the signal into frequencies (Polyphase Channelizer block if using multiple channels, Polyphase Decimator block if only processing one channel)
3. Convert signal to power (Complex to Mag^2 block)
4. Filter out time-variant interference (Filter Outliers hierarchical block) and dedisperse if using multiple channels (Incoherent Dedispersion hierarchical block)
5. Fold (either Fold 1 or Fold 2 hierarchical blocks or using conversion to and integration of vectors)
6. Output pulse profile (whatever sink block is used; may also convert output vectors to streams)

## Pre-Built Blocks

**Fold 1**: uses custom Python block utilizing psrdynspec pulsar processing tools to fold power over time of signal

**Fold 2**: uses built-in GRC blocks to fold timeseries of power

**Filter Outliers (based on median)**: filters outliers using median absolute deviation (using embedded Python block)

**Incoherent Dedispersion**: delays each channel by a calculated amount (using Python module) to align each channel's pulsar spike
