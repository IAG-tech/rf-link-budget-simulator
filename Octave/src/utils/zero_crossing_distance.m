function d0 = zero_crossing_distance(link_margin,d_Km)

  % ZERO CROSSING DISTANCE (Km)
  %
  %  Computes the distance at which the link margin crosses 0dB threshold
  %
  %
  %  Inputs:
  %    link_margin       Link margin vector (dB)
  %    d_Km              Distance vector (Km)
  %
  %  Outputs:
  %    d0                Distance where link margin equals 0dB
  %
  %  Interpretation:
  %    link_margin > 0dB Coverage avalaible
  %    link_margin = 0dB Coverage threshold
  %    link_margin < 0dB Coverage unavalaible
  %
  %
  % ------------ Find first zero crossing -----
  % Finds first point where link margin is minor or equal to 0 dB
  idx = find(link_margin <= 0,1);

  % -------- Case 1: No crossing ----------
  % Link margin is always positive. Coverage extends beyond range

  if(isempty(idx))
  d0 = NaN;

  % -------- Case 2: Crossing at first point -----------
  % Coverage lost at beginning
  elseif(idx == 1)
  d0 = d_Km(1);

  % -------- Case 3: Normal case --------
  % Interpolate between two points around the crossing
  else
  d1 = d_Km(idx-1); % Distance before crossing
  d2 = d_Km(idx);   % Distance after crossing

  m1 = link_margin(idx-1); % Positive margin
  m2 = link_margin(idx);   % Negative margin
  % Linear interpolation to estimate distance where link margin equals 0 dB
  d0 = interp1([m1 , m2], [d1 , d2], 0);
  endif

  endfunction
