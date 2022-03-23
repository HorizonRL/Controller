
from inputs import get_gamepad
import math
import threading
import cv2

from XboxControllerFrame import XboxControllerFrame

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self.frame = XboxControllerFrame()

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()


    def read(self):
        return {
            "sticks": [
                [self.LeftJoystickY,self.LeftJoystickX],
                [self.RightJoystickY, self.RightJoystickX]
            ],

            "triggers": [ 
                self.LeftTrigger,
                self.RightTrigger
            ],

            "btns": [
                self.LeftBumper,
                self.RightBumper,
                self.A,
                self.X,
                self.Y,
                self.B,
                self.LeftThumb,
                self.RightThumb,
                self.Back,
                self.Start,
                self.LeftDPad,
                self.RightDPad,
                self.UpDPad,
                self.DownDPad
                ]
            }


    def read_bool(self):
        return \
            [ 
                XboxController.movment_to_bool([self.LeftJoystickY, self.LeftJoystickX]),
                XboxController.movment_to_bool([self.RightJoystickY, self.RightJoystickX]),
                XboxController.movment_to_bool([self.LeftTrigger]),
                XboxController.movment_to_bool([self.RightTrigger]),
                self.LeftBumper,
                self.RightBumper,
                self.A,
                self.X,
                self.Y,
                self.B,
                self.Back,
                self.Start,
                self.LeftThumb,
                self.RightThumb,
                self.LeftDPad,
                self.RightDPad,
                self.UpDPad,
                self.DownDPad
            ]
        
    
    @staticmethod
    def movment_to_bool(vals):
        for v in vals:
            if abs(v) > 0:
                return 1
        
        return 0

    @staticmethod
    def deadband(value, deadband=0.15):
        return 0 if abs(value) <= deadband else value
        
    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = XboxController.deadband(event.state / XboxController.MAX_JOY_VAL) # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = XboxController.deadband(event.state / XboxController.MAX_JOY_VAL) # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = XboxController.deadband(event.state / XboxController.MAX_JOY_VAL) # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = XboxController.deadband(event.state / XboxController.MAX_JOY_VAL) # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = XboxController.deadband(event.state / XboxController.MAX_TRIG_VAL) # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = XboxController.deadband(event.state / XboxController.MAX_TRIG_VAL) # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state
                elif event.code == 'BTN_WEST':
                    self.X = event.state
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Start = event.state
                elif event.code == 'BTN_START':
                    self.Back = event.state
                elif event.code == 'ABS_HAT0X':
                    self.LeftDPad = 1 if event.state == 1 else 0
                    self.RightDPad = 1 if event.state == -1 else 0
                elif event.code == 'ABS_HAT0Y':
                    self.UpDPad = 1 if event.state == 1 else 0
                    self.DownDPad = 1 if event.state == -1 else 0

    
    def get_current_state(self):
        return self.frame.get_current_frame(self.read())

x = XboxController()
while True:
    f = x.get_current_state()
    cv2.imshow("view", f)
    cv2.waitKey(50)