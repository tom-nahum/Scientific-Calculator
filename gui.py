##########
# FILE: gui.py
# WRITER: Tom Nahum, CS Student at the Hebrew University of Jerusalem
# DESCRIPTION:
##########

from tkinter import *
import tkinter as tk
from tkinter import font as font
from constants import *
from functools import partial
from myButton import *
import math


def to_string(stack):
    return ''.join(stack)


def get_gap(t):
    if t == B1:
        return B1_HEIGHT, B1_WIDTH
    else:
        return B2_HEIGHT, B2_WIDTH


class Gui:
    arithmetic = {MOD: OP_MOD, POW: OP_POW, POW_3: OP_POW_3, POW_2: OP_POW_2,
                  DIVIDE: OP_DIVIDE, MUL: OP_MUL, PLUS: PLUS, MINUS: MINUS}
    functions = {SIN: OP_SIN, COS: OP_COS, TAN: OP_TAN, EXP: OP_EXP, LN: OP_LN,
                 SQRT: OP_SQRT}
    buttons = [[EQUALS, EQUALS, ANS, DOT, ZERO],
               [MINUS, PLUS, THREE, TWO, ONE],
               [DIVIDE, MUL, SIX, FIVE, FOUR],
               [AC, DEL, NINE, EIGHT, SEVEN],
               [MOD, POW, POW_3, POW_2, R_PAR, L_PAR],
               [LN, EXP, TAN, COS, SIN, SQRT],
               ["", "", "", "", "", ""]]

    def __init__(self):
        self.screen = tk.Tk()
        self.last_ans = "0"
        self.exp_stack = []
        self.display_stack = []
        self.display_exp = StringVar()
        self.init_screen()
        self.display = self.set_display_banner()

    def init_screen(self):
        self.screen.title(TITLE)
        self.screen.geometry(SCREEN_SIZE)
        self.screen.resizable(width=False, height=False)
        self.screen.configure(background=S_COLOR)
        self.set_labels()
        self.set_buttons()

    def set_labels(self):
        self.gen_label(NAME_S, NAME_T, NAME_FG, NAME_SIZE, NAME_LOC)
        self.gen_label(COMP_S, COMP_T, COMP_FG, COMP_SIZE, COMP_LOC)
        self.gen_label(MOD_S, MOD_T, MOD_FG, MOD_SIZE, MOD_LOC)

    def gen_label(self, text_size, text, fg, size, loc):
        label_font = font.Font(family=FONT, size=text_size, weight=font.BOLD)
        label = tk.Label(self.screen, text=text, bg=S_COLOR, font=label_font, fg=fg)
        label.pack()
        label.place(height=size[0], width=size[1], x=loc[0], y=loc[1])

    def set_display_banner(self):
        display_font = font.Font(family=FONT, size=D_F_SIZE)
        display = Entry(self.screen, textvariable=self.display_exp, bd=BORDER_SIZE,
                        bg=DISPLAY_BG, font=display_font, fg=DISPLAY_FG)
        display.pack()
        display.place(height=DISPLAY_H, width=DISPLAY_W, x=DISPLAY_X, y=DISPLAY_Y)
        return display

    def set_buttons(self):
        x = S_WIDTH - (2 * (WIDTH_GAP + B1_WIDTH))
        y = S_HEIGHT - (HEIGHT_GAP - WIDTH_GAP + B1_HEIGHT)
        i, j = 0, 0
        self.buttons_factory(EQUALS, B3, x, y)
        j = 2
        # create big buttons
        i, j, x, y = self.create_buttons(i, j, x, y, 4, 5, B1)
        y += HEIGHT_GAP
        # create small buttons
        self.create_buttons(i, j, x, y, 7, 6, B2)

    def create_buttons(self, i, j, x, y, rows, cols, t):
        height_gap, width_gap = get_gap(t)
        while i < rows:
            while j < cols:
                x -= (WIDTH_GAP + t * 0.7 + width_gap)
                key = self.buttons[i][j]
                self.buttons_factory(key, t, x, y)
                j += 1
            y -= (HEIGHT_GAP + height_gap)
            x = S_WIDTH
            j = 0
            i += 1
        return i, j, x, y

    def get_func(self, key):
        if key == EQUALS:
            return self.equals_func
        elif key == ANS:
            return self.ans_func
        elif key == DEL:
            return self.del_func
        elif key == AC:
            return self.ac_func
        else:
            return partial(self.key_func, key)

    def get_exp(self, key):
        if key in self.arithmetic:
            return self.arithmetic.get(key)
        elif key in self.functions:
            return self.functions.get(key)
        return key

    def buttons_factory(self, key, t, x, y):
        if key == AC or key == DEL:
            t = B4
        exp = self.get_exp(key)
        func = self.get_func(key)
        button = None
        if t == B1:
            button = StandardButton(key, exp, (x, y), func)
        elif t == B2:
            button = ExtraButton(key, exp, (x, y), func)
        elif t == B3:
            button = EqualsButton(key, exp, (x, y), func)
        elif t == B4:
            button = ResetButtons(key, exp, (x, y), func)
        button.create(self.screen)

    def key_func(self, key):
        if len(self.exp_stack) == 0 and self.last_ans != "0" and key in self.arithmetic:
            self.exp_stack.append(self.last_ans)
            self.display_stack.append(ANS)
        self.exp_stack.append(self.get_exp(key))
        if key in self.functions:
            self.display_stack.append(key + L_PAR)
        else:
            self.display_stack.append(key)
        self.display_exp.set(to_string(self.display_stack))

    def ans_func(self):
        self.exp_stack.append(self.last_ans)
        self.display_stack.append(ANS)
        self.display_exp.set(to_string(self.display_stack))

    def del_func(self):
        if len(self.exp_stack) != 0 and len(self.display_stack) != 0:
            self.exp_stack.pop()
            self.display_stack.pop()
            self.display_exp.set(to_string(self.display_stack))

    def ac_func(self):
        self.exp_stack.clear()
        self.display_stack.clear()
        self.display_exp.set(to_string(self.display_stack))

    def equals_func(self):
        try:
            result = str(eval(to_string(self.exp_stack)))
            self.display_exp.set(result)
            self.last_ans = result
            self.exp_stack.clear()
            self.display_stack.clear()
        except:  # TODO: split to cases of errors
            self.display_exp.set("ERROR")
            self.exp_stack.clear()
            self.display_stack.clear()
