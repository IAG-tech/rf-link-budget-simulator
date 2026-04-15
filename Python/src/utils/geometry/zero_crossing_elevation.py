import numpy as np
def zero_crossing_elevation(link_margin, elev_deg):
    """
    Finds the minimum elevation angle at which the link margin crosses 0 dB.

    Parameters
    ----------
    link_margin :
        Link margin values in dB as a function of elevation angle.
    elev_deg :
        Elevation angle vector in degrees (0.1° to 90°).

    Returns
    -------
    float
        Minimum operational elevation angle in degrees where link margin = 0 dB.
        Returns np.nan if link margin is negative across the full range (no coverage).
        Returns -1 if link margin is positive across the full range
        (coverage available at all elevation angles).

    """
    idx = np.where(link_margin > 0)[0]

    if len(idx) == 0:
        return np.nan
    elif len(idx) == len(link_margin):
        return -1
    else:
        i = idx[0]
        e1 = elev_deg[i-1]
        e2 = elev_deg[i]
        m1 = link_margin[i-1]
        m2 = link_margin[i]
        elev0 = np.interp(0,[m1,m2],[e1,e2])
        return elev0

