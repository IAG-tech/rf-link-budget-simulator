function FSPL_dB = fspl( cfg , d_Km )

  %  FSPL Free Space Path Loss (dB)

  %  FSPL_dB = fspl (f_MHz, d_Km)
  %  f_MHz: Frecuency in MHz
  %  d_Km: Distance in Km (can be scalar or vector)
  %  Uses formula:
  %     FSPL(dB) = 32.44 + 20*log10(f_MHz) + 20*log10(d_Km)
  %  Assumes far-field, free space conditions

  % ---- Input validation ----

  assert(all( cfg.f_MHz >0), "Frequency must be >0MHz");
  assert(all( d_Km >0), "Distance must be >0Km");

  % ----- Calculation ------

  FSPL_dB = 32.44 + 20*log10(cfg.f_MHz)+ 20*log10(d_Km);

endfunction
