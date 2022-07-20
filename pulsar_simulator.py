#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: vivelpanel
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, RangeWidget
from PyQt5 import QtCore
import numpy as np; import gr_digital_rf
import pulsar_simulator_pulse as pulse  # embedded python module



from gnuradio import qtgui

class pulsar_simulator(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "pulsar_simulator")

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
        self.time = time = 0
        self.samp_rate = samp_rate = 1e6
        self.per = per = .33
        self.off = off = .01
        self.f_off = f_off = .1e6
        self.center_freq = center_freq = 440e6

        ##################################################
        # Blocks
        ##################################################
        self._time_range = Range(0, 1, .01, 0, 200)
        self._time_win = RangeWidget(self._time_range, self.set_time, "'time'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._time_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            center_freq, #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.gr_digital_rf_digital_rf_sink_0 = gr_digital_rf.digital_rf_sink(
            "C:\\Users\vlpannel\Desktop\SRT\raw",
            channels=[
                'ch0',
            ],
            dtype=np.complex64,
            subdir_cadence_secs=3600,
            file_cadence_millisecs=1000,
            sample_rate_numerator=int(samp_rate),
            sample_rate_denominator=1,
            start=None,
            ignore_tags=False,
            is_complex=True,
            num_subchannels=2,
            uuid_str=None,
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
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 2)
        self.blocks_add_xx_2 = blocks.add_vcc(1)
        self.blocks_add_xx_1 = blocks.add_vcc(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_cc(0)
        self.analog_sig_source_x_0_4 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq + f_off), (pulse.pulsar(per, 5*off, time)), 0, 0)
        self.analog_sig_source_x_0_3_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq + (2*f_off)), (pulse.pulsar(per, 6*off, time)), 0, 0)
        self.analog_sig_source_x_0_3 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq - (3*f_off)), pulse.pulsar(per, off, time), 0, 0)
        self.analog_sig_source_x_0_2_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq + (3*f_off)), (pulse.pulsar(per, 7*off, time)), 0, 0)
        self.analog_sig_source_x_0_2 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq - (2*f_off)), (pulse.pulsar(per, 2*off, time)), 0, 0)
        self.analog_sig_source_x_0_1_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq + (4*f_off)), (pulse.pulsar(per, 8*off, time)), 0, 0)
        self.analog_sig_source_x_0_1 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq - f_off), (pulse.pulsar(per, 3*off, time)), 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq + (5*f_off)), (pulse.pulsar(per, 9*off, time)), 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, center_freq, (pulse.pulsar(per, 4*off, time)), 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, (center_freq - (4*f_off)), pulse.pulsar(per, 0, time), 0, 0)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 1, 55555)
        self.analog_fastnoise_source_x_0_2 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, .46, 0, 8192)
        self.analog_fastnoise_source_x_0_1 = analog.fastnoise_source_c(analog.GR_UNIFORM, 1, 9, 8192)
        self.analog_fastnoise_source_x_0_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, .77, 3872, 8192)
        self.analog_fastnoise_source_x_0 = analog.fastnoise_source_c(analog.GR_GAUSSIAN, 1, 234, 8192)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_fastnoise_source_x_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.analog_fastnoise_source_x_0_0, 0), (self.blocks_add_xx_1, 3))
        self.connect((self.analog_fastnoise_source_x_0_1, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.analog_fastnoise_source_x_0_2, 0), (self.blocks_add_xx_1, 2))
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_1, 4))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_2, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_2, 4))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_add_xx_2, 9))
        self.connect((self.analog_sig_source_x_0_1, 0), (self.blocks_add_xx_2, 3))
        self.connect((self.analog_sig_source_x_0_1_0, 0), (self.blocks_add_xx_2, 8))
        self.connect((self.analog_sig_source_x_0_2, 0), (self.blocks_add_xx_2, 2))
        self.connect((self.analog_sig_source_x_0_2_0, 0), (self.blocks_add_xx_2, 7))
        self.connect((self.analog_sig_source_x_0_3, 0), (self.blocks_add_xx_2, 1))
        self.connect((self.analog_sig_source_x_0_3_0, 0), (self.blocks_add_xx_2, 6))
        self.connect((self.analog_sig_source_x_0_4, 0), (self.blocks_add_xx_2, 5))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_2, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.gr_digital_rf_digital_rf_sink_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "pulsar_simulator")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_time(self):
        return self.time

    def set_time(self, time):
        self.time = time
        self.analog_sig_source_x_0.set_amplitude(pulse.pulsar(self.per, 0, self.time))
        self.analog_sig_source_x_0_0.set_amplitude((pulse.pulsar(self.per, 4*self.off, self.time)))
        self.analog_sig_source_x_0_0_0.set_amplitude((pulse.pulsar(self.per, 9*self.off, self.time)))
        self.analog_sig_source_x_0_1.set_amplitude((pulse.pulsar(self.per, 3*self.off, self.time)))
        self.analog_sig_source_x_0_1_0.set_amplitude((pulse.pulsar(self.per, 8*self.off, self.time)))
        self.analog_sig_source_x_0_2.set_amplitude((pulse.pulsar(self.per, 2*self.off, self.time)))
        self.analog_sig_source_x_0_2_0.set_amplitude((pulse.pulsar(self.per, 7*self.off, self.time)))
        self.analog_sig_source_x_0_3.set_amplitude(pulse.pulsar(self.per, self.off, self.time))
        self.analog_sig_source_x_0_3_0.set_amplitude((pulse.pulsar(self.per, 6*self.off, self.time)))
        self.analog_sig_source_x_0_4.set_amplitude((pulse.pulsar(self.per, 5*self.off, self.time)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_1_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_2_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_3.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_3_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_4.set_sampling_freq(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)

    def get_per(self):
        return self.per

    def set_per(self, per):
        self.per = per
        self.analog_sig_source_x_0.set_amplitude(pulse.pulsar(self.per, 0, self.time))
        self.analog_sig_source_x_0_0.set_amplitude((pulse.pulsar(self.per, 4*self.off, self.time)))
        self.analog_sig_source_x_0_0_0.set_amplitude((pulse.pulsar(self.per, 9*self.off, self.time)))
        self.analog_sig_source_x_0_1.set_amplitude((pulse.pulsar(self.per, 3*self.off, self.time)))
        self.analog_sig_source_x_0_1_0.set_amplitude((pulse.pulsar(self.per, 8*self.off, self.time)))
        self.analog_sig_source_x_0_2.set_amplitude((pulse.pulsar(self.per, 2*self.off, self.time)))
        self.analog_sig_source_x_0_2_0.set_amplitude((pulse.pulsar(self.per, 7*self.off, self.time)))
        self.analog_sig_source_x_0_3.set_amplitude(pulse.pulsar(self.per, self.off, self.time))
        self.analog_sig_source_x_0_3_0.set_amplitude((pulse.pulsar(self.per, 6*self.off, self.time)))
        self.analog_sig_source_x_0_4.set_amplitude((pulse.pulsar(self.per, 5*self.off, self.time)))

    def get_off(self):
        return self.off

    def set_off(self, off):
        self.off = off
        self.analog_sig_source_x_0_0.set_amplitude((pulse.pulsar(self.per, 4*self.off, self.time)))
        self.analog_sig_source_x_0_0_0.set_amplitude((pulse.pulsar(self.per, 9*self.off, self.time)))
        self.analog_sig_source_x_0_1.set_amplitude((pulse.pulsar(self.per, 3*self.off, self.time)))
        self.analog_sig_source_x_0_1_0.set_amplitude((pulse.pulsar(self.per, 8*self.off, self.time)))
        self.analog_sig_source_x_0_2.set_amplitude((pulse.pulsar(self.per, 2*self.off, self.time)))
        self.analog_sig_source_x_0_2_0.set_amplitude((pulse.pulsar(self.per, 7*self.off, self.time)))
        self.analog_sig_source_x_0_3.set_amplitude(pulse.pulsar(self.per, self.off, self.time))
        self.analog_sig_source_x_0_3_0.set_amplitude((pulse.pulsar(self.per, 6*self.off, self.time)))
        self.analog_sig_source_x_0_4.set_amplitude((pulse.pulsar(self.per, 5*self.off, self.time)))

    def get_f_off(self):
        return self.f_off

    def set_f_off(self, f_off):
        self.f_off = f_off
        self.analog_sig_source_x_0.set_frequency((self.center_freq - (4*self.f_off)))
        self.analog_sig_source_x_0_0_0.set_frequency((self.center_freq + (5*self.f_off)))
        self.analog_sig_source_x_0_1.set_frequency((self.center_freq - self.f_off))
        self.analog_sig_source_x_0_1_0.set_frequency((self.center_freq + (4*self.f_off)))
        self.analog_sig_source_x_0_2.set_frequency((self.center_freq - (2*self.f_off)))
        self.analog_sig_source_x_0_2_0.set_frequency((self.center_freq + (3*self.f_off)))
        self.analog_sig_source_x_0_3.set_frequency((self.center_freq - (3*self.f_off)))
        self.analog_sig_source_x_0_3_0.set_frequency((self.center_freq + (2*self.f_off)))
        self.analog_sig_source_x_0_4.set_frequency((self.center_freq + self.f_off))

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.analog_sig_source_x_0.set_frequency((self.center_freq - (4*self.f_off)))
        self.analog_sig_source_x_0_0.set_frequency(self.center_freq)
        self.analog_sig_source_x_0_0_0.set_frequency((self.center_freq + (5*self.f_off)))
        self.analog_sig_source_x_0_1.set_frequency((self.center_freq - self.f_off))
        self.analog_sig_source_x_0_1_0.set_frequency((self.center_freq + (4*self.f_off)))
        self.analog_sig_source_x_0_2.set_frequency((self.center_freq - (2*self.f_off)))
        self.analog_sig_source_x_0_2_0.set_frequency((self.center_freq + (3*self.f_off)))
        self.analog_sig_source_x_0_3.set_frequency((self.center_freq - (3*self.f_off)))
        self.analog_sig_source_x_0_3_0.set_frequency((self.center_freq + (2*self.f_off)))
        self.analog_sig_source_x_0_4.set_frequency((self.center_freq + self.f_off))
        self.qtgui_sink_x_0.set_frequency_range(self.center_freq, self.samp_rate)




def main(top_block_cls=pulsar_simulator, options=None):

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
