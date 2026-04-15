from src.utils.config import TerrestrialConfig

lte1800 = TerrestrialConfig(
    # LTE 1800 MHz configuration parameters
    name = "LTE1800",
    f_MHz = 1800,
    hb_m = 30,      # Transmitter antenna height
    hm_m = 1.5,     # Receiver height

    Ptx_dBm = 46,   # LTE macro 43 to 46 dBm, LTE micro 30 to 40
    Gtx_dBi = 15,   # small cells around 6 - 10 dBi , LTE macro base stations 15 to 18 dBi
    Grx_dBi = 0,

    Ltx_dB = 2,     # wire, connectors, ....
    Lrx_dB = 0,     #
    Lextra_dB = 10, # rural 0 to 5 dB, suburban 5 to 10 dB, urban 10 to 20 dB

    scenario = "urban",
    city_type = "large",
    model = "cost231",

    sensitivity_dBm = -95 # -90 to -100 dBm
)