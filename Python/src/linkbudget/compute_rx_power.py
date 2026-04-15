
def compute_rx_power(eirp,cfg, pl):
    """

    Pr is the received power at the receiver (dBm)
    Uses formula:
    Pr = EIRP + Grx_dBi - Lrx_dB - Lextra_dB - PL

        EIRP       Effective Isotropic Radiated Power. Measured in dBm.

        Grx_dBi    Gain of the receiver antenna. Measured in dBi

        Lrx_dB     Losses of the receiver. Measured in dB
        Lextra_dB  Additional fixed losses. Measured in dB

        PL         Propagation path loss. Measured in dB
"""
#  ------- Calculation -------

    pr = eirp + cfg.Grx_dBi - cfg.Lrx_dB - cfg.Lextra_dB - pl

    return pr