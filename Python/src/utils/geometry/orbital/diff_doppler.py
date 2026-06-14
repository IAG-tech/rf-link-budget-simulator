import numpy as np

def diff_doppler(doppler_f_KHz, t):
    """
        Compute the Doppler rate (frequency rate of change) over a satellite pass.

        Calculates the time derivative of the Doppler shift using finite differences.

        Parameters
        ----------
        doppler_f_KHz : np.ndarray
            Doppler shift array in kHz over the satellite pass.
        t : np.ndarray
            Time array in seconds corresponding to doppler_f_KHz.
            Must have the same length as doppler_f_KHz.

        Returns
        -------
        np.ndarray
            Doppler rate in Hz/s. Same length as input arrays.
            Last element is repeated to maintain array length after np.diff.

        Notes
        -----
        The maximum Doppler rate occurs at the point of closest approach
        (maximum elevation), not at the horizon.

        For a VLEO pass at 250 km altitude, typical peak Doppler rate
        is ~700 Hz/s, compared to ~60 Hz/s for a zenith pass — making
        off-zenith rasante passes the dimensioning case for receiver design.
        """
    diff = np.diff(doppler_f_KHz)
    doppler_array = np.append(diff,diff[-1])
    doppler_rate = 1000 * doppler_array / (t[1] - t[0])
    return doppler_rate