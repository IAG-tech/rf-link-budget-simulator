import numpy as np
def fspl(cfg, dist):
    """
    FSPL Free Space Path Loss (dB)

    FSPL_dB = fspl (f_MHz, d_Km)
    f_MHz: Frequency in MHz
    d_Km: Distance in Km (can be scalar or vector)
    Uses formula:
       FSPL(dB) = 32.44 + 20*log10(f_MHz) + 20*log10(d_Km)

    Assumes far-field, free space conditions
    """
    # ------------ Calculation -----------
    fspl = 32.44 + 20*np.log10(cfg.f_MHz) + 20*np.log10(dist)
    return fspl
