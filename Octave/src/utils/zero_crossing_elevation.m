function [elev0, msg] = zero_crossing_elevation(link_margin, elev_deg, band_name)

  % Finds minimum elevation angle where link margin crosses 0 dB
  % Assumes margin increases with elevation angle

  % First point where margin becomes positive
  idx = find(link_margin >= 0, 1);

  % Case 1: Never positive → no coverage at any angle
  if isempty(idx)
    elev0 = NaN;
    msg = sprintf("%s: No coverage at any elevation angle", band_name);

  % Case 2: Already positive at first angle
  elseif idx == 1
    elev0 = elev_deg(1);
    msg = sprintf("%s: Coverage at any elevation angle", band_name);

  % Case 3: Normal  interpolate between last negative and first positive
  else
    e1 = elev_deg(idx-1);   % Last angle with negative margin
    e2 = elev_deg(idx);     % First angle with positive margin
    m1 = link_margin(idx-1);
    m2 = link_margin(idx);
    elev0 = interp1([m1, m2], [e1, e2], 0);
    msg = sprintf("%s: Elevation = %.2f deg", band_name, elev0);
  endif

endfunction
