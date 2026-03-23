addpath(genpath(fileparts(mfilename('fullpath'))))

% Technology comparison demo
% compares received power for TETRA and LTE800 using different
% technology-specific link budget parameters

% ---------- Inputs ---------
% To see the params of tetra and lte please see tetra_config and lte800_config functions
tetra = tetra_config();
lte = lte800_config();

d_Km = linspace(0.1, 30, 300); % Distance vector from 0.1 Km to 30 Km

% ---------- FSPL ------------

FSPL_dB_TETRA = fspl(tetra.f_MHz,d_Km); % Calculation of FSPL of TETRA technology using fspl function
FSPL_dB_LTE   = fspl(lte.f_MHz,d_Km);   % Calculation of FSPL of LTE technology using fspl function

% ---------- Link budget -------

Pr_dBm_TETRA = compute_rx_power(tetra,FSPL_dB_TETRA); % Calculation of TETRA Received power using compute_rx_power function
Pr_dBm_LTE = compute_rx_power(lte,FSPL_dB_LTE);       % Calculation of LTE Received power using compute_rx_power function

% -------- Plots ----------

figure;
plot(d_Km, Pr_dBm_TETRA)
hold on
plot(d_Km, Pr_dBm_LTE)
grid on
xlabel("Distance (km)")
ylabel("Pr (dBm)")
title("TETRA vs LTE800 Received Power")
legend("TETRA", "LTE")
