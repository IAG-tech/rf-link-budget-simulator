def orbital_radius(altitude_km,R):
    """
        Compute the orbital radius of a satellite.

        Parameters
        ----------
        altitude_km : float
            Orbital altitude above Earth's surface in km.
        R : float
            Earth radius in km. Standard value: 6371 km.

        Returns
        -------
        float
            Orbital radius in km (Earth center to satellite).
        """
    r = altitude_km + R
    return r