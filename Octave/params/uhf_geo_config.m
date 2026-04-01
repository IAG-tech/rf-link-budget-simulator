function cfg = uhf_geo_config()

  % UHF GEO satellite configuration
  % Represents a small satellite TT&C (Telemetry, Tracking and Command) link
  % Frequency: 400 MHz (UHF, typical for satellite command and telemetry)
  % Ground station: Yagi antenna (13 dBi)

  cfg.name = "UHF";
  cfg.f_MHz = 400;               % Frequency of S-band

  cfg.Ptx_dBm = 37;              % 30 to 37 dBm small satellites
  cfg.Gtx_dBi = 6;               %  0 to 6 dBi omnidirectional antennas

  cfg.Grx_dBi = 13;              %  10 to 15 Yagui antennas

  cfg.Ltx_dB = 0;
  cfg.Lrx_dB = 0;
  cfg.Lextra_dB = 0;             % Atmosferic losses

  cfg.sensitivity_dBm = -120;    % -100 to -120 dBm

  endfunction
