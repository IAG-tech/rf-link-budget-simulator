from src.utils.config.satellite_config import LEOConfig

leo_optimistic_config = LEOConfig(

    name = "LEO scenario",

    terrestrial_radio_Km = 6371,  # Earth radius (km)

    Ptx_dBm = 30,  # 27 to 33 dBm small satellite
    Gtx_dBi = 6,  # 0 to 6 dBi omnidirectional antennas
    Grx_dBi = 20,  # 20 to 30 dBi parabolic

    Ltx_dB = 0,
    Lrx_dB = 0,
    Lextra_dB = 2,
    model = "fspl",
    sensitivity_dBm = -120,  # -100 to -120 dBm
)