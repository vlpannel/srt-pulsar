# this module will be imported in the into your flowgraph

"""
This code generates the names of the files that store each channel output.
"""

def name(num):
    return '/Users/vivelpanel/Desktop/SRT UROP 2022/Spectrogram/channels/created_channel_' + str(num)

# will finish below code later--for now it is much more complicated
# than necessary, so I use the simpler scheme above
"""
class ChannelFile:
    filepath = '/Users/vivelpanel/Desktop/SRT UROP 2022/Spectrogram/channels/'
    basename = 'created_channel_'
    index = 0

    def __init__(self, num=index):
        self.filename = filepath + basename + str(num)
        if num == index:
            index += 1

    def get_name(self, num):
        if 
        return self.filename
"""
