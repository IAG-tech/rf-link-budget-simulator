import numpy as np

def slant_range(r, h, elevation_deg):
    """
    Compute slant range between ground station and satellite
    as a function of elevation angle.

    Uses the quadratic form of the law of cosines applied to the
    Earth-satellite-ground station triangle:

        d² + 2·r·sin(e)·d + (r² - (r+h)²) = 0

    Solved for the positive root:

        d = -r·sin(e) + sqrt(r²·sin²(e) - r² + (r+h)²)

    Parameters
    ----------
    r : float
        Earth radius in km. Standard value: 6371 km.
    h : float
        Orbital altitude in km (e.g. 35786 km for GEO, 250 km for VLEO).
    elevation_deg : float or np.ndarray
        Elevation angle(s) in degrees.

    Returns
    -------
    float or np.ndarray
        Slant range in km.

    Notes
    -----
    Validated against analytical values:
        elevation 90° → 35786 km (GEO)
        elevation  5° → 41121 km (GEO)
    """
    e = np.deg2rad(elevation_deg)
    d = -r * np.sin(e) + np.sqrt(r**2 * np.sin(e)**2 - r**2 + (r + h)**2)
    return d