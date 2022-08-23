# this module will be imported in the into your flowgraph

def pulsar(period, offset, time):
    return int((time - offset) % period <= .01) * .2
