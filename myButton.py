##########
# FILE: constants.py
# WRITER: Tom Nahum, CS Student at the Hebrew University of Jerusalem
# DESCRIPTION:
##########

from abc import ABC
import tkinter as tk
from tkinter import font as font
from constants import *


class MyButton(ABC):

    def __init__(self, key, loc, func):
        self.size = None
        self.color = None
        self.height = None
        self.width = None
        self.font_color = B_FG
        self.key = key
        self.func = func
        self.x = loc[0]
        self.y = loc[1]

    def create(self, screen):
        button_font = font.Font(family=FONT, size=self.size, weight=font.BOLD)
        button = tk.Button(screen, text=self.key, command=self.func, bg=self.color,
                           fg=self.font_color, font=button_font)
        button.pack()
        button.place(height=self.height, width=self.width, x=self.x, y=self.y)


class StandardButton(MyButton):
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.size = B1_SIZE
        self.color = B1_COLOR
        self.height = B1_HEIGHT
        self.width = B1_WIDTH


class ExtraButton(MyButton):
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.size = B2_SIZE
        self.color = B2_COLOR
        self.height = B2_HEIGHT
        self.width = B2_WIDTH


class ArrowButton(ExtraButton):
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.color = B5_COLOR


class EqualsButton(MyButton):
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.size = B1_SIZE
        self.color = B1_COLOR
        self.height = B1_HEIGHT
        self.width = B3_WIDTH


class ResetButtons(MyButton):
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.size = B1_SIZE
        self.color = B4_COLOR
        self.height = B1_HEIGHT
        self.width = B1_WIDTH
        self.font_color = B4_FG
