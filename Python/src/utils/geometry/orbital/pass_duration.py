

def pass_duration(delta_max, omega):
    """
        Compute the duration of a satellite pass.

        The pass duration is the time the satellite is visible above
        the minimum operational elevation angle, derived from the
        maximum central angle and the orbital angular velocity.

        Parameters
        ----------
        delta_max : float
            Maximum central angle in radians, as returned by
            max_central_angle().
        omega : float
            Orbital angular velocity in rad/s, as returned by
            orbital_angular_speed().

        Returns
        -------
        float
            Pass duration in seconds.

        Notes
        -----
        Assumes a circular orbit and a zenith pass (satellite passes
        directly overhead). For off-zenith passes the actual duration
        is shorter — this value represents the maximum possible pass
        duration for a given altitude and minimum elevation angle.
        """
    T = 2 * delta_max / omega
    return T

