
from src.linkbudget.compute_rx_power import compute_rx_power
from src.linkbudget.eirp import eirp
from src.propagation.shadowing.shadow_fading import shadow_fading
from src.utils.link_budget.link_margin import link_margin
from src.utils.geometry.zero_crossing_distance import zero_crossing_distance
from src.utils.geometry.zero_crossing_elevation import zero_crossing_elevation
from src.utils.geometry.orbital.GEO_distance import geo_distance
from src.propagation.pathloss.fspl_leo import fspl_leo
from src.propagation.pathloss.fspl import fspl


def run_satellite(cfg, dist, slant_delta, f_MHz=None, shadowing=False ):
    if cfg.name == "UHF" or cfg.name == "S-band":
        distance = geo_distance(cfg, dist)
        path_loss = fspl(cfg, distance)
        eirp_value = eirp(cfg)
        rx_power = compute_rx_power(eirp_value, cfg, path_loss)
        margin = link_margin(rx_power, cfg)
        value0 = zero_crossing_elevation(margin, dist)
    else:

        path_loss = fspl_leo(f_MHz, slant_delta)
        if shadowing:
            path_loss = shadow_fading(path_loss,cfg)
        eirp_value = eirp(cfg)
        rx_power = compute_rx_power(eirp_value,cfg, path_loss)
        margin = link_margin(rx_power,cfg)
        value0 = zero_crossing_distance(margin, dist)

    return margin, value0, rx_power

