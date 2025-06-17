# Thermal Sensor Specification Sheet

## 1. Overview

This document specifies the key characteristics of the thermal sensors to be used in the Canadarm2 Thermal Control System. These sensors are critical for real-time monitoring of component temperatures to ensure reliable thermal regulation in orbit.

---

## 2. Sensor Type

- **Type:** Platinum Resistance Thermometer (RTD) or Thermistor
- **Recommended Model:** PT1000 (RTD) / NTC 10kΩ (Thermistor)

---

## 3. Performance Specifications

| Parameter             | Specification                         |
|-----------------------|----------------------------------------|
| Operating Temperature | -100°C to +125°C                       |
| Accuracy              | ±0.5°C typical                         |
| Stability             | ±0.1°C per year                        |
| Response Time         | < 1.5 seconds (in air)                 |
| Resolution            | 0.1°C                                  |
| Self-Heating Effect   | < 0.1°C (with ≤1mA excitation current) |

---

## 4. Electrical Interface

| Feature           | Specification             |
|-------------------|----------------------------|
| Output Type       | Analog voltage or I2C      |
| Excitation Current| 1 mA max                   |
| Supply Voltage    | 3.3V or 5V (depending on model) |
| Wiring            | 2-wire or 4-wire RTD       |
| EMI Shielding     | Yes (space-rated harness)  |

---

## 5. Mechanical Form Factor

| Attribute        | Value                              |
|------------------|-------------------------------------|
| Sensor Body      | Bead or cylindrical probe           |
| Size             | 3mm bead or 25mm × 3mm probe        |
| Cable Type       | Teflon-insulated, low-outgassing    |
| Connector        | Micro-D for flight hardware         |
| Mounting Option  | Adhesive-backed or bracket mount    |

---

## 6. Environmental Compatibility

- **Radiation Tolerance:** 50 krad
- **Vibration Tolerance:** 15g RMS
- **Thermal Cycling:** ±125°C, 200 cycles
- **Outgassing Compliance:** ASTM E595 qualified

---

## 7. Compliance & Standards

- NASA GEVS
- CSA Spaceflight Hardware Standard
- RoHS & REACH Compliant

---

## 8. Notes

- Sensor should be thermally bonded to component surface using space-grade adhesive or mechanical mount.
- Redundant sensors may be placed at critical nodes (e.g., joints, electronics bays).

---

**Prepared by:** Soniya Purushothaman  
**Date:** June 2025
