#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: vlpannel
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
import pmt
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import epyblocks_test_epy_block_0 as epy_block_0  # embedded python block
import epyblocks_test_epy_block_1 as epy_block_1  # embedded python block
import epyblocks_test_epy_block_1_0 as epy_block_1_0  # embedded python block
import epyblocks_test_epy_block_2_0 as epy_block_2_0  # embedded python block
import mitarspysigproc.filtertools as filtert



from gnuradio import qtgui

class epyblocks_test(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "epyblocks_test")

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
        self.time = time = 60
        self.samp_rate = samp_rate = 1000000
        self.period = period = .0335028583
        self.filt_time = filt_time = 10
        self.dev = dev = 10
        self.channel = channel = 21

        ##################################################
        # Blocks
        ##################################################
        self._time_range = Range(0, 120, 1, 60, 200)
        self._time_win = RangeWidget(self._time_range, self.set_time, "'time'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._time_win)
        self._filt_time_range = Range(0, 120, 1, 10, 200)
        self._filt_time_win = RangeWidget(self._filt_time_range, self.set_filt_time, "'filt_time'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._filt_time_win)
        self._dev_range = Range(0, 100, 1, 10, 200)
        self._dev_win = RangeWidget(self._dev_range, self.set_dev, "'dev'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._dev_win)
        self._channel_range = Range(0, 31, 1, 21, 200)
        self._channel_win = RangeWidget(self._channel_range, self.set_channel, "'channel'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._channel_win)
        self.qtgui_vector_sink_f_0 = qtgui.vector_sink_f(
            1024,
            0,
            (1/1024),
            "Phase",
            "Power",
            "",
            2, # Number of inputs
            None # parent
        )
        self.qtgui_vector_sink_f_0.set_update_time(0.10)
        self.qtgui_vector_sink_f_0.set_y_axis((-140), 10)
        self.qtgui_vector_sink_f_0.enable_autoscale(False)
        self.qtgui_vector_sink_f_0.enable_grid(True)
        self.qtgui_vector_sink_f_0.set_x_axis_units("")
        self.qtgui_vector_sink_f_0.set_y_axis_units("")
        self.qtgui_vector_sink_f_0.set_ref_level(0)


        labels = ['Unfiltered', 'Filtered', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_vector_sink_f_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_vector_sink_f_0.set_line_label(i, labels[i])
            self.qtgui_vector_sink_f_0.set_line_width(i, widths[i])
            self.qtgui_vector_sink_f_0.set_line_color(i, colors[i])
            self.qtgui_vector_sink_f_0.set_line_alpha(i, alphas[i])

        self._qtgui_vector_sink_f_0_win = sip.wrapinstance(self.qtgui_vector_sink_f_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_vector_sink_f_0_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_1_win, 5, 0, 1, 1)
        for r in range(5, 6):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.pfb_decimator_ccf_0 = pfb.decimator_ccf(
            32,
            filtert.kaiser_coeffs(32),
            channel,
            100,
            True,
            True)
        self.pfb_decimator_ccf_0.declare_sample_delay(0)
        self.epy_block_2_0 = epy_block_2_0.filter_outlier_blk(samp_rate=samp_rate, time=filt_time, deviations=dev)
        self.epy_block_1_0 = epy_block_1_0.blk(period=period, samp_rate=1000000/32, integration_time=time)
        self.epy_block_1 = epy_block_1.blk(period=period, samp_rate=1000000/32, integration_time=time)
        self.epy_block_0 = epy_block_0.mod_drf_blk(data_dir=r"E:\pulsar\2022-05-26\usrp-rx0-r_20220526T200000_20220526T210800\rf_data", chan='misa-l2', repeat=False)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, (samp_rate * 1000000),True)
        self.blocks_tags_strobe_0 = blocks.tags_strobe(gr.sizeof_float*1, pmt.intern("TAG"), 100000, pmt.intern("strobe"))
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1024, 'C:\\Users\\vlpannel\\Desktop\\filtered', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1024, 'C:\\Users\\vlpannel\\Desktop\\unfiltered', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.epy_block_2_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_tags_strobe_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_throttle_0, 0), (self.pfb_decimator_ccf_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.epy_block_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.epy_block_1, 0), (self.qtgui_vector_sink_f_0, 0))
        self.connect((self.epy_block_1_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.epy_block_1_0, 0), (self.qtgui_vector_sink_f_0, 1))
        self.connect((self.epy_block_2_0, 0), (self.epy_block_1_0, 0))
        self.connect((self.pfb_decimator_ccf_0, 0), (self.blocks_complex_to_mag_squared_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "epyblocks_test")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time
        self.epy_block_1.integration_time = self.time
        self.epy_block_1_0.integration_time = self.time

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate((self.samp_rate * 1000000))
        self.epy_block_2_0.samp_rate = self.samp_rate
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)

    def get_period(self):
        return self.period

    def set_period(self, period):
        self.period = period
        self.epy_block_1.period = self.period
        self.epy_block_1_0.period = self.period

    def get_filt_time(self):
        return self.filt_time

    def set_filt_time(self, filt_time):
        self.filt_time = filt_time
        self.epy_block_2_0.time = self.filt_time

    def get_dev(self):
        return self.dev

    def set_dev(self, dev):
        self.dev = dev
        self.epy_block_2_0.deviations = self.dev

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        self.pfb_decimator_ccf_0.set_channel(int(self.channel))




def main(top_block_cls=epyblocks_test, options=None):

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
