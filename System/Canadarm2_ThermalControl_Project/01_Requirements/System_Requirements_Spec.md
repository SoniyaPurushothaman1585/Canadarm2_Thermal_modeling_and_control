# System Requirements Specification (SRS) — Canadarm2 Thermal Control System

## 1. Introduction
This document defines the top-level functional and non-functional requirements for the Thermal Control System (TCS) of Canadarm2, supporting its operation on the ISS.

## 2. System Context
Canadarm2 operates in Low Earth Orbit (LEO) aboard the ISS, exposed to alternating sunlight and eclipse conditions every ~90 minutes.

## 3. High-Level System Requirements

| ID | Requirement Description |
|----|--------------------------|
| SYS-001 | The TCS shall maintain operational component temperatures within specified limits throughout the orbital cycle. |
| SYS-002 | The system shall provide passive and active thermal control strategies to regulate temperature. |
| SYS-003 | The TCS shall interface with onboard power and telemetry systems of the ISS. |
| SYS-004 | The TCS shall function in vacuum and microgravity conditions. |
| SYS-005 | The system shall detect thermal excursions and enable corrective actions (e.g., heaters). |
| SYS-006 | The TCS design shall conform to NASA/CSA thermal subsystem standards. |

## 4. Assumptions
- ISS orbit: ~400 km altitude, ~90-minute period.
- External heat sources: solar radiation, albedo, IR radiation from Earth.
- Internal heat generation from electronic components.

## 5. Verification Methods
- Analysis, Inspection, Demonstration, and Test (AIDT).

