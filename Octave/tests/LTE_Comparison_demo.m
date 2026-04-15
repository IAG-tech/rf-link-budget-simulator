addpath(genpath(fileparts(mfilename('fullpath'))))

% Frequency effect demo
% compares link margin for three carrier frequencies

% ---------- Inputs ---------

% See lte800_config, lte1800_config and lte2600_config for the default LTE800, LTE1800 and LTE2600 parameters

lte800 = lte800_config();
lte1800 = lte1800_config();
lte2600 = lte2600_config();


d_Km = linspace(0.1, 10, 300); % Distance vector from 0.1 Km to 10 Km


scenario = "urban";
city_type = "big";

% ---------- Okumura Path Loss ------------

% Okumura-Hata model for three different LTE technologies: 800MHz, 1800MHz and 2600MHz

Okumura_800_dB = okumura_hata(d_Km,lte800, scenario,city_type);
Okumura_1800_dB = okumura_hata(d_Km,lte1800, scenario,city_type);
Okumura_2600_dB = okumura_hata(d_Km,lte2600, scenario,city_type);

% ---------- Link budget -----

% Received power for LTE800, LTE1800 and LTE2600

Pr_800MHz_dBm = compute_rx_power(lte800,Okumura_800_dB); % Calculation of TETRA Received power using compute_rx_power function
Pr_1800MHz_dBm = compute_rx_power(lte1800,Okumura_1800_dB); % Calculation of TETRA Received power using compute_rx_power function
Pr_2600MHz_dBm = compute_rx_power(lte2600,Okumura_2600_dB); % Calculation of TETRA Received power using compute_rx_power function

% ------------ Link margin ----------

% Link margin for LTE800, LTE1800 and LTE2600

Margin_800MHz = link_margin(Pr_800MHz_dBm,lte800);
Margin_1800MHz = link_margin(Pr_1800MHz_dBm,lte1800);
Margin_2600MHz = link_margin(Pr_2600MHz_dBm,lte2600);



% -------- Zero crossing distance ---------

% Distance where link margin crosses 0dB line

d0_800_Okumura = zero_crossing_distance(Margin_800MHz,d_Km)
d0_1800_Okumura = zero_crossing_distance(Margin_1800MHz,d_Km)
d0_2600_Okumura = zero_crossing_distance(Margin_2600MHz,d_Km)


% --------- Plots ------------

figure;
plot(d_Km, Margin_800MHz)
hold on
plot(d_Km, Margin_1800MHz)
hold on
plot(d_Km, Margin_2600MHz)
hold on
plot(d_Km, zeros(size(d_Km)),'--k')
grid on
xlabel("Distance (km)")
ylabel("Link margin (dB)")
title("LTE Link Margin Comparison ")
legend("LTE800", "LTE1800","LTE2600", "0dB")

