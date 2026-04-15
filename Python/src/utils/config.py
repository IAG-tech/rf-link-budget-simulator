from dataclasses import dataclass
@dataclass
class TechConfig:
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


@dataclass
class TerrestrialConfig(TechConfig):
    # Terrestrial values
    hb_m: float
    hm_m: float
    scenario: str  # 'urban', 'suburban', 'rural'
    city_type: str # 'large', 'medium_small' (for COST231)
@dataclass
class GeoConfig(TechConfig):
    # Satellite values
    terrestrial_radio_Km: float
    geo_distance_Km: float