import numpy as np

def doppler(f_MHz, omega , r, t):
    """
     Compute the Doppler shift over a satellite pass.

     Calculates the instantaneous Doppler frequency shift as a function
     of time, based on the radial component of the orbital velocity
     relative to the ground station.

     Parameters
     ----------
     f_MHz : float
         Carrier frequency in MHz.
     omega : float
         Orbital angular velocity in rad/s.
     r : float
         Orbital radius (Earth radius + altitude) in km.
     t : np.ndarray
         Time array in seconds, centered at zero at closest approach
         (maximum elevation).

     Returns
     -------
     np.ndarray
         Doppler shift in kHz. Positive when satellite approaches,
         negative when receding, zero at closest approach.

     Notes
     -----
     The radial velocity is derived from the orbital velocity projected
     onto the line of sight between satellite and ground station:

         v_orbital = omega * r
         v_radial  = v_orbital * sin(omega * t)

     Speed of light assumed: 3e5 km/s.
     """
    v_orbital = omega * r
    delta_signed = -omega * t
    v_radial = v_orbital * np.sin(delta_signed)
    f_doppler_kHz = ((f_MHz* 1e3) * v_radial )/ 3e5
    return f_doppler_kHz