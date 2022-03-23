from itertools import count
import cv2
from enum import Enum

class PosMap(Enum):
    L = (180, 280)
    R = (480, 400)
    LT = (200, 112)
    RT = (550, 112)
    LB = (190, 150)
    RB = (570, 150)
    A = (570, 330)
    X = (520, 280)
    Y = (570, 230)
    B = (620, 280)
    LS = (181, 280)
    RS = (481, 400)
    BACK = (320, 280)
    START = (430, 280)
    POV_LEFT = (315, 400)
    POV_RIGHT = (240, 400)
    POV_DOWN = (280, 440)
    POV_UP = (280, 370)

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))

    @classmethod
    def list_name(cls):
        return list(map(lambda c: c.name, cls))
    
    @staticmethod
    def cpos_to_rpos(cpos, size):
        return int(cpos[0] + (size[0] / 2)), int(cpos[1] + (size[1] / 2))

    @staticmethod
    def cpos_to_lpos(cpos, size):
        return int(cpos[0] - (size[0] / 2)), int(cpos[1] - (size[1] / 2))


class ActionColor(Enum):
    PRESS = (0, 204, 0)
    MOVE = (255, 128, 0)


class XboxControllerFrame:

    def __init__(self):
        self.org_path = 'Xcontroller.png'
        self.marker_size_btn = 15
        self.marker_size_move = 10
        self.trigger_width = 30
        self.stick_range = 50
        self.trigger_range = 100
    
    def get_current_frame(self, vals):
        frame = cv2.imread(self.org_path)
        count = 0

        for stick in vals['sticks']:
            x, y = PosMap.list()[count]
            dx, dy = (int(stick[1] * self.stick_range), int(stick[0] * -self.stick_range))
            cv2.circle(frame, (x + dx, y + dy), self.marker_size_move, ActionColor.MOVE.value, -1)
            count += 1

        for trigger in vals['triggers']:
            x, y = PosMap.list()[count]
            dx, dy = 0, int(trigger * -self.trigger_range)
            cv2.line(frame, ((x + dx) - self.trigger_width, (y + dy)), ((x + dx) + self.trigger_width , (y + dy)), ActionColor.MOVE.value, int(2 + (trigger * 10)))
            count += 1

        for btn in vals['btns']:
            if btn == 1:
                x, y = PosMap.list()[count]
                cv2.circle(frame, (x, y), self.marker_size_btn, ActionColor.PRESS.value, -1)
            count += 1

        return frame