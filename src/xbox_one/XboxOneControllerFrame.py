from common.Point import Point
from generic import controller_frame
from xbox_one.XboxOneController import XboxControllerInput
from ControllerTypes import ControllerTypes


class XboxOneControllerFrame(controller_frame.ControllerFrame):
    def __init__(self, controller: XboxControllerInput, res_scale=1):
        settings = controller_frame.FrameSettings(
            color=(255, 128, 0),
            bool_widget_size=25,
            joystick_threshold=0.1,
            joystick_widget_range=45,
            joystick_widget_size=15,
            linear_widget_range=100,
            linear_widget_threshold=0.1,
            linear_widget_length=40,
            linear_widget_width=4,
            display_range_always=True)

        super().__init__(ControllerTypes.XBOX_ONE.value, controller, settings, res_scale)

        self.positions = {
            "left_stick": Point(180, 280),
            "right_stick": Point(480, 400),
            "left_trigger": Point(200, 112),
            "right_trigger": Point(550, 112),
            "left_bumper": Point(190, 150),
            "right_bumper": Point(570, 150),
            "one": Point(570, 330),
            "four": Point(520, 280),
            "three": Point(570, 230),
            "two": Point(620, 280),
            "back": Point(320, 280),
            "start": Point(430, 280),
            "pov_right": Point(315, 400),
            "pov_left": Point(240, 400),
            "pov_down": Point(280, 440),
            "pov_up": Point(280, 370)
        }
        self.register_default(self.positions)
