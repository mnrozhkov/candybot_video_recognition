
def set_head_position (horizontal_angle, vertical_angle):
    print('head: h_angle={0},v_angle={1}'.format(horizontal_angle, vertical_angle))


def set_led_mode(led_on=False, color=(255,255,255), mode='light', frequency=None):
    print('body: led_on={0},color={1}, mode={2}, frequency={3}'.format(led_on, color, mode, frequency))


def set_eyebrows_position(angle):
    print('eyebrows: position=v_angle=', angle)


def set_pupil_position(self, angle, distane_from_center_percent):
    print('eyes pupil position: angle={0}, distane from center(percent)={1}'.format(angle, distane_from_center_percent))

def get_pupil_position(self) -> dict:
    pass
