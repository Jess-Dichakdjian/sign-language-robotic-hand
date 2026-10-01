# Source Code

This directory contains the project-specific source code that can be
clearly separated from the third-party uHandPi software platform.

## `wrist_control/`

Contains a reconstruction of the Raspberry Pi GPIO/PWM controller used
to actuate the two servo motors driving the custom cable-driven
continuum wrist.

The original source file was not recovered; the implementation is
reconstructed from the code and documentation preserved in the bachelor
thesis.

## `vision/`

Contains the project-specific mapping used to adapt the existing
uHandPi gesture-recognition demonstration for sign-language interaction.

The underlying camera, OpenCV and gesture-recognition framework
originated from the uHandPi/Lobot software and is not included here as
original work.
