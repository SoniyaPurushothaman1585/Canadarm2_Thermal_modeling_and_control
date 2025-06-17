# 🧠 Control Strategy Design – Canadarm2 Thermal System

## 1. Control Goals
- Maintain thermal zones within operational limits (e.g., -20°C to +45°C)
- Ensure minimal heater overshoot/undershoot
- Optimize power consumption (≤50W total for heaters)

---

## 2. Control Logic

### 🔁 Primary Strategy:
- **Bang-Bang Control** (on/off control) with ±2°C hysteresis
- Example: 
  - Heater ON when temp < 20°C
  - Heater OFF when temp > 22°C

### 🧠 Rule-Based Overrides:
- **Pre-Heating**: Activate heaters before orbital sunrise based on predicted ephemeris
- **Safety Interlocks**:
  - Disable heater on sensor failure
  - Auto shutoff during high current draw
- **Telemetry Commands**: Allow manual override from ground or ISS

---

## 3. Fault Handling

| Fault Condition             | Action Taken                               |
|----------------------------|---------------------------------------------|
| Sensor discrepancy (>±5°C) | Trigger majority vote or switch to backup   |
| Heater overcurrent         | Auto-disconnect via relay + fault flag      |
| Unresponsive sensor        | Trigger fault mode, disable affected loop   |
| Communication loss         | Default to safe thermal biasing             |

- Redundant sensors deployed in critical areas (e.g., joint motors)
- Fault logs stored and downlinked every 5 minutes via telemetry

---

## 4. Control Loop Parameters
- **Sampling Rate**: 1 Hz (every second)
- **Command Latency**: < 0.5 s to heater relay
- **Telemetry Rate**: 0.2 Hz (every 5 seconds)
- **Data Logged**: Timestamp, node temps, heater states, fault flags

---

## 5. Diagram
```
[Sensors] ──► [Temp Reading] ──► [Bang-Bang Logic + Rules] ──► [Heater Command]
│                                │                             │
└────► [Fault Detection] ◄───────┘                             ▼
[Telemetry + Override Channel] ◄──── [ISS]
```
*Note: This diagram illustrates the control loop, with arrows indicating data and command flow, and feedback loops for fault detection.*

---

## 6. Optimization Considerations
- Use of **thermal mass** and **MLI** to reduce heater cycles
- Power allocation scheme prioritizes survival-critical zones
- Heater duty cycle logging for predictive maintenance

---

## 7. Future Improvements
- PID control testing (using filtered derivative to minimize noise)
- Adaptive thresholds based on orbital phase (day/night)
- Machine-learning-based thermal prediction (optional long-term study)

---

**Prepared by:** Soniya Purushothaman  
**Date:** June 17, 2025  
**Project:** Canadarm2 Thermal Control Design