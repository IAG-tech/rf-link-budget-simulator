import numpy as np
def cost231(cfg, dist ):

    """
  COST-HATA propagation model
  
    Computes path loss using Cost-Hata empirical model.
  
  
    Inputs:
       d_Km       Distance(km) [scalar or vector]
       cfg        Configuration structure containing:
                      - f_MHz    Carrier frequency (MHz)
                      - hb_m   Base station antenna height (m)
                      - hm_m   Receiver antenna height (m)
       scenario   Environment type ("Urban","Suburban","rural")
  
  
    Output:
       cost    Path Loss (dB)

    Limitations
       Frequency:               1500-2000MHz
       Receiver antenna height: 1-10m
       Base antenna height:     30-200m
       Distance:                1-20km
        """

   # ----------- correction factor ---------
   # Mobile antenna height correction depending on scenario

    match cfg.scenario:
        case "urban":
            if cfg.f_MHz >=150 & cfg.f_MHz <= 200:
                correction = 8.29*(np.log10(1.54*cfg.hm_m))**2-1.1
                const = 3
            elif cfg.f_MHz >200 & cfg.f_MHz < 2000:
                correction = 3.2 * (np.log10(11.75* cfg.hm_m)) ** 2 - 4.97
                const = 3
            else:
                raise ValueError("Wrong frequency")
        case {"suburban":"rural"}:
            correction = (1.1*np.log10(cfg.f_MHz)-0.7)*cfg.hm_m-(1.56*np.log10(cfg.f_MHz)-0.8)
            const = 0
        case _:
            raise ValueError(f"Unknown scenario: {cfg.scenario}")

    # ----------- Calculation --------
    cost = 46.3 +33.9*np.log10(cfg.f_MHz) - 13.82*np.log10(cfg.hb_m) -correction + (44.9 - 6.55*np.log10(cfg.hb_m))*np.log10(dist) + const
    return cost