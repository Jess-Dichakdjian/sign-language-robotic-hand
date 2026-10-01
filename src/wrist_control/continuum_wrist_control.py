"""
Reconstructed from the Raspberry Pi wrist-control implementation
documented in my 2024 bachelor thesis.

The original source file was not recovered. This version reproduces
the documented GPIO/PWM control structure for the two servo motors
used to actuate the cable-driven continuum wrist.
"""

import RPi.GPIO as GPIO
from time import sleep

# GPIO pins connected to the two wrist-actuation servos
SERVO_PINS = (17, 27)
PWM_FREQUENCY = 50

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PINS, GPIO.OUT)

servo_pwms = [
    GPIO.PWM(pin, PWM_FREQUENCY)
    for pin in SERVO_PINS
]

for pwm in servo_pwms:
    pwm.start(0)


def set_servo_angle(pwm, angle):
    """
    Convert a servo angle in degrees to an approximate PWM duty cycle.
    """
    angle = max(0, min(180, angle))
    duty_cycle = angle / 18.0 + 2.5

    pwm.ChangeDutyCycle(duty_cycle)
    sleep(0.3)
    pwm.ChangeDutyCycle(0)


try:
    while True:
        # Example wrist configuration used during prototype testing.
        servo1_angle = 90
        servo2_angle = 120

        for pwm, angle in zip(
            servo_pwms,
            (servo1_angle, servo2_angle)
        ):
            set_servo_angle(pwm, angle)

        sleep(1)

except KeyboardInterrupt:
    pass

finally:
    for pwm in servo_pwms:
        pwm.stop()

    GPIO.cleanup()
