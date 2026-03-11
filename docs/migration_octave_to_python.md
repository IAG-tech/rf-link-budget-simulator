# Migration from Octave to Python

This document explains the rationale behind maintaining both an Octave and a Python implementation of the simulator.

---

## Motivation

The project initially started as an Octave prototype in order to rapidly test and validate the mathematical models used in RF link budget analysis.

Octave provides:

- fast prototyping
- MATLAB-like syntax
- convenient numerical experimentation

However, as the simulator grows in complexity, Python offers several advantages.

---

## Why Python

Python provides a more robust ecosystem for scientific computing and software engineering.

Key advantages include:

- modular software architecture
- better package management
- unit testing frameworks
- scientific libraries (NumPy, SciPy)
- advanced visualization tools
- easier integration with other systems

For these reasons, Python will eventually become the primary implementation of the simulator.

---

## Current Status

### Octave Implementation

Purpose:

- initial prototype
- validation of mathematical models
- rapid experimentation

Capabilities:

- link budget calculation
- FSPL
- lognormal shadowing

Future additions may include:

- additional propagation models
- Monte Carlo simulation

---

### Python Implementation

Status:

Work in Progress.

Goals:

- modular simulator architecture
- reproducible simulation pipelines
- improved data handling
- advanced statistical analysis

Planned features:

- full link budget implementation
- propagation models
- Monte Carlo simulation framework
- visualization tools

---

## Validation Strategy

The Octave implementation will serve as a reference baseline during the Python migration.

This allows:

- validation of numerical results
- comparison between implementations
- verification of model correctness

Where possible, both implementations should produce equivalent results for identical scenarios.

---

## Long-Term Plan

Eventually, Python will become the main platform for development, while the Octave implementation will remain as:

- historical reference
- educational prototype
- validation benchmark

---

## Conclusion

The dual-language approach allows the project to combine:

- rapid scientific prototyping (Octave)
- scalable software architecture (Python)
