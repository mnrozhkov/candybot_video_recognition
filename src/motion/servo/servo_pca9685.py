#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

# Import the PCA9685 module.
import Adafruit_PCA9685

# Uncomment to enable debug output.
import logging

logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default channel (0x40)
pwm = Adafruit_PCA9685.PCA9685()


# Alternatively specify a different channel and/or bus:
# pwm = Adafruit_PCA9685.PCA9685(channel=0x41, busnum=2)



# # Helper function to make setting a servo pulse width simpler.
# TODO: Delete after Servo() fix as deprecated
# def set_servo_pulse(channel, pulse):
#     pulse_length = 1000000    # 1,000,000 us per second
#     pulse_length //= 60       # 60 Hz
#     print('{0}us per period'.format(pulse_length))
#     pulse_length //= 4096     # 12 bits of resolution
#     print('{0}us per bit'.format(pulse_length))
#     pulse *= 1000
#     pulse //= pulse_length
#     pwm.set_pwm(channel, 0, pulse)
#
#
# def set_angle(channel, degrees):
#     """
#     Turn servo on specified angle in degrees
#     Params:
#     :param degrees: angle to turn servo, in degrees
#     """
#
#     # Set frequency to 60hz, good for servos.
#     pwm.set_pwm_freq(60)
#     servo_min = 150  # Min pulse length out of 4096
#     servo_max = 600  # Max pulse length out of 4096
#
#     duty = int(servo_min + math.floor(degrees * (servo_max - servo_min) / 180))
#     if duty:
#         try:
#             # print('Moving servo on channel 0')
#             pwm.set_pwm(channel, 0, duty)
#             # time.sleep(0.5)
#         except:
#             # clean up
#             pwm.set_pwm(channel, 0, 0)
#             warnings.warn("Servo was not moved. Move in None. Set servo pin to 0")


class Servo(object):
    """
    Allows controlling up to 16 servos.
    The freq argument sets the PWM signal frequency in Hz. Analog servos usually expect this to be 50, but digital servos can
    often handle higher frequencies, resulting in smoother movements.
    The min_us and max_us arguments set the range of the singnal’s duty that the servo accepts.
    This is different between different servo models, but usually they are centerd at 1500µs.
    The degrees argument specifies the physical range of the servo corresponding to the signal’s duty range specified before.
    It is used to calculate signal’s duty when the angle is specified in degrees or radians.

    Agrs:
        :param channel:
        :param freq:
        :param min_us:
        :min_us:
        :max_us:
        :degrees:

    :return:
    """

    def __init__(self, channel, freq=60, min_us=600, max_us=2400,
                 degrees=180):
        self.period = 1000000 / freq  # pulse length
        self.min_duty = self._us2duty(min_us)  # min_pulse =  self.min_duty * 1000 / 4096
        self.max_duty = self._us2duty(max_us)  # max_pulse = self.min_duty * 1000 / 4096
        self.degrees = degrees
        self.freq = freq
        self.pca9685 = Adafruit_PCA9685.PCA9685()
        self.pca9685.set_pwm_freq(freq)
        self.channel = channel

    def _us2duty(self, value):
        """

        Args:
            value:

        Returns:

        """
        return int(4095 * value / self.period)

    def set_angle(self, degrees=None, radians=None):
        """
        Get or set the servo position. The position can be specified in degrees (the default),
        radians, microseconds or directly as a number between 0 and 4095 signifying the duty cycle.
        It will be automatically clamped to the minimum and maximum range allowed.

        Args:
            degrees:
            radians:

        Returns:

        """
        print('servo: angle:', degrees)
        span = self.max_duty - self.min_duty
        if degrees is not None:
            duty = self.min_duty + span * degrees / self.degrees
        elif radians is not None:
            duty = self.min_duty + span * radians / math.radians(self.degrees)
        else:
            return self.pca9685.set_pwm(0, 0, self.min_duty)

        duty = min(self.max_duty, max(self.min_duty, int(duty)))
        self.pca9685.set_pwm(self.channel, 0, duty)

    # def release(self, channel):
    #     self.pca9685.set_pwm(channel, 0, self.min_duty)



    class Servo360:

        def __init__(self, SERVO_CHANNEL):
            self.RUN_ANGLE = 50
            selg.STOP_ANGLE = 70

            self.servo = Servo(channel=SERVO_CHANNEL)

        def run(self):
            self.servo.set_angle(self.RUN_ANGLE)

        def stop(self):
            self.servo.set_angle(self.STOP_ANGLE)
