# Sign-Language Educational Robotic Hand

**Bachelor Thesis — Mechanical Engineering, Robotics & Mechatronics**

A physical robotic-hand prototype developed for sign-language education, combining a commercially available robotic hand with a **custom cable-driven continuum wrist**, mechanical redesign, multibody simulation, 3D printing and Raspberry Pi-based actuation.

> **Project status:** Completed bachelor thesis prototype.  
> The physical hand and continuum wrist were built and tested; AI-based learner sign recognition and automatic feedback remained future work.

---

## Project Overview

The goal of this project was to investigate how a low-cost physical robotic hand could be adapted as an interactive tool for sign-language education.

Rather than designing an entire dexterous hand from scratch, I used the **Hiwonder uHandPi** robotic hand as the starting platform and focused my engineering work on a major mechanical limitation of the original design: its wrist and lower manipulator.

I redesigned this section as a **cable-driven compliant / continuum wrist**, giving the hand a larger and more natural bending range while maintaining a relatively simple and low-cost mechanical structure.

The project covered the full physical prototyping workflow:

**concept → CAD → kinematic modelling → multibody simulation → material selection → 3D printing → assembly → servo control → physical testing**

---

## What I Built

The final prototype combines:

- the existing uHandPi robotic hand and finger mechanism
- a custom four-section continuum wrist
- flexible backbone elements
- tendon / cable actuation
- two servo motors for the new wrist mechanism
- Raspberry Pi-based control
- custom 3D-printed PLA and TPU components
- a physical enclosure for electronics and actuation components

The prototype was physically manufactured and assembled rather than remaining only a CAD or simulation project.

---

## My Contributions

This was my **individual bachelor thesis project**.

My engineering work included:

### Mechanical Design

- redesigning the lower section of the uHandPi platform
- removing the original lower manipulator / wrist mechanism
- designing a new cable-driven continuum wrist
- designing four rounded wrist sections
- designing the flexible backbone arrangement
- designing cable routing for actuation
- designing the base / electronics enclosure
- creating and refining the assembly in SolidWorks
- checking mechanical clearances before manufacturing

### Modelling & Analysis

- modelling the finger kinematics using Denavit-Hartenberg concepts
- studying forward and inverse kinematics
- modelling the continuum wrist using cable-driven continuum-manipulator concepts
- studying differential kinematics
- deriving the relationship between cable actuation and continuum configuration
- studying Jacobian-based relationships between configuration and end-effector motion
- investigating the dynamic behaviour of the mechanism
- creating an MSC Adams multibody simulation
- analysing simulated motion and mechanical response

### Prototyping

- preparing components for additive manufacturing
- slicing components using Ultimaker Cura
- printing rigid wrist components in PLA
- printing the flexible backbone component in TPU
- physically assembling the redesigned hand
- installing tendon / fishing-line actuation
- integrating the servos and Raspberry Pi

### Control

- writing Python code for Raspberry Pi GPIO / PWM control of the new wrist servos
- commanding pre-defined wrist configurations
- integrating the new mechanical system with the existing uHandPi hand

---

# Starting Platform — Hiwonder uHandPi

The project did **not** create the complete robotic hand from scratch.

The original platform was a commercially available **Hiwonder uHandPi Raspberry Pi robotic hand**.

The existing platform already provided:

- the five-finger hand mechanism
- finger servos / actuation
- Raspberry Pi-based electronics
- open-source Python control software
- camera hardware
- OpenCV-based vision functionality provided by the platform

The existing uHandPi finger-control code is **third-party software and is not claimed as my own work**.

My project focused on mechanically redesigning and extending the platform, particularly the wrist and lower manipulator.

---

# Mechanical Redesign

## Original Limitation

The original uHandPi lower manipulator restricted the range and style of wrist motion needed for expressive sign-language gestures.

The redesign therefore removed the original lower wrist/manipulator assembly while retaining the hand and associated electronics.

---

## Cable-Driven Continuum Wrist

I replaced the original wrist mechanism with a compliant structure consisting of **four rounded sections connected through a flexible backbone**.

```text
Robotic Hand
     │
     ▼
 Rounded Section
     │
 Rounded Section
     │
 Rounded Section
     │
 Rounded Section
     │
 Flexible Backbone
     │
     ▼
 Actuation / Base
```

Unlike a conventional wrist composed entirely of discrete revolute joints, the new mechanism bends continuously through deformation of the compliant structure.

This was selected to provide:

- greater bending flexibility
- smoother wrist-like motion
- reduced mechanical complexity
- relatively low manufacturing cost
- compatibility with additive manufacturing

---

## Tendon / Cable Actuation

The wrist is actuated through cables routed through the continuum structure.

The physical prototype contains **eight cable runs**, arranged so that paired cables act together as effective control directions.

Fishing line was used as an inexpensive tendon material during prototyping.

The tendon forces bend the compliant wrist structure and change the orientation of the robotic hand.

---

# CAD Design

The modified system was modelled in **SolidWorks** before physical manufacturing.

