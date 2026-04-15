import numpy as np
def print_coverage_geo(name, value0):
    """
    Prints a human-readable coverage summary for GEO satellite scenarios.

    Parameters
    ----------
    name : str
        Scenario or band name for display purposes.
    value0 : float
        Minimum operational elevation angle in degrees where link margin = 0 dB.
        np.nan indicates no coverage at any elevation angle.
        -1 indicates coverage available at all elevation angles.

    Output
    ------
    Prints one of three messages:
    - No coverage at any elevation angle (value0 is NaN)
    - Coverage available at all elevation angles (value0 is -1)
    - Coverage available above X degrees

    """
    if np.isnan(value0):
        print(f"{name}: No coverage in any elevation angle")
    elif value0 == -1:
        print(f"{name}: Coverage available at all elevation angles")
    else:
        print(f"{name}: Coverage available above {value0:.2f}°")