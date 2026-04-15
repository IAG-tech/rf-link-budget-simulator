import numpy as np
def print_coverage(name, value0,distance):
    """
    Prints a human-readable coverage summary for terrestrial scenarios.

    Parameters
    ----------
    name : str
        Scenario or technology name for display purposes.
    value0 : float
        Coverage distance in km where link margin crosses 0 dB.
        np.nan indicates coverage across the full range.
    distance :
        Distance vector in km used in the simulation.

    Output:
    ------
    Prints one of three messages:
    - Coverage available across the full range (value0 is NaN)
    - No coverage (value0 at or below minimum distance)
    - Coverage available until X km
    """
    if np.isnan(value0):
        print(f"{name}: Coverage available in all the range")
    elif value0 <= distance[0]:  #
        print(f"{name}: No coverage")
    else:
        print(f"{name}: Coverage available until {value0:.2f} km")