The CAD work included:

- original hand representation
- four custom continuum-wrist sections
- flexible backbone geometry
- cable-routing features
- electronics / actuation enclosure
- full assembly integration

Virtual assembly was used to check:

- mechanical interference
- clearances
- component positioning
- manufacturability
- assembly feasibility

This allowed mechanical issues to be identified before committing to long 3D-printing cycles.

> CAD images will be added to `media/cad/`.

---

# Kinematic Modelling

## Finger Kinematics

The retained hand provides independent finger flexion, with one principal bending degree of freedom associated with each finger.

The finger system was analysed using **Denavit-Hartenberg modelling concepts**.

The five finger variables can be represented as:

```text
θ1  Thumb
θ2  Index
θ3  Middle
θ4  Ring
θ5  Pinky
```

Forward kinematics describes the relationship:

```text
joint configuration → finger/end-effector pose
```

while inverse kinematics considers the reverse problem:

```text
desired pose → required joint configuration
```

---

## Continuum-Wrist Kinematics

The continuum mechanism requires a different modelling approach from a conventional rigid-link manipulator.

The analysis considered the relationship between:

```text
Cable / Tendon Space
        │
        ▼
Configuration Space
(curvature / orientation)
        │
        ▼
Operational Space
(end-effector pose)
```

The model investigated how tendon-length changes produce bending of the compliant mechanism and therefore alter the pose of the attached robotic hand.

---

## Differential Kinematics

Differential kinematics was studied to relate actuation changes to motion of the hand.

Conceptually:

```text
Cable Velocities
       │
       ▼
Configuration-Space Velocity
       │
       ▼
Jacobian
       │
       ▼
End-Effector Velocity
```

This provides a basis for more advanced continuous control of the wrist in future versions of the system.

---

# Dynamic Modelling

The project also considered the dynamic behaviour of the mechanism.

The modelling examined factors including:

- link / component mass
- inertia
- centres of mass
- gravitational effects
- elastic behaviour
- damping
- friction
- motor torque
- compliant-joint behaviour

The purpose was to understand how the physical mechanism responds during movement rather than considering geometry alone.

---

# MSC Adams Simulation

The redesigned system was imported into **MSC Adams** for multibody simulation.

The simulation was used to investigate the behaviour of the continuum mechanism during motion.

Outputs included quantities such as:

- hand position
- angular response
- angular velocity
- kinetic energy
- deformation / displacement behaviour

These simulations provided an additional check between the mechanical design and expected physical behaviour before and during prototyping.

> Simulation screenshots and plots will be added to `media/simulation/`.

---

# Manufacturing

## 3D Printing

The redesigned components were prepared using **Ultimaker Cura** and manufactured using a **Creality Ender 3**.

Two primary materials were used.

### PLA

PLA was used for the four rigid wrist sections.

The complete set required more than ten hours of printing.

### TPU

TPU was used for the flexible backbone element because its flexibility better suited the compliant wrist design.

The backbone required approximately two hours of printing.

---

## Physical Assembly

The final prototype was assembled using:

- four printed wrist sections
- flexible TPU backbone
- eleven mechanical fasteners
- fishing-line tendons
- servo actuation
- Raspberry Pi electronics
- retained uHandPi robotic hand

The resulting assembly produced the physical prototype shown below.

<!-- Add once uploaded:
![Final robotic-hand prototype](media/prototype/final_prototype.jpg)
-->

---

# Control System

The system contained two distinct control layers.

## Existing uHandPi Hand

The finger mechanism retained the uHandPi's existing open-source Python control infrastructure.

This was accessed using the Raspberry Pi environment and VNC-based tools supplied with the original platform.

This existing software was **not developed by me**.

---

## Custom Continuum-Wrist Control

My custom control work focused on the newly designed wrist.

A **Raspberry Pi 4 Model B** was used to command two servo motors through GPIO PWM.

The control concept was:

```text
Python Command
      │
      ▼
Raspberry Pi GPIO
      │
      ▼
PWM Signals
      │
      ▼
Servo Motors
      │
      ▼
Tendon Movement
      │
      ▼
Continuum Wrist Bending
```

The thesis prototype used pre-programmed servo commands rather than a complete closed-loop continuum controller.

---

# Sign-Language Operation

The implemented prototype could reproduce **basic pre-programmed hand configurations and motions**.

The intended educational interaction was:

```text
Select Sign
    │
    ▼
Robot Demonstrates Sign
    │
    ▼
Learner Repeats Sign
```

A more advanced version was envisioned in which a camera would recognise the learner's gesture and provide feedback.

That feedback system was **not completed in the bachelor-thesis prototype**.

---

# Implemented vs Future Functionality

