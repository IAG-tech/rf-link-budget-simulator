import numpy as np
def atmosferic_losses_dB(elevation,zenith_loss_dB=1.0):
    """
        Compute atmospheric path loss as a function of elevation angle.

        Losses scale with 1/sin(elevation),
        reflecting the longer atmospheric path at low
        elevation angles relative to zenith.

        Parameters
        ----------
        elevation : float or np.ndarray
            Elevation angle(s) in degrees. Should be clipped to [el_min, 90]
            before calling this function to avoid numerical singularity at 0°.
        zenith_loss_dB : float, optional
            Atmospheric loss at zenith (90° elevation) in dB. Default is 1.0 dB,
            typical for S-band under clear sky conditions.

        Returns
        -------
        float or np.ndarray
            Atmospheric path loss in dB.

        Notes
        -----
        At low elevation angles the atmospheric path length increases significantly:
            el = 90° → loss = zenith_loss_dB (minimum)
            el = 30° → loss = 2 × zenith_loss_dB
            el =  5° → loss ≈ 11.5 × zenith_loss_dB

        This model is a first-order approximation. The rigorous standard for
        Earth-space links is ITU-R P.618, which accounts for frequency,
        geographic location and rainfall attenuation.
        """
    return zenith_loss_dB/np.sin(np.deg2rad(elevation))