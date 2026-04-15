from src.propagation.pathloss.fspl import fspl
from src.propagation.pathloss.okumura_hata import okumura_hata
from src.propagation.pathloss.cost231 import cost231
def dispatcher(model,config,dist ):
    """

    Selects and executes appropriate path loss model.

    Parameters
    ----------
    model : str
        Propagation model identifier. Supported values:
        - "fspl"         : Free Space Path Loss
        - "okumura-hata" : Okumura-Hata (valid 150–1500 MHz)
        - "cost231"      : COST231-Hata (valid 1500–2000 MHz)
    config : TerrestrialConfig | GeoConfig
        Scenario configuration dataclass.
    dist :
        Distance or elevation angle vector depending on scenario.

    Returns
    -------
    pathloss:
        Path loss values in dB.

    Raises
    ------
    ValueError
        If model identifier is not recognised.

    """
    match model:
        case "fspl":
            pathloss = fspl(config,dist)
        case "okumura-hata":
            pathloss = okumura_hata(config,dist)
        case "cost231":
            pathloss = cost231(config,dist)
        case _:
            raise ValueError(f"Unknown model: {model}")
    return pathloss

