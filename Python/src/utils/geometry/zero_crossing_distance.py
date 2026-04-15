import numpy as np
def zero_crossing_distance(link_margin, dist):
    """
    ZERO CROSSING DISTANCE (Km)

        Computes the distance at which the link margin crosses 0dB threshold


        Inputs:
            link_margin       Link margin vector (dB)
            d_Km              Distance vector (Km)

        Outputs:
            d0                Distance where link margin equals 0dB

        Interpretation:
            link_margin > 0dB Coverage available
            link_margin = 0dB Coverage threshold
            link_margin < 0dB Coverage unavailable

    """
    idx = np.where(link_margin <= 0)[0]

    if len(idx) == 0 :
        return np.nan

    elif idx[0] == 0:
        return dist[0]

    else:
        i = idx[0]
        d1 = dist[i-1]
        d2 = dist[i]
        m1 = link_margin[i-1]
        m2 = link_margin[i]
        d0 = np.interp(0, [m1, m2], [d1, d2])
        return d0