from dataclasses import dataclass
@dataclass
class TerrestrialConfig:
    """
       Configuration for terrestrial propagation scenarios.

       Parameters
       ----------
       name : str
           Scenario identifier (e.g. "TETRA", "LTE1800").
       f_MHz : float
           Carrier frequency in MHz.
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
           Additional fixed system losses in dB (implementation margin).
       sensitivity_dBm : float
           Receiver sensitivity in dBm.
       model : str
           Propagation model identifier (e.g. "okumura_hata", "cost231").
       hb_m : float
           Base station antenna height in meters.
       hm_m : float
           Mobile antenna height in meters.
       scenario : str
           Environment type: 'urban', 'suburban', or 'rural'.
       city_type : str
           City classification for COST231: 'large' or 'medium_small'.
       """
    name: str
    f_MHz: float
    Ptx_dBm: float
    Gtx_dBi: float
    Grx_dBi: float
    Ltx_dB: float
    Lrx_dB: float
    Lextra_dB: float
    sensitivity_dBm: float
    model: str

    hb_m: float
    hm_m: float
    scenario: str  # 'urban', 'suburban', 'rural'
    city_type: str  # 'large', 'medium_small' (for COST231)




