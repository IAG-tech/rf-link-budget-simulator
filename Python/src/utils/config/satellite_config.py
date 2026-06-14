from dataclasses import dataclass
@dataclass
class SatelliteConfig:
    """
        Base configuration for satellite link budget calculations.

        Defines the RF system parameters common to all satellite scenarios
        (GEO, LEO, VLEO). Intended to be subclassed for scenario-specific
        geometry parameters.

        Parameters
        ----------
        name : str
            Scenario identifier (e.g. "UHF", "S-band", "LEO scenario").
        Ptx_dBm : float
            Transmitter output power in dBm.
        Gtx_dBi : float
            Transmit antenna gain in dBi.
        Grx_dBi : float
            Receive antenna gain in dBi.
        Ltx_dB : float
            Transmit side losses in dB (cable, connectors, filters).
        Lrx_dB : float
            Receive side losses in dB (cable, connectors, filters).
        Lextra_dB : float
            Additional fixed system losses in dB (implementation margin,
            pointing loss). For LEO scenarios, atmospheric losses are
            computed separately as a function of elevation angle.
        sensitivity_dBm : float
            Receiver sensitivity in dBm. Minimum detectable signal power.
        model : str
            Propagation model identifier (e.g. "fspl").
        """
    name: str
    Ptx_dBm: float
    Gtx_dBi: float
    Grx_dBi: float
    Ltx_dB: float
    Lrx_dB: float
    Lextra_dB: float
    sensitivity_dBm: float
    model: str


@dataclass
class LEOConfig(SatelliteConfig):
    """
        Configuration for LEO/VLEO satellite link budget scenarios.

        Extends SatelliteConfig with the Earth radius parameter required
        for orbital geometry calculations (slant range, elevation angle,
        pass duration, Doppler).

        Parameters
        ----------
        terrestrial_radio_Km : float
            Earth radius in km. Standard value: 6371 km.
        """
    terrestrial_radio_Km: float

@dataclass
class GEOConfig(SatelliteConfig):
    """
    Configuration for GEO satellite link budget scenarios.

    Extends SatelliteConfig with the geometry parameters specific
    to geostationary orbit.

    Parameters
    ----------
    terrestrial_radio_Km : float
        Earth radius in km. Standard value: 6371 km.
    geo_distance_Km : float
        Distance from Earth surface to GEO orbit in km.
        Standard GEO altitude: 35786 km.
    f_MHz : float
           Carrier frequency in MHz.
    """
    terrestrial_radio_Km: float
    geo_distance_Km: float
    f_MHz: float


