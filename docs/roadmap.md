# Project Roadmap

This document describes the planned development stages of the RF Link Budget Simulator.

The project is developed incrementally to ensure that each component of the system is validated before introducing additional complexity.

---

# Version History and Planned Features

## v0.1 – Initial Project Setup

Goals:

- basic repository structure
- initial documentation
- simple link budget concept

Features:

- project documentation
- basic architecture planning

---

## v0.2 – Core Link Budget

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

## v0.3 – Large Scale Propagation

Goals:

Introduce environmental variability into the link model.

Features:

- lognormal shadowing model
- integration with link budget pipeline

Capabilities:

- deterministic link analysis
- simple stochastic attenuation

---

## v0.4 – Additional Propagation Models (Planned)

Goals:

Expand the propagation modelling capabilities.

Planned features:

- configurable propagation environments

This version focuses on large-scale propagation modelling.

---

## v0.5 – Monte Carlo Simulation (Planned)

Goals:

Move from deterministic analysis to statistical analysis.

Planned features:

- Monte Carlo simulation framework
- random shadowing generation
- SNR distribution analysis
- link margin
- outage probability estimation

This version introduces statistical link analysis.

---

## v0.6 – Small Scale Fading (Planned)

Goals:

Introduce multipath channel effects. Begin migration to Python.

Planned models:

- Rayleigh fading
- Rician fading

Capabilities:

- modelling fast signal fluctuations
- evaluation of link robustness under fading
- Basic Python implementation

---

## v0.7 – Advanced Channel Models (Future)

Potential future extensions:

- Nakagami fading
- correlated shadowing
- time-varying channels
- Doppler effects
- mobility models

---

# Long-Term Goals

Possible future directions include:

- SDR integration
- channel measurement validation
- realistic propagation environments
- advanced simulation workflows
- Python scientific ecosystem integration

---

# Development Philosophy

The simulator is developed with the following principles:

- modular architecture
- transparent mathematical models
- reproducible simulations
- progressive complexity

Each version adds one layer of realism while maintaining clarity in the model design.