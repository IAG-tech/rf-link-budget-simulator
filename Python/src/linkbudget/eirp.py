def eirp(cfg):
    """
    Effective Isotropic Radiated Power, Measured in dBm. Uses formula:

    EIRP = Ptx_dB +Gtx_dBi - Ltx_dB

    """
    eirp_value = cfg.Ptx_dBm + cfg.Gtx_dBi - cfg.Ltx_dB

    return eirp_value