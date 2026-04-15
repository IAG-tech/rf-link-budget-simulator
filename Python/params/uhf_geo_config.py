from src.utils.config import GeoConfig

"""
    UHF GEO satellite configuration
    Represents a small satellite TT&C (Telemetry, Tracking and Command) link
    Frequency: 400 MHz (UHF, typical for satellite command and telemetry)
    Ground station: Yagi antenna (13 dBi)
"""
uhf = GeoConfig(

    name = "UHF",
    f_MHz = 400,    # Frequency of UHF

    geo_distance_Km = 35786,    # GEO orbital altitude (km), so r+g = orbital radius
    terrestrial_radio_Km = 6371,# Earth radius (km)

    Ptx_dBm = 37,   # 30 to 37 dBm small satellite
    Gtx_dBi = 6,    # 0 to 6 dBi omnidirectional antennas
    Grx_dBi = 13,   # 10 to 15 Yagui antennas

    Ltx_dB = 0,
    Lrx_dB = 0,
    Lextra_dB = 0,  # Atmospheric losses
    model = "fspl",

    sensitivity_dBm = -120 # -100 to -120 dBm
)