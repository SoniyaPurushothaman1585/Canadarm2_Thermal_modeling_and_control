# Canadarm2 Thermal Control System

## Functional Architecture

This document outlines the high-level and decomposed functional architecture of the Canadarm2 Thermal Control System, developed following a systems engineering approach.

---

## 🎯 Top-Level System Function

**Function:**
> Maintain Safe Operating Temperatures for Canadarm2 Components During Orbit

---

## 🔧 Primary Functional Decomposition

| Function ID | Function Name                         | Description |
|-------------|----------------------------------------|-------------|
| F-01        | Sense Thermal Environment              | Monitor internal and external temperatures, orbital parameters |
| F-02        | Analyze Thermal State                  | Compare sensed data to thresholds and profiles |
| F-03        | Control Heaters/MLI                    | Activate heaters or switch states based on control logic |
| F-04        | Exchange Data with ISS                 | Send telemetry and receive commands from ISS |
| F-05        | Manage Power Allocation                | Distribute and limit heater power based on mission limits |
| F-06        | Verify System Health                   | Perform self-checks and fault detection |
| F-07        | Report Status & Alarms                 | Generate system messages and trigger alerts if anomalies occur |

---

## 🧮 Subfunction Example – F-03: Control Heaters

| Subfunction ID | Description |
|----------------|-------------|
| F-03.1         | Implement Control Algorithm (PID/on-off) |
| F-03.2         | Enable/Disable Individual Heater Zones |
| F-03.3         | Log Heater State and Duration |

---

## 🔄 Functional Flow (Logical Sequence)

```text
[Sense Thermal Environment]
        ↓
[Analyze Thermal State] ──→ [Verify System Health]
        ↓
[Control Heaters/MLI] ──→ [Manage Power Allocation]
        ↓
[Report Status & Alarms] ←─ [Exchange Data with ISS]
```

---

## 📎 Notes
- This architecture supports mapping to system and thermal requirements.
- Functional interactions can be modeled in SysML or simulated for flow validation.
- Future versions will include logical and physical architectures.
