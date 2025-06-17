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

## 4. Thermal Control Strategy

### 4.1 Passive Elements

- **Multi-Layer Insulation (MLI):** Reduces radiative heat exchange
- **Surface Coatings (e.g., optical white paint):** Controls absorptivity/emissivity
- **Thermal Straps:** Conductive link between hot/cold components
- **Design Placement:** Minimizes gradient stress between segments

### 4.2 Active Elements

- **Resistive Heaters:** Mounted on critical components (joints, electronics)
- **Thermistors/RTDs:** Sense local temperatures
- **Control Logic:** On/off or PID-based thermal control algorithm
- **Power Management:** Uses 28V DC supply from ISS via Canadarm2 power interface

---

## 5. Key Components in Thermal Network

| Component | Thermal Role |
|-----------|--------------|
| **Latching End Effector (LEE)** | Heaters + insulation due to joint activity |
| **Boom Links** | Mostly passive, MLI-covered |
| **Electronics Boxes** | Actively controlled with sensor feedback |
| **Cables & Harness** | Routed thermally and mechanically for minimal gradients |

---

## 6. Functional Thermal Flow

```plaintext
[SUN EXPOSURE] → [MLI & SURFACE COATINGS] → [THERMAL STRAPS] → [TEMP SENSORS]
                           ↓
                     [CONTROL LOGIC]
                           ↓
                   [HEATER ON/OFF CONTROL]
