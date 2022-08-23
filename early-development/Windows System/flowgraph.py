#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# GNU Radio version: 3.10.3.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb
import flowgraph_epy_block_0 as epy_block_0  # embedded python block
import mitarspysigproc.filtertools as filtertools
import numpy as np



from gnuradio import qtgui

class flowgraph(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
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

        self.settings = Qt.QSettings("GNU Radio", "flowgraph")

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
        self.samp_rate = samp_rate = 1000000
        self.drf_data = drf_data = r"E:\pulsar\2022-05-26\usrp-rx0-r_20220526T200000_20220526T210800\rf_data"
        self.chan = chan = "misa-l2"

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)



        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])

        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)

        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.qwidget(), Qt.QWidget)

        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.pfb_channelizer_ccf_0 = pfb.channelizer_ccf(
            32,
            filtertools.kaiser_coeffs(32),
            1.0,
            100)
        self.pfb_channelizer_ccf_0.set_channel_map([])
        self.pfb_channelizer_ccf_0.declare_sample_delay(0)
        self.epy_block_0 = epy_block_0.blk(data_dir=r"E:\pulsar\2022-05-26\usrp-rx0-r_20220526T200000_20220526T210800\rf_data", chan='misa-l2', repeat=False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_file_sink_1_9 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch5', False)
        self.blocks_file_sink_1_9.set_unbuffered(False)
        self.blocks_file_sink_1_8 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch6', False)
        self.blocks_file_sink_1_8.set_unbuffered(False)
        self.blocks_file_sink_1_7 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch7', False)
        self.blocks_file_sink_1_7.set_unbuffered(False)
        self.blocks_file_sink_1_6 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch15', False)
        self.blocks_file_sink_1_6.set_unbuffered(False)
        self.blocks_file_sink_1_5 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch16', False)
        self.blocks_file_sink_1_5.set_unbuffered(False)
        self.blocks_file_sink_1_4 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch17', False)
        self.blocks_file_sink_1_4.set_unbuffered(False)
        self.blocks_file_sink_1_3 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch18', False)
        self.blocks_file_sink_1_3.set_unbuffered(False)
        self.blocks_file_sink_1_26 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch8', False)
        self.blocks_file_sink_1_26.set_unbuffered(False)
        self.blocks_file_sink_1_25 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch9', False)
        self.blocks_file_sink_1_25.set_unbuffered(False)
        self.blocks_file_sink_1_24 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch10', False)
        self.blocks_file_sink_1_24.set_unbuffered(False)
        self.blocks_file_sink_1_23 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch11', False)
        self.blocks_file_sink_1_23.set_unbuffered(False)
        self.blocks_file_sink_1_22 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch12', False)
        self.blocks_file_sink_1_22.set_unbuffered(False)
        self.blocks_file_sink_1_21 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch13', False)
        self.blocks_file_sink_1_21.set_unbuffered(False)
        self.blocks_file_sink_1_20 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch21', False)
        self.blocks_file_sink_1_20.set_unbuffered(False)
        self.blocks_file_sink_1_2 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch19', False)
        self.blocks_file_sink_1_2.set_unbuffered(False)
        self.blocks_file_sink_1_19 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch14', False)
        self.blocks_file_sink_1_19.set_unbuffered(False)
        self.blocks_file_sink_1_18 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch2', False)
        self.blocks_file_sink_1_18.set_unbuffered(False)
        self.blocks_file_sink_1_17 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch3', False)
        self.blocks_file_sink_1_17.set_unbuffered(False)
        self.blocks_file_sink_1_16 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch4', False)
        self.blocks_file_sink_1_16.set_unbuffered(False)
        self.blocks_file_sink_1_15 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch22', False)
        self.blocks_file_sink_1_15.set_unbuffered(False)
        self.blocks_file_sink_1_14 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch23', False)
        self.blocks_file_sink_1_14.set_unbuffered(False)
        self.blocks_file_sink_1_13 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch24', False)
        self.blocks_file_sink_1_13.set_unbuffered(False)
        self.blocks_file_sink_1_12 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch25', False)
        self.blocks_file_sink_1_12.set_unbuffered(False)
        self.blocks_file_sink_1_11 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch26', False)
        self.blocks_file_sink_1_11.set_unbuffered(False)
        self.blocks_file_sink_1_10_2_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch31', False)
        self.blocks_file_sink_1_10_2_0.set_unbuffered(False)
        self.blocks_file_sink_1_10_2 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch30', False)
        self.blocks_file_sink_1_10_2.set_unbuffered(False)
        self.blocks_file_sink_1_10_1 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch28', False)
        self.blocks_file_sink_1_10_1.set_unbuffered(False)
        self.blocks_file_sink_1_10_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch29', False)
        self.blocks_file_sink_1_10_0.set_unbuffered(False)
        self.blocks_file_sink_1_10 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch27', False)
        self.blocks_file_sink_1_10.set_unbuffered(False)
        self.blocks_file_sink_1_1 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch20', False)
        self.blocks_file_sink_1_1.set_unbuffered(False)
        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch1', False)
        self.blocks_file_sink_1_0.set_unbuffered(False)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, 'C:\\Users\\vlpannel\\Desktop\\newpfbdata\\ch0', False)
        self.blocks_file_sink_1.set_unbuffered(False)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.pfb_channelizer_ccf_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_waterfall_sink_x_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.pfb_channelizer_ccf_0, 1), (self.blocks_file_sink_1_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 20), (self.blocks_file_sink_1_1, 0))
        self.connect((self.pfb_channelizer_ccf_0, 27), (self.blocks_file_sink_1_10, 0))
        self.connect((self.pfb_channelizer_ccf_0, 29), (self.blocks_file_sink_1_10_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 28), (self.blocks_file_sink_1_10_1, 0))
        self.connect((self.pfb_channelizer_ccf_0, 30), (self.blocks_file_sink_1_10_2, 0))
        self.connect((self.pfb_channelizer_ccf_0, 31), (self.blocks_file_sink_1_10_2_0, 0))
        self.connect((self.pfb_channelizer_ccf_0, 26), (self.blocks_file_sink_1_11, 0))
        self.connect((self.pfb_channelizer_ccf_0, 25), (self.blocks_file_sink_1_12, 0))
        self.connect((self.pfb_channelizer_ccf_0, 24), (self.blocks_file_sink_1_13, 0))
        self.connect((self.pfb_channelizer_ccf_0, 23), (self.blocks_file_sink_1_14, 0))
        self.connect((self.pfb_channelizer_ccf_0, 22), (self.blocks_file_sink_1_15, 0))
        self.connect((self.pfb_channelizer_ccf_0, 4), (self.blocks_file_sink_1_16, 0))
        self.connect((self.pfb_channelizer_ccf_0, 3), (self.blocks_file_sink_1_17, 0))
        self.connect((self.pfb_channelizer_ccf_0, 2), (self.blocks_file_sink_1_18, 0))
        self.connect((self.pfb_channelizer_ccf_0, 14), (self.blocks_file_sink_1_19, 0))
        self.connect((self.pfb_channelizer_ccf_0, 19), (self.blocks_file_sink_1_2, 0))
        self.connect((self.pfb_channelizer_ccf_0, 21), (self.blocks_file_sink_1_20, 0))
        self.connect((self.pfb_channelizer_ccf_0, 13), (self.blocks_file_sink_1_21, 0))
        self.connect((self.pfb_channelizer_ccf_0, 12), (self.blocks_file_sink_1_22, 0))
        self.connect((self.pfb_channelizer_ccf_0, 11), (self.blocks_file_sink_1_23, 0))
        self.connect((self.pfb_channelizer_ccf_0, 10), (self.blocks_file_sink_1_24, 0))
        self.connect((self.pfb_channelizer_ccf_0, 9), (self.blocks_file_sink_1_25, 0))
        self.connect((self.pfb_channelizer_ccf_0, 8), (self.blocks_file_sink_1_26, 0))
        self.connect((self.pfb_channelizer_ccf_0, 18), (self.blocks_file_sink_1_3, 0))
        self.connect((self.pfb_channelizer_ccf_0, 17), (self.blocks_file_sink_1_4, 0))
        self.connect((self.pfb_channelizer_ccf_0, 16), (self.blocks_file_sink_1_5, 0))
        self.connect((self.pfb_channelizer_ccf_0, 15), (self.blocks_file_sink_1_6, 0))
        self.connect((self.pfb_channelizer_ccf_0, 7), (self.blocks_file_sink_1_7, 0))
        self.connect((self.pfb_channelizer_ccf_0, 6), (self.blocks_file_sink_1_8, 0))
        self.connect((self.pfb_channelizer_ccf_0, 5), (self.blocks_file_sink_1_9, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "flowgraph")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)

    def get_drf_data(self):
        return self.drf_data

    def set_drf_data(self, drf_data):
        self.drf_data = drf_data

    def get_chan(self):
        return self.chan

    def set_chan(self, chan):
        self.chan = chan




def main(top_block_cls=flowgraph, options=None):

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
