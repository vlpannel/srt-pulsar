# SRT Pulsar Processing

The Small Radio Telescope (SRT) is a framework for setting up a 2-meter dish antenna, accompanying (now software-defined) radio, and compatible software to be able to teach and practice radio astronomy techniques. It was developed by the MIT Haystack Observatory. The SRT software was updated in 2020 to be based in Python rather than C and utilizes GNU Radio for some of its data processing pipelines.

This is a project to add the ability for the SRT software to process pulsar data and generate power profiles that reflect the presence of a pulsar by showing characteristic spikes in power.

## Description

This repository includes multiple GNU Radio flowgraphs and Python code to add pulsar processing capabilities to the SRT and similar SDR software setups that use GNU Radio.

Pulsar processing entails reading in complex samples, putting the signal through a polyphase filterbank, finding the power over time of each channel (via Complex to Mag^2), filtering out time-variant interference (based on median absolute deviation), and then folding/integrating the timeseries over the pulsar's period to output a 1024-sample long vector of the power vs phase profile.

## Environment

This project was developed using a Miniconda environment with GNU Radio v3.9.5.0 (which requires Python 3.10.5) installed. The environment used conda-forge to install `gnuradio`, `digital_rf`, `gr-osmosdr`, and `pip` and then used pip to install [`mitarpysigproc`](https://github.com/MIT-Adaptive-Radio-Science/sigprocpython) and [`psrdynspec`](https://github.com/jswoboda/psrdynspec).

### Installation

Steps to replicate original set up:
1. Install applicable distribution of Miniforge from the GNU Radio Wiki [CondaInstall page](https://wiki.gnuradio.org/index.php?title=CondaInstall#Step_1:_Install_conda_itself)
	- Add conda-forge to channels: `conda config --add channels conda-forge`
	- Set channel priority to strict: `conda config --set channel\_priority strict`
2. Use Miniforge to install Mamba (increases speed of installations as substitute for Conda)
	- `conda install mamba`
3. Create and activate an environment for GNU Radio
	- `conda create -n gnuradio`
	- `conda activate gnuradio`
4. Use `mamba` (or `conda`) commands to install GNU Radio, Digital RF, OsmoSDR, and pip
	- `mamba install gnuradio digital_rf gr-osmosdr pip`
5. Download [mitarspysigproc (sigprocpython)](https://github.com/MIT-Adaptive-Radio_Science/sigprocpython) and [psrdynspec](https://github.com/jswoboda/psrdynspec) from GitHub and install them using pip
	- Navigate to each of the directories (sigprocpython-main and psrdynspec-master)
	- `pip install -e .` (for each directory)

### Using These Flowgraphs

If not an experienced user of GNU Radio, please see below directions on using GNU Radio Companion and GNU Radio hierarchical blocks.

In order to open and use flowgraphs, after downloading them, activate the applicable GNU Radio Conda environment and use command `gnuradio-companion` to open GNU Radio Companion (GRC), GNU Radio's GUI for running and manipulating flowgraphs. For more information on how to use GRC, see [GNU Radio Wiki](https://wiki.gnuradio.org/index.php?title=Main_Page).

This repo includes GRC hierarchical blocks which can be incorporated into other flowgraphs and customized via parameters. To use a hierarchical block, simply click the "Reload Blocks" button in GRC and find the correct block in the list of blocks (should be under the category of "GRC Hier Blocks") and treat the hierarchical block just as any other normal block. To directly manipulate how all instances of a hierarchical block work internally, you can directly edit the blocks by opening their GRC flowgraph files and making changes. Every time the hierarchical block's GRC flowgraph is altered, you much refresh blocks before using again in another flowgraph.

## Navigating This Repository

This repository is not available for installation; it simply includes possibly useful files to download and use through GNU Radio. The repository is structured as follows
- **blocks**: holds specially designed GRC blocks from pulsar processing
- **docs**: documentation detailing how to use pulsar processing blocks
- **examples**: examples of pulsar processing
- **environment**: files regarding conda and Python environment

## Future Work

There are many ways this work could be improved in the future, including but not limited to:
- Creating an OOT module to group together all pulsar-processing tools
- Filtering out frequency-specific interference by comparing variances of all channels and discarding noisy channels
- Creating a method of coherent (within a channel) dedispersion for these flowgraphs
- Improving efficiency of Python blocks by writing more efficient code (eg. replacing arrays with deques)
- Create tests for debugging
- Further documentation

## Acknowledgments

This project was developed as an MIT UROP (Undergraduate Research Opportunities Program) project, with this specific UROP assignment being a joint collaboration between the MIT Kavli Institute and the MIT Haystack Observatory.

This work would not be possible without the help from advisors Prof. Kiyoshi Masui of the Kavli Institute and Dr. John Swoboda of the Haystack Observatory. Additional help comes from Calvin Leung (Kavli), Alan Rogers (Haystack). This work builds upon previous work done by the contributors to the SRT.

The flowgraphs were tested using data collected from the Millstone Hill Incoherent Scatter Antenna.

The software developed in this program relies on GNU Radio developed by the GNU Radio Project, Digital RF created at the MIT Haystack Observatory, the Python signal processing tools (mitarspysigproc) created by John Swoboda, and the Python pulsar processing tools (psrdynspec) created by Akshay Suresh.
