import numpy as np

def max_central_angle(min_elevation_deg,r,R):
    """
        Compute the maximum central angle of a satellite pass.

        The central angle is the angle at the Earth's center between the
        ground station and the satellite's position. The maximum central
        angle corresponds to the minimum operational elevation angle and
        defines the half-width of the visible arc.

        Parameters
        ----------
        min_elevation_deg : float
            Minimum operational elevation angle in degrees.
        r : float
            Orbital radius in km (Earth radius + altitude).
        R : float
            Earth radius in km. Standard value: 6371 km.

        Returns
        -------
        float
            Maximum central angle in radians.

        Notes
        -----
        Derived from the law of sines applied to the Earth-satellite-
        ground station triangle:

            delta_max = arccos(R/r · cos(el_min)) - el_min
        """

    delta_max = np.arccos(R / r * np.cos(np.deg2rad(min_elevation_deg))) - np.deg2rad(min_elevation_deg)
    return delta_max
