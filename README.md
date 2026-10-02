# Sign-Language Educational Robotic Hand

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23102292.svg)](https://doi.org/10.5281/zenodo.23102292)

**Bachelor Thesis — Mechanical Engineering, Robotics & Mechatronics**

A physical robotic-hand prototype for sign-language education, developed by extending a commercial **Hiwonder uHandPi** platform with a custom **cable-driven compliant continuum wrist**, multibody simulation, additive manufacturing, Raspberry Pi servo control, and a preliminary vision-based sign-selection proof of concept.

> **Status:** Completed bachelor thesis prototype  
> **Academic year:** 2023–2024  
> **Institution:** National Polytechnic University of Armenia  
> **DOI:** [10.5281/zenodo.23102292](https://doi.org/10.5281/zenodo.23102292)

![Final physical prototype](media/prototype/final_prototype.jpg)

---

## At a Glance

| | |
|---|---|
| **Problem** | The original robotic-hand platform had limited wrist mobility for sign-language demonstrations |
| **Main contribution** | Mechanical redesign and physical implementation of a cable-driven compliant continuum wrist |
| **Hardware** | Hiwonder uHandPi, Raspberry Pi 4, servo motors, 3D-printed wrist |
| **Mechanical tools** | SolidWorks, MSC Adams, Ultimaker Cura |
| **Programming** | Python, Raspberry Pi GPIO/PWM, adapted gesture-to-sign mapping |
| **Manufacturing** | PLA, TPU, tendon/fishing-line actuation |
| **Result** | Working physical prototype with actuated continuum wrist |
| **Vision work** | Existing gesture detector adapted as a limited sign-selection proof of concept |
| **Not completed** | General sign-language recognition, learner feedback, closed-loop continuum control, formal user study |

---

# Project Overview

This bachelor thesis investigated how a low-cost physical robotic-hand platform could be mechanically extended for **sign-language demonstration and education**.

Rather than designing an entire dexterous robotic hand from scratch, the commercially available **Hiwonder uHandPi** was used as the starting platform.

The existing platform already provided:

- the five-finger robotic hand
- finger servo actuation
- Raspberry Pi electronics
- camera hardware
- existing Python control software
- existing computer-vision demonstrations

My main engineering focus was the mechanical limitation of the original lower manipulator and wrist.

I removed the original lower manipulator and designed a **custom cable-driven compliant continuum wrist** intended to provide a larger and smoother range of wrist orientations while remaining relatively simple, inexpensive and manufacturable.

The overall engineering workflow was:

```text
Problem Definition
        ↓
Mechanical Redesign
        ↓
SolidWorks CAD
        ↓
Continuum-Wrist Modelling
        ↓
MSC Adams Simulation
        ↓
Material Selection
        ↓
3D Printing
        ↓
Physical Assembly
        ↓
Raspberry Pi / Servo Control
        ↓
Physical Testing
```

The project should therefore be understood primarily as a **mechanical and mechatronics prototype**, rather than as a completed sign-language-recognition system.

---

# My Contributions

My primary thesis work included:

- redesign of the original uHandPi lower manipulator
- design of the cable-driven compliant continuum wrist
- design of four custom wrist sections
- compliant-backbone integration
- tendon-routing design
- SolidWorks CAD and assembly integration
- engineering drawing preparation
- study of continuum-manipulator kinematics and dynamics
- MSC Adams multibody simulation
- material selection
- PLA and TPU additive manufacturing
- physical prototype assembly
- tendon and servo integration
- Raspberry Pi control of the two wrist-actuation servos
- physical testing of the continuum-wrist motion
- adaptation of existing gesture-recognition logic as a sign-selection proof of concept

---

# Mechanical Redesign

## Original Platform

The starting point was the commercially available **Hiwonder uHandPi Raspberry Pi robotic hand**.

The hand and finger actuation were retained, while the original lower manipulator was removed.

The original configuration limited the wrist orientations available to the hand. Since wrist orientation contributes to the appearance of many sign-language gestures, the lower section was redesigned to investigate a more compliant form of movement.

---

## Original vs Redesigned System

![Original uHandPi and redesigned system](media/cad/design_comparison.jpg)

The redesigned system introduced:

- four rounded continuum-wrist sections
- a flexible central backbone
- tendon / cable actuation
- two servo motors
- custom support geometry
- a new base / electronics enclosure
- integration with the existing uHandPi hand

---

# Cable-Driven Continuum Wrist

The redesigned wrist consists of four serially arranged sections connected through a compliant structure.

```text
uHandPi Hand
     │
     ▼
┌───────────┐
│ Section 1 │
├───────────┤
│ Section 2 │
├───────────┤
│ Section 3 │
├───────────┤
│ Section 4 │
└───────────┘
     │
     ▼
Flexible Backbone
     │
     ▼
Tendon Actuation
     │
     ▼
Servo Motors
```

Unlike a conventional rigid wrist whose movement occurs at discrete revolute joints, the redesigned mechanism distributes bending through a compliant structure.

The design was selected to investigate:

- continuous compliant bending
- increased wrist-orientation range
- relatively low mechanical complexity
- low-cost tendon actuation
- compatibility with additive manufacturing
- integration with the existing robotic hand

It is important to distinguish **continuous deformation** from actuation degrees of freedom.

Although a continuum mechanism distributes deformation along its structure, the physical prototype is actuated by a finite number of servo-driven tendon inputs.

---

## Tendon Arrangement

The prototype uses **eight physical tendon runs**.

For conceptual modelling, these were grouped into effective actuation directions.

Fishing line was used as a low-cost tendon material during prototyping.

Two servo motors actuated the tendon mechanism and produced bending of the continuum wrist.

The actuation chain can be represented as:

```text
Servo Motion
      ↓
Tendon Displacement
      ↓
Compliant Deformation
      ↓
Wrist Bending
      ↓
Hand Orientation
```

The prototype used predefined servo commands and did not implement closed-loop tendon-tension or shape control.

---

# CAD Design

The modified system was designed and assembled in **SolidWorks**.

My CAD work included:

- continuum-wrist sections
- compliant-backbone arrangement
- tendon-routing geometry
- wrist-to-hand connection
- support structure
- base / electronics enclosure
- complete modified assembly

Virtual assembly was used to inspect component positioning, clearances and possible mechanical interference before physical manufacturing.

## Assembly Overview

![Final robotic-hand CAD assembly](media/cad/assembly_render.jpg)

## Technical Drawing

![SolidWorks technical drawing](media/cad/technical_drawing.png)

Native SolidWorks files are stored under:

```text
cad/solidworks/
```

Neutral CAD exports are provided in both formats:

```text
cad/exports/
├── RoboticHand.stp
└── RoboticHand.x_t
```

This allows the geometry to be accessed without requiring the original SolidWorks environment.

---

# Continuum-Wrist Modelling

The main modelling focus of the thesis was the newly designed continuum wrist.

The existing uHandPi fingers form separate mechanical branches and were not treated as consecutive links of a single serial Denavit-Hartenberg chain.

The continuum wrist was instead considered through three conceptual spaces:

```text
Actuation Space
(tendon displacement)
        ↓
Configuration Space
(curvature / orientation)
        ↓
Operational Space
(hand pose)
```

Changes in tendon displacement cause deformation of the compliant wrist and therefore modify the position and orientation of the attached hand.

---

## Differential Kinematics

Differential kinematics was studied as a framework for relating changes in actuation to changes in end-effector motion.

Conceptually:

```text
Tendon Velocities
        ↓
Configuration-Space Velocity
        ↓
Jacobian Relationship
        ↓
End-Effector Velocity
```

This modelling provides a basis for more advanced closed-loop continuum control.

A complete Jacobian-based closed-loop controller was **not implemented** in the bachelor-thesis prototype.

---

# Dynamic Modelling and MSC Adams Simulation

The mechanical analysis considered physical properties affecting the redesigned wrist, including:

- component mass
- inertia
- centres of mass
- gravity
- compliant behaviour
- damping and friction
- tendon forces
- servo actuation

The goal was to understand the expected mechanical response of the redesigned system rather than to perform a formal structural certification.

---

## MSC Adams

The robotic hand and continuum wrist were modelled in **MSC Adams** for multibody dynamic simulation.

The simulation was used to inspect system behaviour including:

- hand position
- angular response
- angular velocity
- kinetic energy
- overall mechanism motion

The Adams work is therefore presented as **multibody dynamic simulation**, not as finite-element stress certification.

### Simulation Demonstration

[Watch the MSC Adams wrist simulation](media/demos/adams_wrist_simulation.avi)

> The simulation recording is stored as an AVI file and may need to be downloaded locally for playback depending on the browser.

The recovered MSC Adams model files are available under:

```text
simulation/adams/
├── Jessica_Robot.bin
└── MODEL_hand.bin
```

These files are preserved as original project artefacts from the bachelor thesis.

---

# Material Selection and Manufacturing

Material selection was based primarily on the mechanical role of each component.

## PLA

PLA was used for the four rigid wrist sections.

The material provided sufficient rigidity for the structural sections while remaining inexpensive and easy to manufacture using fused-filament fabrication.

The complete set required more than ten hours of printing.

## TPU

TPU was used for the flexible backbone because the mechanism required controlled compliance during wrist bending.

The backbone required approximately two hours of printing.

## Tendons

Fishing line was used as the tendon material because it was:

- lightweight
- inexpensive
- readily available
- suitable for transmitting tensile force during prototype testing

The custom components were prepared using **Ultimaker Cura** and manufactured using a **Creality Ender 3**.

---

# Physical Assembly

The final prototype combined:

- rigid PLA wrist sections
- TPU compliant backbone
- mechanical fasteners
- fishing-line tendons
- two servo motors
- Raspberry Pi electronics
- the retained uHandPi robotic hand

## Final Prototype

![Completed physical robotic-hand prototype](media/prototype/final_prototype.jpg)

The project therefore progressed beyond CAD and simulation to a complete physical mechatronics prototype.

---

# Wrist Control

The custom continuum wrist was controlled separately from the original uHandPi finger-control software.

A **Raspberry Pi 4 Model B** was used as the single-board control computer.

Two servo motors were controlled through GPIO-based PWM signals.

The documented implementation used:

- GPIO pins `17` and `27`
- `50 Hz` PWM
- conversion from requested servo angle to PWM duty cycle
- simultaneous control of both servo motors
- GPIO cleanup when the program exited

The control pipeline was:

```text
Python
   │
   ▼
Raspberry Pi GPIO
   │
   ▼
PWM
   │
   ▼
Two Servo Motors
   │
   ▼
Tendon Displacement
   │
   ▼
Continuum-Wrist Bending
```

The prototype used **open-loop predefined servo positions**.

It did not measure:

- tendon tension
- continuum shape
- final hand pose

and therefore did not implement closed-loop shape control.

---

## Reconstructed Wrist-Control Source

The original wrist-control source file was not recovered from the archived project directory.

However, the original implementation was preserved in the bachelor-thesis documentation.

The repository therefore contains a clearly labelled reconstruction:

[`src/wrist_control/continuum_wrist_control.py`](src/wrist_control/continuum_wrist_control.py)

The file reconstructs the documented GPIO/PWM architecture and is **not presented as the untouched original 2024 source file**.

---

# Vision and Sign-Language Proof of Concept

The uHandPi platform already included camera-processing and hand-gesture-recognition demonstration software.

I did **not** develop the underlying gesture detector from scratch.

Instead, I adapted part of the existing rock-paper-scissors / gesture-recognition pipeline so detected gesture classes could trigger predefined sign-language configurations.

The demonstrated mappings included:

```text
Detected Rock
     ↓
Letter A configuration
```

and:

```text
Detected Scissors
     ↓
Letter K configuration
```

The project-specific mapping is reconstructed here:

[`src/vision/gesture_to_sign_mapping.py`](src/vision/gesture_to_sign_mapping.py)

The purpose of this work was to demonstrate the integration concept:

```text
Camera
   ↓
Existing Gesture Detector
   ↓
Project-Specific Mapping
   ↓
Predefined Robotic-Hand Configuration
```

This was a **proof of concept**, not a general-purpose sign-language-recognition model.

---

# Implemented vs Planned

| Component | Status |
|---|---|
| Physical robotic-hand prototype | ✅ Implemented |
| Custom compliant continuum wrist | ✅ Implemented |
| SolidWorks CAD design | ✅ Implemented |
| Technical drawing | ✅ Implemented |
| Continuum-wrist modelling | ✅ Studied / developed |
| MSC Adams simulation | ✅ Implemented |
| PLA / TPU manufacturing | ✅ Implemented |
| Physical wrist assembly | ✅ Implemented |
| Two-servo tendon actuation | ✅ Implemented |
| Raspberry Pi wrist controller | ✅ Implemented |
| Physical wrist movement | ✅ Demonstrated |
| Existing uHandPi finger software | ✅ Used as baseline |
| Adapted gesture detector | ✅ Proof of concept |
| Gesture-to-sign mapping | ✅ Proof of concept |
| General sign-language recognition | ❌ Not implemented |
| Automatic learner-sign evaluation | ❌ Not implemented |
| Real-time learner feedback | ❌ Not implemented |
| Closed-loop continuum control | ❌ Not implemented |
| Quantitative positioning validation | ❌ Not performed |
| Formal educational user study | ❌ Not performed |

---

# Engineering Results

The project successfully produced a working physical mechatronics prototype incorporating a custom compliant wrist into an existing robotic-hand platform.

The principal engineering outcomes were:

- redesign of the original lower manipulator
- custom cable-driven continuum wrist
- CAD-to-hardware development workflow
- multibody dynamic simulation
- PLA / TPU manufacturing
- tendon-based wrist actuation
- Raspberry Pi servo control
- physical demonstration of the continuum mechanism
- integration with the existing uHandPi hand
- preliminary adaptation of existing vision software for sign-selection commands

The project demonstrated the **mechanical and mechatronic feasibility of the redesigned wrist**.

No numerical claims are made regarding:

- positioning accuracy
- repeatability
- sign-production accuracy
- sign-recognition accuracy
- educational effectiveness

because these were not formally evaluated.

---

# Engineering Limitations

## Open-Loop Control

The wrist used predefined servo positions rather than direct measurement of continuum configuration.

Effects such as tendon stretch, friction, backlash, hysteresis, deformation and servo positioning error were therefore not actively compensated.

## Mechanical Repeatability

Cable-driven compliant mechanisms can be affected by tendon tension, material deformation and assembly tolerances.

A systematic quantitative repeatability study was not performed.

## Software Integration

The custom wrist-control implementation and the existing uHandPi finger-control system were not consolidated into one unified software architecture.

## Vision System

The vision experiment reused and adapted an existing gesture detector rather than training a dedicated sign-language model.

## Educational Validation

No formal study with sign-language learners, educators or children was conducted.

The project therefore does not claim demonstrated improvements in learning performance.

## Safety

The prototype did not include formal functional-safety validation or product-level certification and should be regarded as a research and educational prototype.

---

# Future Work

Potential future development includes:

- closed-loop continuum-wrist control
- tendon-tension sensing
- shape or pose feedback
- improved tendon calibration
- quantitative repeatability evaluation
- unified finger and wrist control
- improved enclosure and electronics integration
- alternative compliant materials
- continuum-geometry optimisation
- dedicated sign-language-recognition models
- expansion of the predefined sign library
- automatic learner feedback
- evaluation with sign-language educators and learners
- emergency-stop and additional safety functionality

---

# Technology Stack

### Mechanical Design & Simulation

- SolidWorks
- MSC Adams
- continuum robotics
- compliant mechanisms
- tendon-driven actuation
- multibody dynamics

### Manufacturing

- Ultimaker Cura
- Creality Ender 3
- PLA
- TPU
- additive manufacturing

### Embedded Control

- Raspberry Pi 4
- Python
- RPi.GPIO
- PWM servo control

### Computer Vision / Integration

- OpenCV
- existing uHandPi gesture-recognition framework
- project-specific gesture-to-sign mapping

---

# Repository Structure

```text
sign-language-robotic-hand/
│
├── README.md
├── .gitignore
│
├── cad/
│   ├── solidworks/
│   │   ├── Robotic Arm.SLDASM
│   │   ├── RoboticHand.SLDDRW
│   │   └── associated SLDPRT files/
│   │
│   └── exports/
│       ├── RoboticHand.stp
│       └── RoboticHand.x_t
│
├── simulation/
│   └── adams/
│       ├── Jessica_Robot.bin
│       └── MODEL_hand.bin
│
├── media/
│   ├── prototype/
│   │   └── final_prototype.jpg
│   │
│   ├── cad/
│   │   ├── assembly_render.jpg
│   │   ├── design_comparison.jpg
│   │   └── technical_drawing.png
│   │
│   └── demos/
│       └── adams_wrist_simulation.avi
│
└── src/
    ├── README.md
    │
    ├── wrist_control/
    │   └── continuum_wrist_control.py
    │
    └── vision/
        └── gesture_to_sign_mapping.py
```

Large software installations, Python distributions and the full third-party uHandPi software tree are intentionally excluded.

---

# Attribution and Third-Party Work

## Hiwonder uHandPi

This project builds upon the commercially available **Hiwonder uHandPi** robotic-hand platform.

The existing platform provided:

- robotic hand and finger mechanism
- finger servos
- Raspberry Pi electronics
- camera hardware
- existing Python finger-control software
- existing OpenCV / gesture-recognition demonstrations

These components are **not claimed as my original work**.

---

## Vision Software

The original uHandPi/Lobot software provided the underlying gesture-detection and robot-action infrastructure.

My work involved adapting and repurposing parts of that existing pipeline for the sign-language proof of concept.

The repository therefore contains only a reconstruction of the **project-specific gesture-to-sign mapping**, rather than redistributing the complete upstream software as my own implementation.

---

## My Original Thesis Work

My original thesis contributions include:

- mechanical redesign of the lower manipulator
- design of the cable-driven compliant continuum wrist
- SolidWorks CAD integration
- engineering drawings
- continuum-wrist modelling
- multibody simulation in MSC Adams
- material selection
- additive manufacturing
- physical assembly
- tendon and servo integration
- custom Raspberry Pi wrist control
- physical testing
- adaptation and integration of existing gesture-recognition functionality

---

# What This Project Demonstrates

This project provides evidence of experience in:

- physical robot prototyping
- robotic hands and end-effectors
- continuum robotics
- compliant mechanisms
- tendon-driven actuation
- SolidWorks CAD
- engineering drawings
- MSC Adams
- multibody dynamics
- additive manufacturing
- material selection
- Raspberry Pi
- Python
- PWM servo control
- computer-vision integration
- hardware/software integration
- iterative mechanical design
- human-robot interaction concepts
- responsible attribution of third-party platforms and software

---

# Citation

This repository has been archived on Zenodo.

**DOI:**  
[10.5281/zenodo.23102292](https://doi.org/10.5281/zenodo.23102292)

If referencing this project, please use the citation metadata provided by Zenodo.

---

# Academic Context

**Bachelor Thesis — 2023/2024**

**Mechanical Engineering — Robotics & Mechatronics Track**  
National Polytechnic University of Armenia

**Author:** Jessica Dichakdjian  
**Supervisor:** Prof. Narek Zakaryan

---

# Project Status

✅ **Completed physical bachelor-thesis prototype**

The mechanical redesign, CAD work, modelling, simulation, manufacturing, physical assembly and wrist actuation were completed.

The broader sign-language-recognition and automated learner-feedback system remained incomplete and is presented as future work rather than as a completed capability.
