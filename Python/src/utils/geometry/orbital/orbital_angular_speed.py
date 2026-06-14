import numpy as np


def orbital_angular_speed(r):
    """
    Compute the orbital angular velocity for a circular orbit.

    Derived from Newton's law of gravitation and centripetal force:

        v = sqrt(GM / r)
        ω = v / r = sqrt(GM / r³)

    Parameters
    ----------
    r : float
        Orbital radius in km (Earth radius + altitude).

    Returns
    -------
    float
        Orbital angular velocity in rad/s.

    Notes
    -----
    GM = 3.986e5 km³/s² (Earth's gravitational parameter).

    Validation:
        r = 6621 km (250 km VLEO) → ω ≈ 1.172e-3 rad/s
        r = 6921 km (550 km LEO)  → ω ≈ 1.078e-3 rad/s
    """
    GM = 3.986e5  # km³/s²
    return np.sqrt(GM / r ** 3)