addpath(genpath(fileparts(mfilename('fullpath'))))

  % GEO Satellite Link Budget Demo
  % Simulates link margin vs elevation angle for UHF and S-band
  % GEO orbit at 35,786 km using FSPL propagation model
  %
  % Outputs:
  %   - Minimum operational elevation angle per band
  %   - Link margin vs elevation angle plot (UHF vs S-band)

% ---------- Inputs ---------

  % Loading the inputs

geo_uhf = uhf_geo_config();     % UHF technology parameters
geo_sband = sband_geo_config(); % S-band technology parameters
constants = geo_constants();    % Physical constants

angle = linspace(5,90,86);      % Angle vector from 5º to 90º with step of 1º

d_Km = GEO_distance(constants,angle); % Calculates the distance at the angles of the vector


% ---------- Path Loss Model ------------

  % Calculates the path loss of the technologies using the parameters of the technologies
  % and the distance calculated before

FSPL_UHF_dB = fspl(geo_uhf,d_Km);
FSPL_Sband_dB = fspl(geo_sband,d_Km);

% ---------- Link budget -----

  % Calculates received power at the ground station for the diferent satellite technologies

Pr_dBm_FSPL_UHF = compute_rx_power(geo_uhf,FSPL_UHF_dB);
Pr_dBm_FSPL_Sband = compute_rx_power(geo_sband,FSPL_Sband_dB);

% ------------ Link margin ----------

  % Link margin for UHF and S-band

Margin_FSPL_UHF = link_margin(Pr_dBm_FSPL_UHF,geo_uhf);
Margin_FSPL_Sband = link_margin(Pr_dBm_FSPL_Sband,geo_sband);

% -------- Zero crossing angle ---------

  % Finds the elevation angle where link margin crosses 0dB line and becomes positive
  % Displays different messages depending on the result
  %        - Coverage at any angle: link margin is always positive
  %        - No coverage at any angle: link margin is always negative
  %        - Elevation = xº Minimal operational angle (link margin crosses 0 dB at a specific angle)

 [d0_FSPL_UHF, msg] = zero_crossing_elevation(Margin_FSPL_UHF,angle,'UHF');
 disp(msg)
 [d0_FSPL_Sband, msg] = zero_crossing_elevation(Margin_FSPL_Sband,angle,'S-band');
 disp(msg)

% --------- Plots ------------

figure;
plot(angle, Margin_FSPL_UHF)
hold on
plot(angle, Margin_FSPL_Sband)
hold on
plot(angle, zeros(size(d_Km)),'--k')
grid on
ylim([-2 3])
xlabel("Angle (º)")
ylabel("Link margin (dB)")
title("GEO Link Margin vs Elevation Angle")
legend("UHF Margin", "S-band Margin","0dB")
