function cfg = geo_constants()

  % Physical constants for GEO satellite geometry
  % Used by GEO_distance and all satellite scenario configs

  cfg.terrestrial_radio = 6371 ; % Earth radius (km)
  cfg.geo_distance = 35786;      % GEO orbital altitude (km), so r+g = orbital radius

  endfunction
