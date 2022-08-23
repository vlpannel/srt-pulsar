# SRT-py Progress (UROP Summer 2022, Viveca Pannell)

## Daily Work

### 5/23/2022
- Set up Anaconda and installed both mamba and GNU Radio (did not just miniforge or Miniconda).
- Connected to Nooelec NESDR and received signals (using CubicSDR).
- Created flow graph in GNU Radio based on the one in the presentation; no RTL-SDR source yet (cannot find that block?).

### 5/25/2022
- Downloaded osmosdr, digital\_rf, and other modules to allow connection between GNU Radio and RTL-SDR.
- Explored WVURAIL DSPIRA modules, watching Introduction to Signals lecture.
- (With help) got GlobalProtect MIT VPN and NoMachine installed and functioning.

### 6/20/2022
- Just because I haven't updated this log in a while does not mean I've been doing nothing.
- Have learned a lot about digital signal processing (DSP), Fourier transforms (FT), sampling, and complex numbers.
- Today studied complex sampling.
- Today rewrote basic binning Python script and then wrote shell debugging version.
- See GitHub commits/log for more info on recent changes and developments.
- See notes on personal tablet device for more notes and info.

### 6/21/2022
- Did a lot of reading about polyphase filterbanks; however, Kiyo was right that trying to understand all of the fundamentals can be unproductively "spinning one's wheels".
- Talked to Kiyo about how PFBs work as well as the binning we will need to do for pulsar processing.
- Made a few GRC flowcharts with PFB channelizer block.
- Wrote an outline for how to create a spectrogram with just numpy and pyplot.

### 6/23/2022
- In past few days have created flowgraphs and Python scripts to channelize data and then read it (eventual goal is to create spectrogram).
- Installed h5py through Anaconda.
