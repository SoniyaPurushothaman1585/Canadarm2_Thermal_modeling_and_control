# Thermal Architecture Overview – Canadarm2 Thermal Control System

## 1. Introduction

This document presents the thermal architecture of the Canadarm2 Thermal Control System (TCS). It describes how thermal loads are managed in the space environment, how components are thermally protected, and how the system integrates with the International Space Station (ISS) for operational functionality.

---

## 2. Objectives

- Maintain component temperatures within operational and survival ranges
- Handle orbital thermal cycling (eclipse and sunlit phases)
- Protect electronics, sensors, joints, and mechanical links
- Interface reliably with ISS power and telemetry systems
- Support fault-tolerant thermal control

---

## 3. System Context

Canadarm2 operates on the exterior of the ISS, exposed to:

- Vacuum and microgravity
- Large temperature swings (–150°C to +120°C)
- Limited conductive paths
- Radiative-only heat rejection to space or optional ISS radiator coupling

---

## 4. 🔧 Thermal Control Strategy

### 4.1 Passive Control Methods
- **Multi-Layer Insulation (MLI):** Reduces radiative heat transfer between components and to space.
- **Thermal Coatings:** Surface treatments to control absorptivity/emissivity ratios.
- **Component Placement:** Optimize layout to isolate thermally sensitive hardware.
- **Thermal Isolation Mounts:** Prevent unwanted conduction from hot to cold components.
- **Heat Pipes / Thermal Straps (if applicable):** Conduct heat from hot areas to radiative surfaces.

### 4.2 Active Control Methods
- **Resistive Heaters:** Used in joints, electronics boxes, and end effectors.
- **Temperature Sensors (RTDs/Thermistors):** Monitor local temperatures in real time.
- **Control Logic:** Simple on/off control or PID regulation based on sensor input.
- **Power Management:** Draws 28V DC from ISS power bus, with defined max draw limits.
- **Health Monitoring:** Heater current and temperature profiles logged via telemetry.

---

## 5. 🔩 Key Components in the Thermal Network

| Component                  | Thermal Strategy              | Notes                                   |
|---------------------------|-------------------------------|-----------------------------------------|
| **Boom Segments**         | Passive (coating, MLI)        | Minimal heat generation                 |
| **Rotary Joints**         | Active + Passive              | Heaters, sensors, and insulation        |
| **Electronics Modules**   | Active                        | Tight thermal limits, controlled zones  |
| **Latching End Effector** | Active + Thermal isolation    | Operates in contact with external loads |
| **Harness & Cabling**     | Passive                       | Routed with thermal/mechanical restraint|
| **Power/Thermal Buses**   | Interface-Linked              | Shares power and status with ISS        |

---


## 6. Functional Thermal Flow

This high-level functional sequence represents the sensing, control, and actuation loop of the thermal system:

- [SENSE THERMAL ENVIRONMENT]
  - ↓
- [ANALYZE THERMAL STATE]
  - ↓
- [CONTROL HEATERS & MLI]
  - ↓
- [MANAGE POWER BUDGET]
  - ↓
- [VERIFY SYSTEM HEALTH]
  - ↓
- [EXCHANGE DATA WITH ISS]
  - ↓
- [REPORT STATUS & FAULTS]

*Note: Arrows indicate the flow of operations, with feedback loops implied (e.g., from VERIFY SYSTEM HEALTH to ANALYZE THERMAL STATE).*

## 7. Thermal Interfaces

| Interface ID    | Description                              |
|-----------------|------------------------------------------|
| IF-THERM-001    | Conductive path to ISS Radiator (optional mount point) |
| IF-THERM-002    | Radiative interface to deep space (primary heat sink) |
| IF-THERM-003    | Internal joint contact interfaces (thermal continuity paths) |

### Additional Components

| Component            | Thermal Strategy | Notes                             |
|----------------------|------------------|-----------------------------------|
| Harness & Cabling    | Passive          | Routed with thermal/mechanical restraint |
| Power/Thermal Buses  | Interface-Linked | Shares power and status with ISS  |
---

## 8. Verification and Testing

- **Thermal Vacuum Testing (TVAC):** Verify performance in simulated LEO vacuum.
- **Orbital Simulation (MATLAB/Python):** Simulate thermal transients due to orbit cycling.
- **Power Budget Simulation:** Ensure heaters operate within power limits (≤50 W).
- **Fault Injection Testing:** Evaluate behavior under heater or sensor fault conditions.

---

## 9. Compliance and Standards

- **CSA/NASA Thermal Design Guidelines**
- **ECSS-E-TM-10-21A** – Thermal analysis and verification methodology
- **MIL-STD-1540** – Environmental testing for aerospace hardware

---

## 10. Summary

The Canadarm2 Thermal Architecture ensures robust and redundant thermal regulation through a combination of passive and active methods tailored for the dynamic space environment. The architecture balances temperature control with power efficiency and fault resilience, enabling safe and reliable operations throughout orbital cycles and mission phases.

---

**Author:** Soniya Purushothaman  
**Date:** June 2025  
**Version:** 1.0  
