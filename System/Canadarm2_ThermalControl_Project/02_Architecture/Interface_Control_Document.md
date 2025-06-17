# Interface Control Document (ICD) – Canadarm2 Thermal Control System

## 1. Purpose
This Interface Control Document (ICD) defines all critical interfaces between the Canadarm2 Thermal Control System and external/internal systems. It supports configuration management, subsystem integration, and verification.

---

## 2. Scope
Applies to the active/passive thermal control elements of Canadarm2 that operate aboard the International Space Station (ISS), including heaters, sensors, and structural thermal paths.

---

## 3. Interface Categories

### 3.1 Mechanical Interfaces

| Interface ID | Description | Source | Receiving Component | Notes |
|--------------|-------------|--------|----------------------|-------|
| IF-MECH-001  | Thermal straps/coupling to structural joints | Joint structure | Thermal bus | Aluminum/copper conduction paths |
| IF-MECH-002  | Mounting of thermal sensors and heaters | Robotic arm segments | Sensors/heaters | Bonded or screw-mounted, must survive vibration and vacuum |
| IF-MECH-003  | Multi-Layer Insulation (MLI) blankets | Canadarm2 surface | External space | Designed for EVA compatibility and debris resilience |

---

### 3.2 Electrical Interfaces

| Interface ID | Description | Power Spec | Connector | Notes |
|--------------|-------------|------------|-----------|-------|
| IF-ELEC-001  | Power supply for heaters | 28V DC | MIL-DTL-38999 | Shared with subsystem power bus |
| IF-ELEC-002  | Heater control lines | 28V DC command | Custom bus | Controlled via main avionics controller |
| IF-ELEC-003  | Sensor signal routing | Analog or digital | Shielded twisted pair | Routed through ISS telemetry harness |

---

### 3.3 Data Interfaces

| Interface ID | Description | Protocol | Source | Destination |
|--------------|-------------|----------|--------|-------------|
| IF-COM-001   | Thermal telemetry uplink | ISS Bus (1553B or Ethernet) | Canadarm2 sensors | Ground/ISS computers |
| IF-COM-002   | Command interface for heaters | Telecommand packets | Ground control | On-board heater controller |
| IF-COM-003   | Fault detection/status reporting | CCSDS packets | TCS module | Ground crew and astronauts |

---

### 3.4 Thermal Interfaces

| Interface ID | Description | Type | Conductive/Convective | Comments |
|--------------|-------------|------|------------------------|----------|
| IF-THERM-001 | Heat dissipation to ISS radiators | Passive | Conductive | Optional through arm bracket link |
| IF-THERM-002 | Radiative emission to space | Passive | Radiative | MLI design must optimize view factors |
| IF-THERM-003 | Internal conduction path between joints | Passive | Conductive | Controlled using contact resistance material |

---

## 4. Interface Verification Methods

| Interface ID | Verification Method |
|--------------|---------------------|
| IF-MECH-001 to 003 | Visual inspection, vibration test, fit-check |
| IF-ELEC-001 to 003 | Continuity check, power-on test, EMI/EMC |
| IF-COM-001 to 003  | Simulated command test, telemetry injection |
| IF-THERM-001 to 003| Thermal vacuum test, heat path simulation |

---

## 5. Change Control
All interface changes must be reviewed through the Interface Control Working Group (ICWG) and documented in the change log (see `/06_Documentation/Change_Log.md`).

---

**Author:** Soniya Purushothaman  
**Date:** June 2025  
**Version:** 1.0  
