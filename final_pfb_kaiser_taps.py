import mitarspysigproc.filtertools as ft
import numpy as np

x = 5 # FOR DEBUG

def taps(chans):
    """
    Returns PFB taps for Kaiser windowing using filtertools.

    Parameters
    ----------
    chans : int
        Number of channels that PFB will yield

    Returns
    -------
    taps : vector
        Filter taps for PFB as a real vector
    """
    taps = np.reshape(ft.kaiser_coeffs(chans), -1)
    return taps
