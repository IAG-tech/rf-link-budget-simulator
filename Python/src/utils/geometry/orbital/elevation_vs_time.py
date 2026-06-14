import numpy as np
def elevation_vs_time(T, omega, r, R, el_min_deg=5.0):
    """
        Compute slant range and elevation angle over a satellite pass.

        Calculates the geometry of a satellite pass from first visibility
        to last visibility, centered at closest approach (t=0).

        Parameters
        ----------
        T : float
            Total pass duration in seconds.
        omega : float
            Orbital angular velocity in rad/s.
        r : float
            Orbital radius (Earth radius + altitude) in km.
        R : float
            Earth radius in km. Standard value: 6371 km.
        el_min_deg : float, optional
            Minimum elevation angle in degrees. Elevation is clipped to this
            value at the edges of the pass to avoid numerical singularity at
            0° and to reflect the minimum operational elevation of the ground
            station. Default is 5.0°.

        Returns
        -------
        list of np.ndarray
            [t, slant_delta, el_t] where:
            - t : time array in seconds, centered at zero at closest approach.
            - slant_delta : slant range in km at each time step.
            - el_t : elevation angle in degrees, clipped to [el_min_deg, 90].

        Notes
        -----
        The elevation angle is derived from the law of cosines applied to the
        Earth-satellite-ground station triangle:

            slant² = r² + R² - 2·R·r·cos(omega·|t|)
            el = arcsin((r² - R² - slant²) / (2·R·slant))

        Elevation is clipped to el_min_deg at both ends of the pass. This
        ensures consistency between the elevation plot and the link margin
        calculation, where atmospheric losses are computed as a function of
        the same elevation array.
        """
    t = np.linspace(-T/2, T/2,int(T) )
    delta_t = omega * np.abs(t)
    slant_delta = np.sqrt(r**2 + R**2 -2*R*r*np.cos(delta_t))
    el_t = np.rad2deg(np.arcsin((r**2 - R**2 - slant_delta**2) / (2 * R * slant_delta)))
    el_t = np.clip(el_t, el_min_deg, 90)
    return [t,slant_delta,el_t]
