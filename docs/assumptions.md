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

## Satellite scenario (v0.5)

### Orbital geometry

GEO satellite distance varies with elevation angle.
The slant range is computed using the law of cosines:

d² + 2·r·sin(ε)·d + (r² - (r+g)²) = 0

Where:
- r = 6,371 km (Earth radius)
- g = 35,786 km (GEO orbital altitude)
- ε = elevation angle (degrees)

Solving for d (positive root):

d = -r·sin(ε) + sqrt(r²·sin²(ε) - r² + (r+g)²)

Reference values:
- Elevation 90°: 35,786 km (minimum distance)
- Elevation 5°: ~41,121 km (maximum distance)

### UHF scenario parameters

| Parameter | Value | Justification |
|---|---|---|
| Frequency | 400 MHz | Typical TT&C band for small satellites |
| Tx Power | 37 dBm | Small satellite (5W) |
| Tx Antenna Gain | 6 dBi | Omnidirectional satellite antenna |
| Rx Antenna Gain | 13 dBi | Yagi antenna — ground station |
| Rx Sensitivity | -120 dBm | Optimised low-rate TT&C receiver |

### S-band scenario parameters

| Parameter | Value | Justification |
|---|---|---|
| Frequency | 2000 MHz | S-band downlink |
| Tx Power | 37 dBm | Small satellite (5W) |
| Tx Antenna Gain | 6 dBi | Omnidirectional satellite antenna |
| Rx Antenna Gain | 30 dBi | Small parabolic dish — ground station |
| Rx Sensitivity | -120 dBm | S-band receiver |

### Key results

- UHF minimum operational elevation angle: 41.49°
- S-band link margin positive across full elevation range (5°–90°)
- FSPL difference between bands at 90°: ~14 dB
- S-band requires significantly higher Rx antenna gain to 
  compensate for increased propagation loss

## Limitations

### Terrestrial scenario limitations

The current model does not include:

- terrain effects  
- diffraction  
- interference  
- noise modeling  
- SINR or capacity estimation  

Only received power (Pr) is computed.

### Satellite scenario limitations

- FSPL only — no atmospheric absorption model
- No Doppler effect (GEO assumption)
- No polarisation losses
- No rain attenuation (ITU-R P.618 not implemented)
- Single ground station, no diversity


## Purpose

The goal of this project is to explore the fundamentals of:

- RF link budgets  
- propagation vs distance  
- frequency impact on coverage
- comparation between technologies  
- shadow fading effects
