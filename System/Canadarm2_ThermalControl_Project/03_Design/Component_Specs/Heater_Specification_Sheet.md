# Heater Specification Sheet

## 1. Overview

This document outlines the specifications for surface-mounted Kapton heaters used in the Canadarm2 Thermal Control System. These heaters maintain component temperatures within operational limits during orbital variations.

---

## 2. Heater Type

- **Type:** Polyimide Film Heater (Kapton)
- **Configuration:** Surface mount (flexible)
- **Form Factor:** Flat rectangular film

---

## 3. Performance Specifications

| Parameter           | Value                       |
|---------------------|-----------------------------|
| Operating Voltage   | 28 V DC                     |
| Power Rating        | 5–20 W per heater           |
| Temperature Range   | -100°C to +150°C            |
| Resistance Tolerance| ±10%                        |
| Watt Density        | 0.5–2.0 W/cm²               |
| Thermal Response    | <10 seconds to reach 50°C   |

---

## 4. Electrical Characteristics

| Parameter              | Specification              |
|------------------------|----------------------------|
| Interface              | 2-pin or 4-pin harness     |
| Connectors             | Micro-D (flight-rated)     |
| EMI Shielding          | Integrated via braid       |
| Wire Harness           | Teflon-insulated, 26 AWG   |
| Safety Features        | Overcurrent cutoff relay   |

---

## 5. Mechanical Form Factor

- **Dimensions:** 50 × 50 mm to 100 × 100 mm (customizable)
- **Weight:** < 50 grams per unit
- **Adhesive Backing:** Space-rated acrylic adhesive
- **Bend Radius:** >10 mm (flex-tolerant)

---

## 6. Environmental Compliance

| Property              | Value / Standard                  |
|------------------------|----------------------------------|
| Outgassing             | ASTM E595 compliant              |
| Radiation Tolerance    | 50 krad (total ionizing dose)    |
| Vibration              | 14.1 g RMS (per NASA GEVS)       |
| Thermal Cycling        | ±125°C for 200 cycles            |

---

## 7. Integration Notes

- Mount directly to high thermal mass components
- Use in conjunction with thermal insulation (MLI)
- Routed to heater controller via spacecraft harness
- Controlled via bang-bang or PID logic (refer to control doc)

---

## 8. Compliance & Standards

- NASA GEVS-compliant
- CSA Thermal Component Standards
- RoHS & REACH Certified

---

**Prepared by:** Soniya Purushothaman  
**Date:** June 2025  
**Project:** Canadarm2 Thermal Control System  
