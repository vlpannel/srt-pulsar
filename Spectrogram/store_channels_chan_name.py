# this module will be imported in the into your flowgraph

"""
This code generates the names of the files that store each channel output.
"""

class ChannelFile:
    basename = 'created_channel_'
    index = 0

    def __init__(self):
        self.filename = basename + str(index)
        index += 1

    def get_name(self):
        return self.filename
