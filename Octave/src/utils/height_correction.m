function correction = height_correction(cfg, city_type)
  % Height correction function
  % depending on the city type returns a different value for correction factor
  %
  % Inputs:
  %   cfg        Configuration structure containing:
  %                    - f_MHz   Carrier frequency (MHz)
  %                    - h_rx_m  Receiver antenna height (m)
  %
  %   city_type  City size for the correction factor ("big","medium","small")
  %
  % Outputs:
  %   correction   correction value for Okumura-Hata model


  % -------------------- Scenario election ----------------
  % Computes correction for Okumura-Hata model depending on scenario
  switch lower(strtrim(city_type))
    case "big"
      if(cfg.f_MHz<=300)
        correction = 8.29*(log10(1.54*cfg.h_rx_m))^2-1.1;
      else
        correction = 3.2*(log10(11.75*cfg.h_rx_m))^2-4.97;
      endif
    case {"medium", "small"}
        correction = (1.1*log10(cfg.f_MHz)-0.7)*cfg.h_rx_m-(1.56*log10(cfg.f_MHz)-0.8);
    otherwise
        error("Unknowed city type");
  endswitch

 endfunction
