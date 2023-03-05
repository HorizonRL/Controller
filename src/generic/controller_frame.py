from enum import Enum, auto
from common.Point import Point
from typing import Any, Callable
from dataclasses import dataclass
from generic.Controller import Controller
import cv2


class ControllerWidgetTypes(Enum):
    BOOL = auto()
    JOYSTICK = auto()
    LINIEAR_Y = auto()


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

    linear_widget_length: int
    linear_widget_threshold: int
    linear_widget_range: int
    linear_widget_width: int

    display_range_always: bool


class ControllerFrame:
    def __init__(self, image_path: str, controller: Controller, settings: FrameSettings, res_scale=1):
        self._image_path = image_path
        self._controller = controller
        self._widgets = []
        self._settings = settings
        self._res_scale = res_scale
        
        self._widgets_handlers = {
            ControllerWidgetTypes.BOOL: self._handle_bool_widget,
            ControllerWidgetTypes.JOYSTICK: self._handle_joystick_widget,
            ControllerWidgetTypes.LINIEAR_Y: self._handle_linear_widget,
        }

    def register(self, widget: GUI_ControllerWidget):
        self._widgets.append(widget)

    def _handle_bool_widget(self, frame, widget: GUI_ControllerWidget, value):
        if bool(value):
            cv2.circle(frame, widget.point.to_int_tuple(), int(self._res_scale * self._settings.bool_widget_size), self._settings.color, -1)
        return frame 

    def _handle_joystick_widget(self, frame, widget: GUI_ControllerWidget, value):
        if self._settings.display_range_always or abs(value.x) > self._settings.joystick_threshold or abs(value.y) > self._settings.joystick_threshold:
            delta_point = Point(
                int(value.x * self._settings.joystick_widget_range),
                int(-value.y * self._settings.joystick_widget_range))

            cv2.circle(frame, (widget.point + delta_point).to_int_tuple(),  int(self._res_scale * self._settings.joystick_widget_size), self._settings.color, -1)
            
        return frame

    def _handle_linear_widget(self, frame, widget: GUI_ControllerWidget, value):
        if self._settings.display_range_always or abs(value) > self._settings.linear_widget_threshold:
            dy = -value * self._settings.linear_widget_range

            start_point = Point(
                widget.point.x - self._settings.linear_widget_length,
                widget.point.y + dy
            )

            end_point = Point(
                widget.point.x + self._settings.linear_widget_length, 
                start_point.y
            )
            
            cv2.line(frame, start_point.to_int_tuple(), end_point.to_int_tuple(), self._settings.color, int(self._res_scale * self._settings.linear_widget_width))
        
        return frame

    def _frame_add_widget(self, frame, widget: GUI_ControllerWidget):
        value = widget.func()
        self._widgets_handlers[widget.widget_type](frame, widget, value)
        return frame 

    def get(self):
        frame = cv2.imread(self._image_path)
        for widget in self._widgets:
            frame = self._frame_add_widget(frame, widget)

        frame = cv2.resize(
            frame, 
            (int(frame.shape[1] * self._res_scale), int(frame.shape[0] * self._res_scale)),
            interpolation=cv2.INTER_AREA
        )

        return frame
    
    def register_default(self, positions: dict):
        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["one"],
            self._controller.get_btn_one
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["two"],
            self._controller.get_btn_two
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["two"],
            self._controller.get_btn_two
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["three"],
            self._controller.get_btn_three
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["four"],
            self._controller.get_btn_four
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["start"],
            self._controller.get_start_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["back"],
            self._controller.get_back_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["pov_up"],
            self._controller.get_pov_up_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["pov_down"],
            self._controller.get_pov_down_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["pov_left"],
            self._controller.get_pov_left_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["pov_right"],
            self._controller.get_pov_right_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["right_stick"],
            self._controller.get_right_stick_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["left_stick"],
            self._controller.get_left_stick_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["right_bumper"],
            self._controller.get_right_bumper_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.BOOL, 
            positions["left_bumper"],
            self._controller.get_left_bumper_btn
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.LINIEAR_Y, 
            positions["right_trigger"],
            self._controller.get_right_trigger_value
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.LINIEAR_Y, 
            positions["left_trigger"],
            self._controller.get_left_trigger_value
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.JOYSTICK, 
            positions["left_stick"],
            lambda: Point(self._controller.get_left_stick_x_value(), self._controller.get_left_stick_y_value())
        ))

        self.register(GUI_ControllerWidget(
            ControllerWidgetTypes.JOYSTICK, 
            positions["right_stick"],
            lambda: Point(self._controller.get_right_stick_x_value(), self._controller.get_right_stick_y_value())
        ))
