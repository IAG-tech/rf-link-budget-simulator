% Shadow fading demo:
% show how log-normal shadowing causes deviations around
% the received power predicted by  the FPSL model

% ---------- Inputs ---------

tetra = tetra_config(); % I use TETRA technology for the demo

% ---------- Scenario -------

scenario = "urban"; % Selection of different scenarios

d_Km = linspace(0.1, 30, 300);   % Distance vector from 0.2Km to 30Km

% ---------- FSPL ------------

FSPL_dB = fspl(tetra.f_MHz,d_Km);                % Calculation of FSPL using fspl function
FSPL_dB_shadow = shadow_fading(FSPL_dB,scenario); % Add shadow to the FSPL using shadow_fading function

% ---------- Link budget -----

Pr_dBm_shadow = compute_rx_power(tetra,FSPL_dB_shadow); % Received power with shadow
Pr_dBm = compute_rx_power(tetra,FSPL_dB);               % Received power without shadow

% ---------- Plots -----------

figure;
plot(d_Km, Pr_dBm)
hold on
plot(d_Km, Pr_dBm_shadow)
grid on
xlabel("Distance (km)")
ylabel("Pr (dBm)")
title("Shadow Fading Effect")
legend("Received power whithout shadowing", "Shadowed received power")
