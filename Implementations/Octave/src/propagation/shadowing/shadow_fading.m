function PL_shadow = shadow_fading (PL,scenario)

  % Applies log-normal shadow fading to a path loss vector
  % The shadowing term is modelled as a zero-mean  Gaussian random variable
  % in dB, with scenario-dependant standard deviation

  % -------- Scenario selector -------

   switch lower(scenario)
     case "urban"
       sigma = 8;
     case "suburban"
       sigma = 6;
     case "rural"
       sigma = 4;
     otherwise
       error("Unknown scenario");
   endswitch

  % ------- Calculation -------

  shadow = sigma*randn(size(PL)); % sigma *  zero-mean Gaussian random  variable vector
  PL_shadow = PL + shadow;        % Adds log-normal shadow fading to Path loss

  endfunction
