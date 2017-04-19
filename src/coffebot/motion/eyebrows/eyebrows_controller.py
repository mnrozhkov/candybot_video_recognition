class Eyebrows:

    def __init__(self):
        self.backlight_color = None
        self.vertical_angle = 0

    def move_up(self, angle: float=math.pi / 4):
        print('eyebrows move up:', angle)
        self.vertical_angle = angle

    def move_down(self, angle: float=math.pi / 4):
        print('eyebrows move down:', angle)
        self.vertical_angle = -angle

    def turn_backlight_on(self):
        print('eyebrows backlight on')

    def turn_backlight_off(self):
        print('eyebrows backlight off')

    def turn_backlight_dim(self):
        print('eyebrows backlight dim')

    def set_backlight_color(self, color):
        print('backlight:', color)
        self.backlight_color = color

    def blink_backlight(self, times: int=1):
        print('eyebrows backlight blink:', times)
