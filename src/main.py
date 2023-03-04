import os
from pyxboxcontroller import XboxController, XboxControllerState
import time
controller1 = XboxController(0)
while True:
    os.system("cls")
    print(controller1.state)