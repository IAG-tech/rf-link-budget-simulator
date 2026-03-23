function cost = cost_hata(d_Km, cfg, scenario)
  %  COST-HATA propagation model
  %
  %  Computes path loss using Cost-Hata empirical model.
  %
  %
  %  Inputs:
  %     d_Km       Distance(km) [scalar or vector]
  %     cfg        Configuration structure containing:
  %                    - f_MHz    Carrier frequency (MHz)
  %                    - h_tx_m   Base station antenna height (m)
  %                    - h_rx_m   Receiver antenna height (m)
  %     scenario   Environment type ("Urban","Suburban","rural")
  %
  %
  %  Output:
  %     cost    Path Loss (dB)

  %  Limitations
  %     Frequency:               1500-2000MHz
  %     Receiver antenna height: 1-10m
  %     Base antenna height:     30-200m
  %     Distance:                1-20km

  % ----------- correction factor ---------
  % Mobile antenna height correction depending on scenario

        switch lower(strtrim(scenario))
          case "urban"
            if (cfg.f_MHz>=150 && cfg.f_MHz<=200)
              correction = 8.29*(log10(1.54*cfg.h_rx_m))^2-1.1;
              constant = 3;
             elseif (cfg.f_MHz>200 && cfg.f_MHz<=2000)
              correction = 3.2*(log10(11.75*cfg.h_rx_m))^2-4.97;
              constant = 0;
            else
              error("Wrong frequency");
            endif
          case {"suburban", "rural"}
            correction = (1.1*log10(cfg.f_MHz)-0.7)*cfg.h_rx_m-(1.56*log10(cfg.f_MHz)-0.8);
            constant = 0;
        endswitch

      cost = 46.3 + 33.9*log10(cfg.f_MHz) - 13.82*log10(cfg.h_tx_m) - correction + (44.9 - 6.55*log10(cfg.h_tx_m))*log10(d_Km)+constant;

  endfunction
