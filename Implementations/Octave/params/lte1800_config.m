function cfg = lte1800_config()
  % LTE 1800 MHz configuration parameters

  cfg.name = "LTE-1800";
  cfg.f_MHz = 1800;

  cfg.Ptx_dBm = 46;         % LTE macro 43 to 46 dBm, LTE micro 30 to 40
  cfg.Gtx_dBi= 8;           % small cells around 6 - 10 dBi , LTE macro base stations 15 to 18 dBi
  cfg.Grx_dBi = 0;

  cfg.h_tx_m = 30;          % Transmitter antenna height
  cfg.h_tx_m = 1.5;         % Receiver height

  cfg.Ltx_dB = 2;           % wire, connectors, ....
  cfg.Lrx_dB = 0;
  cfg.Lextra_dB = 10;       % rural 0 to 5 dB, suburban 5 to 10 dB, urban 10 to 20 dB

  cfg.sensivity_dBm = -95;  % -90 to -100 dBm

  endfunction
