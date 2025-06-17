# Canadarm2_Thermal_modeling_and_control
Canadarm2 Thermal Modeling and Control :-This project simulates a simplified thermal control system for a space robotic arm, inspired by Canadarm2. It demonstrates conceptual design, component sizing, and verification methods for space-based thermal systems.
# Canadarm2 Thermal Modeling and Control

This project simulates a simplified thermal control system for a space robotic arm, inspired by Canadarm2. It demonstrates conceptual design, component sizing, and verification methods for space-based thermal systems.

---

## 📌 Project Objectives

- Model heat transfer in robotic arm segments exposed to orbital thermal cycles.
- Simulate passive and active thermal control strategies (radiators + heaters).
- Generate temperature history curves and verify thermal limits compliance.
- Propose a simple TVAC test plan for hardware validation.

---

## 🛠 Technologies Used

- **Python** for simulation scripting
- **NumPy**, **Matplotlib**, and **SciPy** for analysis
- **CAD mockups** in PNG (future integration with NX CAD)
- **Excel** for verification matrix
- TVAC test plan in Markdown & DOCX

---

## 🔧 Modules Overview

- `thermal_simulation.py`: Simulates transient thermal behavior using orbital parameters.
- `heater_control.py`: Controls heater ON/OFF based on thermal thresholds.
- `parameters.py`: Stores constants like emissivity, heater power, and node areas.
- `utils.py`: Utility functions for plotting, logging, and formatting.

---

## 📈 Simulation Outputs

- **Temperature curves** for each joint/node
- **Heat flux plots** showing radiative loss and heater input
- **Thermal balance summary** with predicted min/max temps

---

## 📋 Test & Verification Artifacts

- ✅ Thermal vacuum test procedure with expected results
- ✅ Verification matrix linking temperature limits to subsystem needs
- ✅ Summary of assumptions and test configurations

---

## 📂 Sample Results

<p align="center">
  <img src="figures/temperature_plot.png" width="600" />
</p>

---

## ✨ Future Work

- Integrate with real CAD thermal nodes from  Thermal Desktop
- Model shadowing and ISS albedo effects
- Introduce ML-based temperature prediction for heater control

---

## 📧 Contact

Author: Soniya P.  
Email: Soniya.purushothaman2022@gmail.com  
LinkedIn: www.linkedin.com/in/soniya-purushothaman
gitlab:https://gitlab.com/SoniyaLeo

