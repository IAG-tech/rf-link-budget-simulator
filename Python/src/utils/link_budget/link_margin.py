def link_margin(pr, cfg):
    """
    LINK MARGIN(dB)

    Computes the link margin as the difference between receiver power
    and receiver sensitivity

    Inputs:
        Pr      Received power(dBm)
        cfg     Configuration structure containing:
                    - sensitivity_dBm Receiver sensitivity(dBm)
    Output:
        link Link margin(dB)

    Interpretation:
        link > 0 dB sufficient signal level
        link = 0 dB coverage threshold
        link < 0 dB insufficient signal level

    Link margin can be used to estimate coverage probability when
    combined with random fading (Monte Carlo simulations).
    """

    link = pr - cfg.sensitivity_dBm
    return link