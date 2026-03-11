function cfg = lte800_config()
  % LTE 800 MHz configuration parameters

  cfg.name = "LTE-800";
  cfg.f_MHz = 800;             % Typical bands 791 - 821 MHz uplink, 832 - 862 MHz downlink

  cfg.h_tx_m = 30;             % Transmitter antenna height
  cfg.h_tx_m = 1.5;            % Receiver height

  cfg.Ptx_dBm = 46;            % LTE macro 43 to 46 dBm, LTE micro 30 to 40
  cfg.Gtx_dBi = 15;            % small cells around 6 - 10 dBi , LTE macro base stations 15 to 18 dBi
  cfg.Grx_dBi = 0;

  cfg.Ltx_dB = 2;              % wire, connectors, ....
  cfg.Lrx_dB = 0;
  cfg.Lextra_dB = 10;          % rural 0 to 5 dB, suburban 5 to 10 dB, urban 10 to 20 dB

  cfg.sensitivity_dBm = -95;   % -90 to -100 dBm

  endfunction
