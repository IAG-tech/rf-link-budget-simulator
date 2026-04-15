function cfg = sband_geo_config()

  % S-band GEO satellite configuration
  % Represents a small satellite downlink scenario
  % Frequency: 2 GHz (S-band, typical Earth observation missions)
  % Ground station: small parabolic dish (30 dBi)

  cfg.name = "S-band";
  cfg.f_MHz = 2000;                     % Frequency of S-band

  cfg.Ptx_dBm = 37;                     % 30 to 37 dBm small satellites
  cfg.Gtx_dBi = 6;                      %  0 to 6 dBi omnidirectional antennas

  cfg.Grx_dBi = 30;                     % 20 to 30 dBi parabolic antennas

  cfg.Ltx_dB = 0;
  cfg.Lrx_dB = 0;
  cfg.Lextra_dB = 1;                    % Atmospheric losses

  cfg.sensitivity_dBm = -120;           % -100 to -120 dBm

  endfunction
