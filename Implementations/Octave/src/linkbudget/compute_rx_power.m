function Pr = compute_rx_power(cfg,PL)

  % Pr is the received power at the receiver (dBm)
  % Uses formula:
  % Pr = Ptx_dBm + Gtx_dBi + Grx_dBi - Ltx_dB - Lrx_dB - Lextra_dB - PL

  % Ptx_dBm    Power transmited. Measured in dBm
  % Gtx_dBi    Gain of the transmitter antenna. Measured in dBi
  % Grx_dBi    Gain of the receiver antenna. Measured in dBi

  % Ltx_dB     Losses of the transmitter. measured in dB
  % Lrx_dB     Losses of the receiver. Measured in dB
  % Lextra_dB  Additional fixed losses. Measured in dB

  % PL         Propagation path loss (FSPL with optional shadow fading). Measured in dB

% ------- Calculation -------

  Pr = cfg.Ptx_dBm + cfg.Gtx_dBi + cfg.Grx_dBi - cfg.Ltx_dB - cfg.Lrx_dB - cfg.Lextra_dB - PL;


  endfunction
