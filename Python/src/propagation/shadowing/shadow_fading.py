import numpy as np
def shadow_fading(pl,cfg):
    """
   Applies log-normal shadow fading to a path loss vector
   The shadowing term is modelled as a zero-mean  Gaussian random variable
   in dB, with scenario-dependant standard deviation
    """
    match cfg.scenario:
        case "urban":
            sigma = 8,
        case "suburban":
            sigma = 6,
        case "rural":
            sigma = 4,
        case _:
            raise ValueError(f"Unknown scenario: {cfg.scenario}")

    shadow = sigma*np.random.randn(len(pl))
    pl_shadow = pl + shadow
    return pl_shadow
