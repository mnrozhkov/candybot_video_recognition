#!/usr/bin/env python3

Angle = 0

def set_angle(angle: float) -> None:

    global Angle
    Angle = angle

    print('set angle:' Angle)


def get_angle() -> float:
    
    global Angle

    return Angle
