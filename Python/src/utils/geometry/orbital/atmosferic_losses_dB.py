import numpy as np
def atmosferic_losses(elevation,zenith_loss_dB=1.0):
    return zenith_loss_dB/np.sin(np.deg2rad(elevation))