| Component | Status |
|---|---|
| Physical robotic-hand prototype | ✅ Implemented |
| Custom continuum wrist | ✅ Implemented |
| SolidWorks mechanical design | ✅ Implemented |
| Multibody simulation | ✅ Implemented |
| PLA / TPU manufacturing | ✅ Implemented |
| Physical assembly | ✅ Implemented |
| Raspberry Pi wrist-servo control | ✅ Implemented |
| Basic pre-programmed motion/sign reproduction | ✅ Implemented |
| Existing uHandPi finger control | ✅ Used — third-party baseline |
| Camera hardware | ✅ Existing uHandPi hardware |
| Automatic learner sign recognition | ❌ Not completed |
| Automatic sign-accuracy feedback | ❌ Not completed |
| Closed-loop continuum control | ❌ Not implemented |
| Formal educational user study | ❌ Not performed |
| Quantitative sign-recognition accuracy | ❌ Not available |

---

# Demonstration

## Physical Prototype

<!-- Add:
![Physical robotic-hand prototype](media/prototype/final_prototype.jpg)
-->

## Motion Demonstration

<!-- Add:
![Robotic-hand demonstration](media/demos/robotic_hand.gif)
-->

A longer physical demonstration is available in:

```text
media/demos/robotic_hand.mp4
```

---

# Results

The project successfully produced a **working physical prototype** of the redesigned robotic hand and continuum wrist.

The main engineering outcomes were:

- successful mechanical integration with the existing uHandPi hand
- physical manufacture of the redesigned wrist
- compliant bending using a cable-driven mechanism
- Raspberry Pi / servo actuation of the new wrist
- basic reproduction of pre-programmed motions
- multibody simulation of the redesigned structure
- complete CAD-to-hardware prototyping workflow

The project was primarily a **mechanical and mechatronics prototype**, rather than a validated sign-recognition or educational-AI system.

No controlled quantitative user-study results or sign-recognition accuracy measurements are claimed.

---

# Limitations

The prototype has several important limitations.

### Control

The continuum wrist was controlled using pre-programmed servo positions rather than full closed-loop shape or end-effector control.

### Hand Integration

The existing uHandPi finger-control system remained separate from much of the custom wrist-control implementation.

### Perception

The planned camera-based recognition of a learner's sign was not completed.

### Educational Feedback

The prototype could demonstrate gestures but could not automatically evaluate the learner's sign accuracy.

### Mechanical Precision

Cable-driven compliant mechanisms introduce challenges including:

- tendon tension
- friction
- backlash
- deformation
- calibration
- repeatability

These effects were not fully compensated through feedback control in the prototype.

---

# Future Work

Potential next steps include:

- integrate finger and wrist control into one software architecture
- develop closed-loop continuum-wrist control
- add joint / tendon / shape sensing
- improve tendon tensioning and calibration
- implement camera-based sign recognition
- provide automatic learner feedback
- create a structured sign library
- quantitatively evaluate repeatability and positioning
- conduct appropriately designed educational user studies
- redesign the electronics enclosure
- investigate lighter and more durable compliant materials

---

# Technology Stack

### Mechanical / Simulation

- SolidWorks
- MSC Adams
- Ultimaker Cura
- additive manufacturing
- PLA
- TPU
- cable / tendon-driven mechanisms

### Robotics / Control

- Raspberry Pi 4
- Python
- GPIO
- PWM servo control
- robotic-hand kinematics
- continuum robotics
- multibody dynamics

### Existing Platform Technologies

- Hiwonder uHandPi
- OpenCV
- VNC-based control tools

---

# Repository Structure

The repository is being reconstructed from the original bachelor-thesis project files.

```text
sign-language-robotic-hand/
│
├── README.md
│
├── src/
│   └── wrist_control/
│
├── cad/
│
├── simulation/
│
├── docs/
│
└── media/
    ├── prototype/
    ├── cad/
    ├── simulation/
    └── demos/
```

Only files whose ownership and purpose can be clearly identified will be included.

---

# Attribution

## Hiwonder uHandPi

This project uses the **Hiwonder uHandPi** robotic hand as its starting platform.

The original:

- hand mechanism
- finger actuation
- Raspberry Pi software
- camera system
- OpenCV functionality
- associated open-source control code

were developed by Hiwonder / the upstream uHandPi project and are **not my original work**.

My bachelor-thesis contribution focused on redesigning and extending the platform with the custom continuum wrist, modelling, simulation, manufacturing and associated wrist-control implementation.

Third-party source code will not be presented as my own work.

---

# What This Project Demonstrates

For robotics and mechatronics roles, this project demonstrates experience with:

- physical robotic prototyping
- CAD and mechanical design
- compliant / continuum mechanisms
- tendon-driven actuation
- robotic-hand systems
- kinematic modelling
- dynamics
- multibody simulation
- additive manufacturing
- material selection
- Raspberry Pi integration
- servo control
- Python
- hardware/software integration
- iterative mechanical design
- human-robot interaction concepts

---

## Academic Context

**Bachelor Thesis — 2023/2024**

Mechanical Engineering — Robotics & Mechatronics track  
National Polytechnic University of Armenia

**Author:** Jessica Dichakdjian

---

## Project Status

✅ **Completed physical bachelor-thesis prototype**

The repository is currently being reconstructed and documented for my robotics engineering portfolio.
