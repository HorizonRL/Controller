from enum import Enum, auto
from common import Point
from typing import Callable
from dataclasses import dataclass
from Controller import Controller
import cv2


class ControllerWidgetTypes(Enum):
    BOOL = auto()
    JOYSTICK = auto()
    LINIEAR = auto()


@dataclass
class GUI_ControllerWidget:
    widget_type : ControllerWidgetTypes
    point: Point
    func: Callable


@dataclass
class FrameSettings:
    color: tuple

    bool_widget_size: int

    joystick_threshold: float
    joystick_widget_range: int
    joystick_widget_size: int

    linear_widget_size: int
    linear_widget_threshold: int
    linear_widget_range: int

    display_range_always: bool


class ControllerFrame:
    def __init__(self, image_path: str, controller: Controller, settings: FrameSettings):
        self._image_path = image_path
        self._controller = controller
        self._widgets = []
        self._settings = settings
        
        self._widgets_handlers = {
            ControllerWidgetTypes.BOOL: self._handle_bool_widget,
            ControllerWidgetTypes.JOYSTICK: self._handle_joystick_widget,
            ControllerWidgetTypes.LINIEAR: self._handle_linear_widget,
        }

    def register(self, widget: GUI_ControllerWidget):
        self._widgets.append(widget)

    def _handle_bool_widget(self, frame, widget: GUI_ControllerWidget):
        if bool(widget.value):
            cv2.circle(frame, (widget.point.x, widget.point.y), self._settings.bool_widget_size, self._settings.color, -1)

    def _handle_joystick_widget(self, frame, widget: GUI_ControllerWidget):
        if self._settings.display_range_always or abs(widget.value.x) > self._settings.joystick_threshold or abs(widget.value.y) > self._settings.joystick_threshold:
            dx = int(widget.value.x * self._settings.joystick_widget_range)
            dy = int(widget.value.y * self._settings.joystick_widget_range)
            cv2.circle(frame, (widget.point.x + dx, widget.point.y + dy), self._settings.joystick_widget_size, self._settings.color, -1)

    def _handle_linear_widget(self, frame, widget: GUI_ControllerWidget):
        if self._settings.display_range_always or abs(widget.value) > self._settings.linear_widget_threshold:
            dy = widget.value * self._settings.linear_widget_range

            start_point = Point(
                widget.point.x - self._settings.linear_widget_size,
                widget.point.y + dy
            )

            end_point = Point(
                widget.point.x + self._settings.linear_widget_size, 
                start_point.y
            )
            
            cv2.line(frame, start_point.to_tuple(), end_point.to_tuple(), self._settings.color, -1)


    def _frame_add_widget(self, frame, widget: GUI_ControllerWidget):
        self._widgets_handlers[widget.widget_type](frame, widget)

    def get(self):
        frame = cv2.imread(self._image_path)
        [self._frame_add_widget(frame, widget) for widget in self.widgets]
        return frame
    
    def register_default(self, positions: dict):
        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["one"],
            self._controller.get_btn_one,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["two"],
            self._controller.get_btn_two,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["two"],
            self._controller.get_btn_two,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["three"],
            self._controller.get_btn_three,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["four"],
            self._controller.get_btn_four,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["start"],
            self._controller.get_start_btn,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["back"],
            self._controller.get_back_btn,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["pov_up"],
            self._controller.get_pov_up,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["pov_down"],
            self._controller.get_pov_down,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["pov_left"],
            self._controller.get_pov_left,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["pov_right"],
            self._controller.get_pov_right,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["right_stick"],
            self._controller.get_right_stick_btn,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["left_stick"],
            self._controller.get_left_stick_btn,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["right_bumper"],
            self._controller.get_right_bumper_btn,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["left_bumper"],
            self._controller.get_left_bumper_btn,
            False
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.LINIEAR, 
            positions["right_trigger"],
            self._controller.get_right_trigger_value,
            0
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.LINIEAR, 
            positions["left_trigger"],
            self._controller.get_left_trigger_value,
            0
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.JOYSTICK, 
            positions["left_stick"],
            lambda: Point(self._controller.get_left_stick_x_value, self._controller.get_left_stick_y_value),
            Point(0, 0)
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.JOYSTICK, 
            positions["right_stick"],
            lambda: Point(self._controller.get_right_stick_x_value, self._controller.get_right_stick_y_value),
            Point(0, 0)
        ))
