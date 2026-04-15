from src.utils.config import GeoConfig

"""
   S-band GEO satellite configuration
   Represents a small satellite downlink scenario
   Frequency: 2 GHz (S-band, typical Earth observation missions)
   Ground station: small parabolic dish (30 dBi)
"""

Sband = GeoConfig(



    name = "S-band",
    f_MHz = 2000,    # Frequency of S-band

    geo_distance_Km = 35786,    # GEO orbital altitude (km), so r+g = orbital radius
    terrestrial_radio_Km = 6371,# Earth radius (km)

    Ptx_dBm = 37,               # 30 to 37 dBm small satellite
    Gtx_dBi = 6,                # 0 to 6 dBi omnidirectional antennas
    Grx_dBi = 30,               # 20 to 30 dBi parabolic

    Ltx_dB = 0,
    Lrx_dB = 0,
    Lextra_dB = 1,  # Atmospheric losses
    model = "fspl",
    sensitivity_dBm = -120 # -100 to -120 dBm
)