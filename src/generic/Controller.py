from abc import abstractmethod, abstractstaticmethod
from ControllerTypes import ControllerTypes


class Controller:
    @abstractstaticmethod
    def get_connected() -> list:
        raise NotImplementedError()

    def __init__(self, name: str, controller_type: ControllerTypes, controller_id: str):
        self._name = name
        self._controller_type = controller_type
        self._controller_id = controller_id
    
    @abstractmethod
    def get_btn_one(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_btn_two(self) -> bool:
        raise NotImplementedError()
    
    @abstractmethod
    def get_btn_three(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_btn_four(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_start_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_back_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_pov_up_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_pov_down_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_pov_left_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_pov_right_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_left_stick_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_right_stick_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_left_bumper_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_right_bumper_btn(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_right_trigger_value(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_left_trigger_value(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_left_stick_x_value(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_left_stick_y_value(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_right_stick_x_value(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def get_right_stick_y_value(self) -> float:
        raise NotImplementedError()
