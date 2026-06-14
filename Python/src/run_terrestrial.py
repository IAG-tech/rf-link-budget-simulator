from src.propagation.dispatcher import dispatcher
from src.linkbudget.compute_rx_power import compute_rx_power
from src.linkbudget.eirp import eirp
from src.propagation.shadowing.shadow_fading import shadow_fading
from src.utils.link_budget.link_margin import link_margin
from src.utils.geometry.zero_crossing_distance import zero_crossing_distance


def run_terrestrial(cfg, dist, model=None, shadowing=False):
    """
        Runs the terrestrial RF link budget simulation.

        Computes path loss using the selected propagation model, optionally adds
        log-normal shadowing, and returns the link margin and received power
        over a range of distances.

        Args:
            cfg (TerrestrialConfig): System configuration — frequency, TX power,
                antenna gains, losses, sensitivity, propagation model parameters.
            dist (np.ndarray): Distance vector in km.
            model (str, optional): Propagation model override. If None, uses cfg.model.
                Supported: 'fspl', 'okumura_hata', 'cost231'.
            shadowing (bool): If True, adds log-normal shadowing on top of path loss.

        Returns:
            margin (np.ndarray): Link margin in dB for each distance value.
                Positive = viable link, negative = insufficient signal.
            value0 (float): Distance in km where link margin crosses zero —
                maximum coverage range.
            rx_power (np.ndarray): Received power in dBm for each distance value.
        """

    model_to_use = model if model else cfg.model
    path_loss = dispatcher(model_to_use, cfg, dist)
    if shadowing:
        path_loss = shadow_fading(path_loss, cfg)
    eirp_value = eirp(cfg)
    rx_power = compute_rx_power(eirp_value, cfg, path_loss)
    margin = link_margin(rx_power, cfg)
    value0 = zero_crossing_distance(margin, dist)

    return margin, value0, rx_power
