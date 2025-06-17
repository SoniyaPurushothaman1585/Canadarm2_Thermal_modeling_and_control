# Functional Decomposition – Canadarm2 Thermal Control System

## 1. Purpose
This document decomposes the top-level function of the Canadarm2 Thermal Control System into hierarchical functional blocks. It supports traceability to system requirements and architecture modeling, guiding simulation and implementation.

---

## 2. Top-Level Function
**Maintain Thermal Stability for Canadarm2 Subsystems During ISS Orbit Operations**

This includes maintaining component temperatures within operational limits, minimizing thermal gradients, and ensuring system survivability during orbital transitions.

---

## 3. Functional Hierarchy

### 3.1 Level 0 – Mission Function
- Maintain Thermal Stability for Canadarm2

### 3.2 Level 1 – Primary Functions
| Function ID | Function Name                | Description |
|-------------|------------------------------|-------------|
| F-01        | Sense Thermal Environment     | Detect temperatures using sensors located across the robotic arm |
| F-02        | Analyze Thermal Data          | Convert raw sensor data into actionable thermal states (e.g., underheating, overheating) |
| F-03        | Control Thermal Devices       | Activate heaters, adjust MLI coverage, or command operational modes |
| F-04        | Manage Power Resources        | Allocate electrical power to heaters efficiently |
| F-05        | Exchange Telemetry            | Send and receive data to/from the ISS avionics and telemetry systems |
| F-06        | Verify System Health          | Monitor thermal system performance and detect faults or excursions |
| F-07        | Report Status                 | Generate alarms or periodic thermal status for ground/ISS teams |

---

### 3.3 Level 2 – Supporting Subfunctions

| Function ID | Subfunction                   | Parent Function | Description |
|-------------|-------------------------------|------------------|-------------|
| F-01.1      | Acquire Temperature Data       | F-01             | Poll temperature sensors located at joints, electronics, and external surfaces |
| F-02.1      | Compare to Thresholds          | F-02             | Compare readings against operating thresholds |
| F-03.1      | Heater Activation              | F-03             | Send ON/OFF or PID commands to heater circuits |
| F-03.2      | MLI Configuration Control      | F-03             | Adjust MLI positioning (if active or deployable) |
| F-04.1      | Monitor Power Budget           | F-04             | Check available power vs. system demand |
| F-06.1      | Fault Detection                | F-06             | Identify abnormal trends or component failures |
| F-07.1      | Generate Thermal Reports       | F-07             | Package data for downlink or crew displays |

---

## 4. Inputs and Outputs

| Function         | Inputs                                   | Outputs                                |
|------------------|------------------------------------------|----------------------------------------|
| F-01 Sense       | Orbital environment, component temp      | Raw thermal data                       |
| F-02 Analyze     | Raw thermal data                         | Status: Normal, Warning, Critical      |
| F-03 Control     | Status, command logic                    | Heater commands, MLI control signals   |
| F-04 Manage Power| Power availability, system priority      | Allocated power levels                 |
| F-05 Exchange    | ISS telemetry commands                   | System state, heater data              |
| F-06 Verify      | Sensor data, command feedback            | Health flags, diagnostic results       |
| F-07 Report      | Diagnostic results, system state         | Alerts, formatted status reports       |

---

## 5. Notes

- This decomposition supports modular system implementation and aligns with both simulation and hardware integration phases.
- The functions listed here trace directly to requirements in the `System_Requirements_Spec.md` and `Thermal_Performance_Requirements.md`.

---

**Author:** Soniya Purushothaman  
**Date:** June 2025
