# Project Roadmap

This document describes the planned development stages of the RF Link Budget Simulator.
The project is developed incrementally to ensure that each component of the system is 
validated before introducing additional complexity.

---

## Version History and Planned Features

### v0.1 – Initial Project Setup ✅

Goals:
- basic repository structure
- initial documentation
- simple link budget concept

Features:
- project documentation
- basic architecture planning

---

### v0.2 – Core Link Budget ✅

Goals:
Implement the basic RF link budget calculation.

Features:
- transmit power
- antenna gains
- Free Space Path Loss (FSPL)
- received power calculation

Outputs:
- received power estimation
- basic link margin evaluation

---

### v0.3 – Large Scale Propagation ✅

Goals:
Introduce environmental variability into the link model.

Features:
- lognormal shadowing model
- integration with link budget pipeline

Capabilities:
- deterministic link analysis
- simple stochastic attenuation

---

### v0.4 – Additional Propagation Models ✅

Goals:
Expand the propagation modelling capabilities.

Features:
- Okumura-Hata model (urban / suburban / rural)
- COST 231-Hata model (urban extension, 1500–2000 MHz)
- configurable propagation environments


---

### v0.5 – Satellite Link Budget Scenario ✅

Goals:
Extend the simulator to cover satellite communication scenarios.

Features:
- GEO satellite link scenario (35,786 km)
- S-band and UHF frequency support
- atmospheric loss margin
- elevation angle effect on link margin
- comparison: terrestrial vs satellite link budget

This version bridges the simulator with real space-to-ground 
communication analysis.

---

### v0.6 – Migration to Python ✅

Goals:
Migrate the full codebase to Python for modularity, 
maintainability and ecosystem integration.

Features:
- modular architecture (propagation, link budget, utils)
- model dispatcher pattern
- NumPy / SciPy implementation
- Plotly visualisation
- equivalent outputs to Octave prototype

---

### v0.7 – Monte Carlo Simulation 🔄

Goals:
Move from deterministic analysis to statistical analysis.

Features:
- Monte Carlo simulation framework
- random shadowing generation
- SNR distribution analysis
- link margin statistics
- outage probability estimation

---

### Electronic Warfare module 

Goals:
Evaluate link resilience.

Features:
- ESM
- J/S ratio
- Burn-through range
---

### v0.9 – SDR Integration and Model Validation

Goals:
Connect simulated models with real measured signals.

Features:
- RTL-SDR signal capture
- measured vs simulated path loss comparison
- model validation workflow
- DSP pipeline integration (FFT, filtering)

---

## Long-Term Goals

Possible future directions include:

- small-scale fading (Rayleigh, Rician)
- mobility models and dynamic simulation
- Doppler effects
- GNU Radio integration
- advanced radar signal processing

---

## Development Philosophy

The simulator is developed with the following principles:

- modular architecture
- transparent mathematical models
- reproducible simulations
- progressive complexity

Each version adds one layer of realism while maintaining 
clarity in the model design.
