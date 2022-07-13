#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: DRF To File
# Author: vivelpanel
# GNU Radio version: 3.9.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import gr_digital_rf
import numpy as np; import gr_digital_rf



from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "DRF To File", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("DRF To File")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.source_directory = source_directory = '/Volumes/NO NAME/pulsar/2022-05-26/rf_data'
        self.samp_rate = samp_rate = 32000
        self.drfsink_directory = drfsink_directory = "/Users/vivelpanel/Desktop/SRT UROP 2022/Testing DRF Scripts/rtl-output/2xDrfout"

        ##################################################
        # Blocks
        ##################################################
        self.gr_digital_rf_digital_rf_source_0 = gr_digital_rf.digital_rf_source(
            source_directory,
            channels=[
                'misa-l2',
            ],
            start=[
                int(1653595200000000),
            ],
            end=[
                int(1653595299999999),
            ],
            repeat=True,
            throttle=False,
            gapless=False,
            min_chunksize=None,
        )
        self.gr_digital_rf_digital_rf_sink_0 = gr_digital_rf.digital_rf_sink(
            drfsink_directory,
            channels=[
                'ch0',
            ],
            dtype=np.int16,
            subdir_cadence_secs=3600,
            file_cadence_millisecs=1000,
            sample_rate_numerator=int(samp_rate),
            sample_rate_denominator=1,
            start=0,
            ignore_tags=False,
            is_complex=False,
            num_subchannels=1,
            uuid_str='adsf',
            center_frequencies=(
                None
            ),
            metadata={},
            is_continuous=True,
            compression_level=0,
            checksum=False,
            marching_periods=True,
            stop_on_skipped=False,
            stop_on_time_tag=False,
            debug=False,
            min_chunksize=None,
        )
        self.blocks_vector_to_streams_0 = blocks.vector_to_streams(gr.sizeof_short*1, 2)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_short*1, samp_rate,True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_short*1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_short*1, '/Users/vivelpanel/Desktop/SRT UROP 2022/Testing DRF Scripts/rtl-output/source_block_output', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.gr_digital_rf_digital_rf_sink_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 1), (self.blocks_null_sink_0, 0))
        self.connect((self.blocks_vector_to_streams_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.gr_digital_rf_digital_rf_source_0, 0), (self.blocks_vector_to_streams_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_source_directory(self):
        return self.source_directory

    def set_source_directory(self, source_directory):
        self.source_directory = source_directory

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_drfsink_directory(self):
        return self.drfsink_directory

    def set_drfsink_directory(self, drfsink_directory):
        self.drfsink_directory = drfsink_directory




def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
