function okumura = okumura_hata(d_Km, cfg, scenario, city_type)

  %  OKUMURA-HATA propagation model
  %
  %  Computes path loss using Okumura-Hata empirical model.
  %
  %
  %  Inputs:
  %     d_Km       Distance(km) [scalar or vector]
  %     cfg        Configuration structure containing:
  %                    - f_MHz    Carrier frequency (MHz)
  %                    - h_tx_m   Base station antenna height (m)
  %                    - h_rx_m   Receiver antenna height (m)
  %     scenario   Environment type ("Urban","Suburban","rural")
  %     city_type  City size for the correction factor ("big","medium","small")
  %
  %
  %  Output:
  %     okumura    Path Loss (dB)

  %  Limitations:
  %     Frequency:               150-1500MHz
  %     Receiver antenna height: 1-10m
  %     Base antenna height:     30-200m

  % ----------- Height correction factor ---------
  % Mobile antenna height correction depending on city type

        correction = height_correction(cfg, city_type);

  % ----------- Urban model ----------------------
  % Okumura-Hata path loss for urban environments

        okumura_urban = 69.55 + 26.16*log10(cfg.f_MHz) - 13.82*log10(cfg.h_tx_m) - correction + (44.9 - 6.55*log10(cfg.h_tx_m))*log10(d_Km);

  % ---------------- Scenario election ------------
  % Apply correction depending on scenario

        switch lower(scenario)
          case "urban"
            okumura = okumura_urban;
          case "suburban"
            okumura = okumura_urban -2*(log10(cfg.f_MHz/28))^2 - 5.4;
          case "rural"
            okumura = okumura_urban -4.78*(log10(cfg.f_MHz))^2 + 18.33*log10(cfg.f_MHz)- 40.94;
        endswitch

  endfunction
