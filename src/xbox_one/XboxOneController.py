from generic.Controller import Controller
from pyxboxcontroller import XboxController, XboxControllerState
from ControllerTypes import ControllerTypes


class XboxControllerInput(Controller):

    @staticmethod
    def get_connected() -> list:
        def get_raw_controllers() -> list:
            connected = []

            is_done = False
            index = 0
            while not is_done:
                try:
                    controller = XboxController(index)
                    controller.state
                except ConnectionError:
                    is_done = True
                    continue

                connected.append(controller)
                index += 1

            return connected
        
        raw_controllers = get_raw_controllers()
        controllers = []

        for raw_controller in raw_controllers:
            controller_id = raw_controller.id
            controllers.append(XboxControllerInput(
                f'xbx_{controller_id}',
                controller_id
            ))
        
        return controllers

    def __init__(self, name: str, controller_id: str):
        super().__init__(name, ControllerTypes.XBOX_ONE, controller_id)
        self.raw_input = XboxController(controller_id)

    def get_btn_one(self) -> bool:
        return self.raw_input.state.a

    def get_btn_two(self) -> bool:
        return self.raw_input.state.b
    
    def get_btn_three(self) -> bool:
        return self.raw_input.state.y

    def get_btn_four(self) -> bool:
        return self.raw_input.state.x

    def get_start_btn(self) -> bool:
        return self.raw_input.state.start

    def get_back_btn(self) -> bool:
        return self.raw_input.state.select

    def get_pov_up_btn(self) -> bool:
        return self.raw_input.state.dpad_up

    def get_pov_down_btn(self) -> bool:
        return self.raw_input.state.dpad_down

    def get_pov_left_btn(self) -> bool:
        return self.raw_input.state.dpad_left

    def get_pov_right_btn(self) -> bool:
        return self.raw_input.state.dpad_right
    
    def get_left_stick_btn(self) -> bool:
        return self.raw_input.state.l3

    def get_right_stick_btn(self) -> bool:
        return self.raw_input.state.r3

    def get_left_bumper_btn(self) -> bool:
        return self.raw_input.state.lb

    def get_right_bumper_btn(self) -> bool:
        return self.raw_input.state.rb

    def get_right_trigger_value(self) -> float:
        return self.raw_input.state.r_trigger
    
    def get_left_trigger_value(self) -> float:
        return self.raw_input.state.l_trigger

    def get_left_stick_x_value(self) -> float:
        return self.raw_input.state.l_thumb_x

    def get_left_stick_y_value(self) -> float:
        return self.raw_input.state.l_thumb_y

    def get_right_stick_x_value(self) -> float:
        return self.raw_input.state.r_thumb_x

    def get_right_stick_y_value(self) -> float:
        return self.raw_input.state.r_thumb_y
