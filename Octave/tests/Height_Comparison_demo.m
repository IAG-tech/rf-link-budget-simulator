addpath(genpath(fileparts(mfilename('fullpath'))))

% Antenna height comparison demo
% compares link margin for three transmitter antenna heights using LTE 1800MHz
% while keeping all other link budget parameters equal

% ---------- Inputs ---------

% See lte1800_config for the default LTE1800 parameters


lte20 = lte1800_config();
lte40 = lte1800_config();
lte80 = lte1800_config();

lte20.h_tx_m = 20;
lte40.h_tx_m = 40;
lte80.h_tx_m = 80;

d_Km = linspace(0.1, 10, 300); % Distance vector from 0.1 Km to 10 Km


scenario = "urban";
city_type = "big";

% ---------- Path Loss Model  ------------

% Okumura-Hata path loss for LTE-1800 at different base station heights

PL_20_dB = okumura_hata(d_Km,lte20, scenario,city_type);
PL_40_dB = okumura_hata(d_Km,lte40, scenario,city_type);
PL_80_dB = okumura_hata(d_Km,lte80, scenario,city_type);


% ---------- Received power ---------------

% Received power for LTE1800 at different base station heights

Pr_20m_dBm = compute_rx_power(lte20,PL_20_dB);
Pr_40m_dBm = compute_rx_power(lte40,PL_40_dB);
Pr_80m_dBm = compute_rx_power(lte80,PL_80_dB);

% ------------ Link margin -----------------

% Link margin for LTE1800 at different base station heights

Margin_20m = link_margin(Pr_20m_dBm,lte20);
Margin_40m = link_margin(Pr_40m_dBm,lte40);
Margin_80m = link_margin(Pr_80m_dBm,lte80);


% -------- Zero crossing distance ---------

% Distance where link margin crosses 0dB line

d0_20m = zero_crossing_distance(Margin_20m,d_Km)
d0_40m = zero_crossing_distance(Margin_40m,d_Km)
d0_80m = zero_crossing_distance(Margin_80m,d_Km)

% --------- Plots ------------

figure;
plot(d_Km, Margin_20m)
hold on
plot(d_Km, Margin_40m)
hold on
plot(d_Km, Margin_80m)
hold on
plot(d_Km, zeros(size(d_Km)),'--k')
grid on
xlabel("Distance (km)")
ylabel("Link margin (dB)")
title("Antenna height Comparison (LTE1800 & Okumura-Hata Model)")
legend("20m", "40m","80m","0dB")
