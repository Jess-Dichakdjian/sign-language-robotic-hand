"""
Sign-language mapping proof of concept.

The original hand-gesture detector and robot action infrastructure
came from the Hiwonder/uHandPi software platform.

For my bachelor-thesis prototype, I adapted the detected gesture
classes to trigger predefined robotic-hand configurations representing
sign-language letters.

This file reconstructs that project-specific mapping without including
the full third-party uHandPi software stack.
"""


GESTURE_TO_SIGN = {
    "Rock": "A",
    "Scissors": "K",
}


def detected_gesture_to_sign(gesture):
    """
    Convert a gesture class produced by the existing vision system
    into the corresponding sign-language demonstration command.
    """
    return GESTURE_TO_SIGN.get(gesture)


def handle_detected_gesture(gesture, execute_sign):
    """
    Trigger a predefined robotic-hand action when a supported
    gesture is detected.

    `execute_sign` should be a function supplied by the robot-control
    layer.
    """
    sign = detected_gesture_to_sign(gesture)

    if sign is None:
        return False

    execute_sign(sign)
    return True
