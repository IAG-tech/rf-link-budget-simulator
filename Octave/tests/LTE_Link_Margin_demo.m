addpath(genpath(fileparts(mfilename('fullpath'))))

% Model comparison demo
% compares link margin for three different propagation models at LTE1800

% ---------- Inputs ---------

% See lte1800_config for the default LTE1800 parameters

lte = lte1800_config();


d_Km = linspace(0.1, 30, 300); % Distance vector from 0.1 Km to 30 Km

scenario = "urban";
city_type = "big";

% ---------- Path Loss Models ------------

% Cost-Hata, Okumura-Hata and FSPL models for LTE-1800

Cost231_dB = cost_hata(d_Km,lte, scenario);
Okumura_dB = okumura_hata(d_Km,lte, scenario,city_type);
FSPL_dB = fspl(lte,d_Km);

% ---------- Link budget -----

% Received power for LTE1800 with differents path losses

Pr_dBm_Cost231 = compute_rx_power(lte,Cost231_dB);
Pr_dBm_Okumura = compute_rx_power(lte,Okumura_dB);
Pr_dBm_FSPL = compute_rx_power(lte,FSPL_dB);

% ------------ Link margin ----------

% Link margin for LTE1800

Margin_FSPL = link_margin(Pr_dBm_FSPL,lte);
Margin_Okumura = link_margin(Pr_dBm_Okumura,lte);
Margin_Cost231 = link_margin(Pr_dBm_Cost231,lte);


% -------- Zero crossing distance ---------

% Distance where link margin crosses 0dB line

d0_FSPL = zero_crossing_distance(Margin_FSPL,d_Km)
d0_Okumura = zero_crossing_distance(Margin_Okumura,d_Km)
d0_Cost231 = zero_crossing_distance(Margin_Cost231,d_Km)

% --------- Plots ------------

figure;
plot(d_Km, Margin_FSPL)
hold on
plot(d_Km, Margin_Okumura)
hold on
plot(d_Km, Margin_Cost231)
hold on
plot(d_Km, zeros(size(d_Km)),'--k')
grid on
xlabel("Distance (km)")
ylabel("Link margin (dB)")
title("Propagation Model Comparison (FSPL vs Okumura-Hata vs Cost231-Hata)")
legend("FSPL", "Okumura","Cost231","0dB")
