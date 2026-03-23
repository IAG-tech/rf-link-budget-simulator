function link = link_margin(Pr,cfg)

  % LINK MARGIN (dB)
  %
  % Computes the link margin as the difference between receiver power
  % and receiver sensitivity
  %
  % Inputs:
  %    Pr    Received power (dBm)
  %    cfg   Configuration structure containing:
  %                - sensitivity_dBm Receiver sensitivity (dBm)
  %
  % Output:
  %    link  Link margin (dB)
  %
  % Interpretation:
  %     link > 0 dB   sufficient signal level
  %     link = 0 dB   coverage threshold
  %     link < 0 dB   insufficient signal level
  %
  % Link margin can be used to estimate coverage probability when
  % combined with random fading (Monte Carlo simulations).

  link = Pr - cfg.sensitivity_dBm;

  endfunction
