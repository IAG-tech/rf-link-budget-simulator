import numpy as np
def height_correction(cfg):
    """
Height correction function
depending on the city type returns a different value
for correction factor

Inputs:
    cfg             Configuration structure containing:
                            - f_MHz Carrier frequency(MHz)
                            - h_rx_m Receiver antenna height(m)

    city_type       City size for the correction factor ("large", "medium", "small")

Outputs:
    correction      correction value for Okumura - Hata model
        """

# -------------------- Scenario election - ---------------
# Computes correction for Okumura - Hata model depending on scenario
    match cfg.city_type:
        case "large":
            if cfg.f_MHz <= 300:
                correction = 8.29 * (np.log10(1.54 * cfg.hm_m)) ** 2 - 1.1
            else:
                correction = 3.2 * (np.log10(11.75 * cfg.hm_m)) ** 2 - 4.97
        case "medium", "small":
            correction = (1.1 * np.log10(cfg.f_MHz) - 0.7) * cfg.hm_m - (1.56 * np.log10(cfg.f_MHz) - 0.8)
        case _:
            raise ValueError("Unknown city type")
    return correction

