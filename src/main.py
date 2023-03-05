from generic.controller_frame import FrameSettings
from xbox_one.XboxOneController import XboxControllerInput
from xbox_one.XboxOneControllerFrame import XboxOneControllerFrame
import cv2

def main():
    controllers = XboxControllerInput.get_connected()
    frame = XboxOneControllerFrame(controllers[0], res_scale=0.5)
    while True:
        try:
            f = frame.get()
        except ConnectionError:
            pass
        cv2.imshow("view", f)
        cv2.waitKey(50)


if __name__ == '__main__':
    main()