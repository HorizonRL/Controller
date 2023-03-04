from generic import controller_frame
from xbox.XboxOneController import XboxOneController
from ControllerTypes import ControllerTypes



class XboxOneControllerFrame(controller_frame.ControllerFrame):
    def __init__(self, controller: XboxOneController, settings: controller_frame.FrameSettings):
        super().__init__(ControllerTypes.XBOX_ONE.value, controller, settings)
        
        self.positions = {
            "left_stick": (180, 280),
            "right_stick": (480, 400),
            "left_trigger": (200, 112),
            "right_trigger": (550, 112),
            "left_bumper": (190, 150),
            "right_bumper": (570, 150),
            "one": (570, 330),
            "four": (520, 280),
            "thre": (570, 230),
            "two": (620, 280),
            "back": (320, 280),
            "start": (430, 280),
            "pov_left": (315, 400),
            "pov_right": (240, 400),
            "pov_down": (280, 440),
            "pov_up": (280, 370)
        }

        self.register_default(self.positions)
