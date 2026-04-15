from src.propagation.pathloss.okumura_hata import okumura_hata
from src.utils.config import TerrestrialConfig

tetra = TerrestrialConfig(
    # TETRA 400 MHz configuration parameters
    name = "TETRA",
    f_MHz = 400,   # Typical bands 380 - 385 MHz uplink, 390 - 395 MHz downlink

    hb_m= 30,      # Transmitter antenna height
    hm_m= 1.5,     # Receiver height

    Ptx_dBm= 44,   # 43 to 46 dBm
    Gtx_dBi= 6,    # 3 to 8 dBi
    Grx_dBi= 0,    # -2 to +2 dBi

    Ltx_dB = 2,    # wire, connectors, ....
    Lrx_dB=0,
    Lextra_dB= 10, # rural 0 to 5 dB, suburban 5 to 10 dB, urban 10 to 20 dB

    scenario = "urban",
    city_type = "large",
    model = "okumura-hata",

    sensitivity_dBm = -100 # 100 to -104 dBm

)
