from src.linkbudget.compute_rx_power import compute_rx_power
from src.linkbudget.eirp import eirp
from src.propagation.shadowing.shadow_fading import shadow_fading
from src.utils.link_budget.link_margin import link_margin
from src.utils.geometry.zero_crossing_elevation import zero_crossing_elevation
from src.utils.geometry.orbital.slant_range import slant_range
from src.utils.geometry.orbital.atmosferic_losses_dB import atmosferic_losses_dB
from src.propagation.pathloss.fspl_leo import fspl_leo
from src.propagation.pathloss.fspl import fspl

def run_satellite(cfg,dist=None,slant_delta=None, f_MHz=None,elevation_deg=None, shadowing=False ):
    """
        Compute link margin and received power for satellite scenarios.

        Supports two scenario types determined by cfg.name:
        - GEO (UHF / S-band): static geometry, slant range computed from
          elevation angle sweep.
        - LEO/VLEO: dynamic geometry, parametric frequency, slant range and elevation pre-computed
          by elevation_vs_time() and passed as arrays.

        Parameters
        ----------
        cfg : GEOConfig or LEOConfig
            Satellite link budget configuration. Scenario type is inferred
            from cfg.name.
        dist : np.ndarray, optional
            Elevation angle array in degrees. Used in GEO scenario to compute
            slant range and find zero-crossing elevation.
        slant_delta : np.ndarray, optional
            Slant range array in km over the pass. Required for LEO/VLEO.
        f_MHz : float, optional
            Carrier frequency in MHz. Required for LEO/VLEO FSPL calculation.
        elevation_deg : np.ndarray, optional
            Elevation angle array in degrees over the pass. Used in LEO/VLEO
            to compute elevation-dependent atmospheric losses. If None,
            atmospheric losses default to 0.0 dB.
        shadowing : bool, optional
            If True, applies log-normal shadow fading to path loss.
            Default is False.

        Returns
        -------
        margin : np.ndarray
            Link margin in dB at each point.
        value0 : float or int
            GEO: elevation angle at which link margin crosses zero dB.
            LEO/VLEO: 0 (not applicable).
        rx_power : np.ndarray
            Received power in dBm at each point.

        Notes
        -----
        In LEO/VLEO scenarios, atmospheric losses are computed separately
        from Lextra_dB and subtracted from received power. Lextra_dB covers
        fixed system losses (cable, connectors, implementation margin).
        Atmospheric losses scale with 1/sin(elevation) and are computed by
        atmosferic_losses_dB().
        """
    if cfg.name == "UHF" or cfg.name == "S-band":
        distance = slant_range(cfg.terrestrial_radio_Km,cfg.geo_distance_Km , dist)
        path_loss = fspl(cfg, distance)
        eirp_value = eirp(cfg)
        rx_power = compute_rx_power(eirp_value, cfg, path_loss)
        margin = link_margin(rx_power, cfg)
        value0 = zero_crossing_elevation(margin, dist)
    else:
        if elevation_deg is not None:
            atm_losses = atmosferic_losses_dB(elevation_deg)
        else:
            atm_losses = 0.0

        path_loss = fspl_leo(f_MHz, slant_delta)
        if shadowing:
            path_loss = shadow_fading(path_loss,cfg)
        eirp_value = eirp(cfg)
        rx_power = compute_rx_power(eirp_value,cfg, path_loss) - atm_losses
        margin = link_margin(rx_power,cfg)
        value0 = 0

    return margin, value0, rx_power

