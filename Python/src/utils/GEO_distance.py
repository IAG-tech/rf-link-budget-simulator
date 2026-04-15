import numpy as np
def geo_distance(cfg, angle):
    """
    Calculates the slant range between ground station and GEO satellite
    as afunction of elevation angle.

    Uses the quadratic form of the law of cosines:
    d ^ 2 + 2 * r * sin(e) * d + (r ^ 2 - (r + g) ^ 2) = 0

    Solved for the positive root:
        d = -r * sin(e) + sqrt(r ^ 2 * sin ^ 2(e) - r ^ 2 + (r + g) ^ 2)

    Where:
        r = Earth radius(km)
        g = GEO orbital altitude(km), so r + g = orbital radius
        e = elevation angle(degrees), we need to convert to radians

    Validation:
        elevation 90 deg -> 35,786km
        elevation  5 deg -> 41,121km
    """
    d = -cfg.terrestrial_radio_Km * np.sin(np.deg2rad(angle)) + np.sqrt(cfg.terrestrial_radio_Km ** 2 * (np.sin(np.deg2rad(angle))) ** 2 - cfg.terrestrial_radio_Km ** 2 + (cfg.terrestrial_radio_Km + cfg.geo_distance_Km) ** 2)
    return d
