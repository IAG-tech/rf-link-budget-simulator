function d = GEO_distance(cfg, angle)

  % Calculates the slant range between ground station and GEO satellite
  % as a function of elevation angle.
  %
  % Uses the quadratic form of the law of cosines:
  %   d^2 + 2*r*sin(e)*d + (r^2 - (r+g)^2) = 0
  %
  % Solved for the positive root:
  %   d = -r*sin(e) + sqrt(r^2*sin^2(e) - r^2 + (r+g)^2)
  %
  % Where:
  %   r = Earth radius (km)
  %   g = GEO orbital altitude (km), so r+g = orbital radius
  %   e = elevation angle (degrees), we need to convert to radians
  %
  % Validation:
  %   elevation 90 deg -> 35,786 km
  %   elevation  5 deg -> 41,121 km

    r = cfg.terrestrial_radio;
    g = cfg.geo_distance;

    d = -r*sin(deg2rad(angle))+sqrt(r^2*(sin(deg2rad(angle))).^2-r^2+(r+g)^2);

  endfunction
