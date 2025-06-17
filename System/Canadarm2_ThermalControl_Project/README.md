# Canadarm2 Thermal Control System Project

## 🛰️ Overview
This project models and analyzes the thermal control system for Canadarm2, focusing on:

- Passive and active thermal regulation strategies
- Orbit-induced environmental loads
- Simulation of transient and steady-state temperatures
- Verification against defined performance requirements

It follows a **Systems Engineering lifecycle** from requirements to testing.

---

## 📁 Project Structure

| Folder | Description |
|--------|-------------|
| `01_Requirements/` | Contains system and thermal performance requirements |
| `02_Architecture/` | Functional, logical, and physical system architecture |
| `03_Design/` | Detailed thermal design, component specs, trade studies |
| `04_Modeling_Simulation/` | Python scripts, models, inputs, outputs |
| `05_Verification_Validation/` | Test plans, verification matrix, simulation validation |
| `06_Documentation/` | ConOps, risk register, change log, presentations |
| `07_References/` | Research papers, standards, handbooks |

---

## 📋 High-Level System Requirements

### 1. General System Requirements

**REQ-001:**  The Thermal Control System (TCS) shall maintain all Canadarm2 critical components within specified temperature limits during all mission phases, including nominal operations, standby, and maneuvers.

**REQ-002:**  The TCS shall operate effectively under the thermal environment experienced in Low Earth Orbit (LEO) aboard the ISS, accounting for orbital sunrise/sunset cycles (~90-minute period).

**REQ-003:**  The TCS shall provide both active and passive thermal control methods, including heaters, radiators, insulation, and thermal coatings, to manage temperature fluctuations.

**REQ-004:**  The TCS shall interface with Canadarm2’s Command and Data Handling system to allow monitoring and control of thermal states.

### 2. Environmental and Thermal Loads

**REQ-005:**  The TCS shall be designed to handle external thermal loads from solar radiation, Earth albedo, and Earth infrared radiation as per ISS orbital parameters.

**REQ-006:**  The TCS shall accommodate induced thermal loads caused by internal heat dissipation from Canadarm2 electronics, motors, and actuators.

**REQ-007:**  The TCS shall withstand and maintain functionality during thermal vacuum conditions as expected in the ISS environment.

### 3. Performance and Safety

**REQ-008:**  The system shall maintain critical component temperatures within a safe range, typically between -40°C and +60°C, unless otherwise specified by subsystem requirements.

**REQ-009:**  The TCS shall provide real-time temperature data with a resolution of at least ±1°C for thermal management decisions.

**REQ-010:**  The system shall automatically adjust heater power or other active controls to prevent overcooling or overheating without manual intervention.

### 4. Verification and Validation

**REQ-011:**  The TCS design shall be validated through thermal analysis simulations and thermal vacuum (TVAC) testing replicating LEO conditions.

**REQ-012:**  Thermal performance test plans shall include transient and steady-state conditions replicating orbital thermal cycles.

### 5. Interfaces and Constraints

**REQ-013:**  The TCS hardware shall be compatible with existing Canadarm2 mechanical interfaces and electrical power budgets.

**REQ-014:**  The system shall comply with ISS safety and operational standards, including electromagnetic compatibility and controlled goods regulations.

See detailed breakdown in the following markdown files:

- [`System_Requirements_Spec.md`](01_Requirements/System_Requirements_Spec.md)
- [`Thermal_Performance_Requirements.md`](01_Requirements/Thermal_Performance_Requirements.md)
- [`Interface_Requirements.md`](01_Requirements/Interface_Requirements.md)

---

## 🚀 Key Objectives

- Develop a thermal node model of Canadarm2 using Python
- Implement heater control logic (on/off or PID)
- Validate performance during orbital transitions
- Integrate system engineering practices throughout

---

## 🧰 Tools & Libraries

- Python (NumPy, Matplotlib, SciPy)
- Thermal Desktop (optional reference)
- Draw.io / Cameo for architecture diagrams

---

## 📌 How to Run Simulations

```bash
cd 04_Modeling_Simulation/Scripts
python thermal_simulation.py
```

Simulation results will appear in the `Outputs/` folder.

---

## 📋 Status

- [x] Requirements defined
- [ ] Architecture completed
- [ ] Simulation model in progress
- [ ] Initial verification plan drafted

---

## 🧠 Author: Soniya Purushothaman
Email: Soniya.purushothaman2022@gmail.com  
LinkedIn: www.linkedin.com/in/soniya-purushothaman  
Gitlab: https://gitlab.com/SoniyaLeo



Feel free to contribute or fork this project for your own research or coursework.
