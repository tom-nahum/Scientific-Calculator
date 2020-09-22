##########
# FILE: gui.py
# WRITER: Tom Nahum, CS Student at the Hebrew University of Jerusalem
# DESCRIPTION:
##########

from tkinter import *
from functools import partial
from my_button import *
import math


def sin(x):
    return math.sin(math.radians(x))


def cos(x):
    return math.cos(math.radians(x))


def tan(x):
    return math.tan(math.radians(x))


class Gui:
    arithmetic = {MOD: OP_MOD, POW: OP_POW, POW_3: OP_POW_3, POW_2: OP_POW_2,
                  DIVIDE: OP_DIVIDE, MUL: OP_MUL, PLUS: PLUS, MINUS: MINUS}
    functions = {SQRT: OP_SQRT, SIN: OP_SIN, COS: OP_COS, TAN: OP_TAN, EXP: OP_EXP,
                 LN: OP_LN}
    powers = {POW_2: POW_2_DIS, POW_3: POW_3_DIS, POW: POW_DIS}
    rounding = {L_FLOOR: OP_L_FLOOR, R_FLOOR: OP_R_FLOOR, L_CEIL: OP_L_CEIL,
                R_CEIL: OP_R_CEIL}
    buttons = [[(EQUALS, B3), (EQUALS, B3), (ANS, B1), (DOT, B1), (ZERO, B1)],
               [(MINUS, B1), (PLUS, B1), (THREE, B1), (TWO, B1), (ONE, B1)],
               [(DIVIDE, B1), (MUL, B1), (SIX, B1), (FIVE, B1), (FOUR, B1)],
               [(AC, B4), (DEL, B4), (NINE, B1), (EIGHT, B1), (SEVEN, B1)],
               [(POW, B2), (POW_3, B2), (POW_2, B2), (SQRT, B2), (R_PAR, B2),
                (L_PAR, B2)],
               [(MOD, B2), (LN, B2), (EXP, B2), (TAN, B2), (COS, B2), (SIN, B2)],
               [(R_FLOOR, B2), (L_FLOOR, B2), (R_ARR, B5), (L_ARR, B5), (R_CEIL, B2),
                (L_CEIL, B2)]]

    def __init__(self):
        self.screen = tk.Tk()
        self.exp_stack = [(EXP_SEP, DIS_SEP)]
        self.last_ans = INIT_ANS
        self.is_error = False
        self.is_answer = False
        self.cur_idx = 0
        self.init_screen()
        self.display_var = StringVar()
        self.display_banner = self.set_display_banner()
        self.display_exp()
        self.screen.after(CURSOR_BLINK, self.set_cursor)

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
        display = Entry(self.screen, textvariable=self.display_var, bd=BORDER_SIZE,
                        bg=DISPLAY_BG, font=display_font, fg=DISPLAY_FG)
        display.pack()
        display.place(height=DISPLAY_H, width=DISPLAY_W, x=DISPLAY_X, y=DISPLAY_Y)
        return display

    def set_cursor(self):
        if not self.is_answer and not self.is_error:
            cur = self.exp_stack[self.cur_idx]
            if cur[1] == DIS_SEP:
                self.exp_stack[self.cur_idx] = (EXP_SEP, "")
            elif cur[1] == "":
                self.exp_stack[self.cur_idx] = (EXP_SEP, DIS_SEP)
            self.display_exp()
        self.screen.after(400, self.set_cursor)

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
        if t == B1:
            height_gap, width_gap = B1_HEIGHT, B1_WIDTH
        else:
            height_gap, width_gap = B2_HEIGHT, B2_WIDTH
        while i < rows:
            while j < cols:
                x -= (WIDTH_GAP + t * 0.7 + width_gap)
                key = self.buttons[i][j][0]
                b_type = self.buttons[i][j][1]
                self.buttons_factory(key, b_type, x, y)
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
        elif key == L_ARR:
            return partial(self.arrow_func, L)
        elif key == R_ARR:
            return partial(self.arrow_func, R)
        else:
            return partial(self.key_func, key)

    def buttons_factory(self, key, t, x, y):
        func = self.get_func(key)
        button = None
        if t == B1:
            button = StandardButton(key, (x, y), func)
        elif t == B2:
            button = ExtraButton(key, (x, y), func)
        elif t == B3:
            button = EqualsButton(key, (x, y), func)
        elif t == B4:
            button = ResetButtons(key, (x, y), func)
        elif t == B5:
            button = ArrowButton(key, (x, y), func)
        button.create(self.screen)

    def display_exp(self):
        cur_dis = "".join(elem[1] for elem in self.exp_stack)
        self.display_var.set(cur_dis)

    def add_elem(self, exp_elem, dis_elem):
        self.exp_stack = self.exp_stack[:self.cur_idx] + [(exp_elem, dis_elem)] + \
                         [(EXP_SEP, DIS_SEP)] + self.exp_stack[self.cur_idx + 1:]

    def remove_elem(self):
        self.exp_stack = self.exp_stack[:self.cur_idx - 1] + self.exp_stack[self.cur_idx:]

    # def print_exp(self):
    #     exp = "".join(elem[0] for elem in self.exp_stack)
    #     dis = "".join(elem[1] for elem in self.exp_stack)
    #     print("Exp: ", exp, "\t", "Dis: ", dis)

    def get_exp(self, key):
        if key in self.arithmetic:
            return self.arithmetic.get(key)
        elif key in self.functions:
            return self.functions.get(key)
        elif key in self.rounding:
            return self.rounding.get(key)
        return key

    def get_dis(self, key):
        if key in self.functions:
            return key + L_PAR
        elif key in self.powers:
            return self.powers.get(key)
        else:
            return key

    def arrow_func(self, direct):
        if not self.is_error and \
                not ((direct == L and self.cur_idx == 0) or
                     (direct == R and self.cur_idx == len(self.exp_stack) - 1)):
            self.is_answer = False
            self.exp_stack[self.cur_idx] = self.exp_stack[self.cur_idx + direct]
            self.exp_stack[self.cur_idx + direct] = (EXP_SEP, DIS_SEP)
            self.display_exp()
            self.cur_idx += direct

    def check_power(self):
        if self.cur_idx - 1 >= 0 and \
                self.exp_stack[self.cur_idx - 1][1] in self.powers.values():
            return True
        elif self.cur_idx + 1 <= len(self.exp_stack) - 1 and \
                self.exp_stack[self.cur_idx + 1][1] in self.powers.values():
            return True
        else:
            return False

    def key_func(self, key):
        if not self.is_error:
            self.is_answer = False
            if len(self.exp_stack) == 1 and self.last_ans != INIT_ANS \
                    and key in self.arithmetic:
                self.add_elem(self.last_ans, ANS)
                self.cur_idx += 1
            if key in self.powers and self.check_power():
                return
            self.add_elem(self.get_exp(key), self.get_dis(key))
            self.cur_idx += 1
            self.display_exp()

    def ans_func(self):
        if not self.is_error:
            self.is_answer = False
            self.add_elem(self.last_ans, ANS)
            self.cur_idx += 1
            self.display_exp()

    def del_func(self):
        if not self.is_error and len(self.exp_stack) != 1:
            self.is_answer = False
            self.remove_elem()
            self.cur_idx -= 1
            self.display_exp()

    def ac_func(self):
        if self.is_error:
            self.is_error = False
            self.last_ans = INIT_ANS
        self.is_answer = False
        self.exp_stack = [(EXP_SEP, DIS_SEP)]
        self.cur_idx = 0
        self.display_exp()

    def equals_func(self):
        if not self.is_error:
            try:
                if len(self.exp_stack) == 1:
                    self.display_var.set(self.last_ans)
                else:
                    expression = "".join(elem[0] for elem in self.exp_stack)
                    result = str(eval(expression))[:MAX_CHARS_NUM]
                    self.display_var.set(result)
                    self.last_ans = result
            except OverflowError:
                self.display_var.set(STACK_ERROR)
                self.is_error = True
            except (ZeroDivisionError, ValueError):
                self.display_var.set(MATH_ERROR)
                self.is_error = True
            except SyntaxError:
                self.display_var.set(SYNTAX_ERROR)
                self.is_error = True
            finally:
                self.is_answer = True
                self.exp_stack = [(EXP_SEP, DIS_SEP)]
                self.cur_idx = 0
