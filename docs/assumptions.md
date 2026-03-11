# Assumptions

This simulator implements a simplified RF link budget model intended for educational purposes and basic propagation exploration.

## Propagation model

Path loss is computed using the Free Space Path Loss (FSPL) model:

FSPL(dB) = 32.44 + 20·log10(f_MHz) + 20·log10(d_km)

Where:

- f_MHz = carrier frequency in MHz  
- d_km = distance between transmitter and receiver in km  

The model assumes:

- Line-of-sight propagation  
- No reflections or diffraction  
- No terrain or clutter effects  

## Shadow fading

Large-scale signal variations can be simulated using log-normal shadow fading.

Shadow fading is modeled as:

PL_shadow = PL + Xσ

Where Xσ is a Gaussian random variable.

Typical values used:

| Scenario | σ (dB) |
|--------|--------|
| Urban | 8 |
| Suburban | 6 |
| Rural | 4 |

## System losses

Additional losses are modeled with a constant parameter:

Lextra_dB

This represents aggregated losses such as:

- building penetration
- vegetation attenuation
- miscellaneous system losses

## Limitations

The current model does not include:

- terrain effects  
- diffraction  
- interference  
- noise modeling  
- SINR or capacity estimation  

Only received power (Pr) is computed.

## Purpose

The goal of this project is to explore the fundamentals of:

- RF link budgets  
- propagation vs distance  
- frequency impact on coverage
- comparation between technologies  
- shadow fading effects
