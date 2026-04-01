function cfg = tetra_config()

  % TETRA 400 MHz configuration parameters

  cfg.name = "UHF";
  cfg.f_MHz = 400;               % Typical bands 380 - 385 MHz uplink, 390 - 395 MHz downlink


  cfg.Ptx_dBm = 44;              % 43 to 46 dBm
  cfg.Gtx_dBi = 6;               %  3 to 8 dBi
  cfg.Grx_dBi = 0;               %  -2 to +2 dBi

  cfg.Ltx_dB = 2;                % wire, connectors, ....
  cfg.Lrx_dB = 0;
  cfg.Lextra_dB = 10;            % rural 0 to 5 dB, suburban 5 to 10 dB, urban 10 to 20 dB

  cfg.sensitivity_dBm = -100;    % 100 to -104 dBm


  endfunction
