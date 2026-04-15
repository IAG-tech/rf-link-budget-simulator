from dataclasses import dataclass
@dataclass
class SatelliteConfig:
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
    # LEO-VLEO Satellite values
    terrestrial_radio_Km: float

