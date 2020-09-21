##########
# FILE: constants.py
# WRITER: Tom Nahum, CS Student at the Hebrew University of Jerusalem
# DESCRIPTION:
##########

TITLE = "My Calculator"
INIT_ANS = ""

# Arrows
DIS_SEP = "|"
EXP_SEP = ""
L_ARR = "◄"
R_ARR = "►"
R = 1
L = -1

# Errors:
SYNTAX_ERROR = "Syntax ERROR"
MATH_ERROR = "Math ERROR"
STACK_ERROR = "Stack ERROR"

# Screen properties:
S_COLOR = "grey15"
S_HEIGHT = 450
S_WIDTH = 330
SCREEN_SIZE = str(S_WIDTH) + "x" + str(S_HEIGHT)

# Font of keys:
FONT = 'Helvetica'

# Labels:
# Name label
NAME_LOC = (105, 35)
NAME_SIZE = (10, 120)
NAME_FG = "firebrick3"
NAME_T = "Super-Calculator"
NAME_S = 10
# Model label
MOD_LOC = (245, 5)
MOD_SIZE = (20, 80)
MOD_FG = "ivory3"
MOD_T = "Python 3"
MOD_S = 13
# Company label
COMP_LOC = (2, 7)
COMP_SIZE = (20, 80)
COMP_FG = "ivory3"
COMP_T = "CAS.IO"
COMP_S = 15

# Expression display banner properties:
DISPLAY_Y = 60
DISPLAY_X = 8
DISPLAY_W = 314
DISPLAY_H = 65
DISPLAY_FG = "midnight blue"
DISPLAY_BG = "PaleGreen4"
BORDER_SIZE = 3
D_F_SIZE = 25

# Buttons properties:
B_FG = "white"
# Gaps between buttons:
HEIGHT_GAP = 10
WIDTH_GAP = 5

# BUTTONS
# The text on the key:
# Special functions
SIN = "sin"
COS = "cos"
TAN = "tan"
EXP = "exp"
LN = "ln"
SQRT = "√"
LOG = "log"
# Arithmetic operands
MOD = "mod"
POW = "xⁿ"
POW_3 = "x³"
POW_2 = "x²"
DIVIDE = "÷"
MUL = "×"
L_CEIL = "⌈"
R_CEIL = "⌉"
R_FLOOR = "⌋"
L_FLOOR = "⌊"
# Specials keys:
AC = "AC"
DEL = "DEL"
ANS = "Ans"
EQUALS = "="
# Basic keys
NINE = "9"
EIGHT = "8"
SEVEN = "7"
SIX = "6"
FIVE = "5"
FOUR = "4"
THREE = "3"
TWO = "2"
ONE = "1"
ZERO = "0"
DOT = "."
L_PAR = "("
R_PAR = ")"
MINUS = "-"
PLUS = "+"

# The actual expression to execute:
# Special functions
OP_SIN = "math.sin("
OP_COS = "math.cos("
OP_TAN = "math.tan("
OP_EXP = "math.exp("
OP_LN = "math.log("
OP_SQRT = "math.sqrt("
# Arithmetic operands:
OP_MOD = "%"
OP_POW = "**"
OP_POW_3 = "**3"
OP_POW_2 = "**2"
OP_DIVIDE = "/"
OP_MUL = "*"
OP_R_CEIL = ")"
OP_L_CEIL = "math.ceil("
OP_R_FLOOR = ")"
OP_L_FLOOR = "math.floor("

# The text on the display banner:
POW_DIS = "^"
POW_3_DIS = "³"
POW_2_DIS = "²"

# Big buttons:
B1 = 0
B1_SIZE = 18
B1_COLOR = "gray9"
B1_HEIGHT = 40
B1_WIDTH = 60
# Small buttons:
B2 = 1
B2_SIZE = 13
B2_COLOR = "gray19"
B2_HEIGHT = 30
B2_WIDTH = 48
# Equals button:
B3 = 2
B3_WIDTH = B1_WIDTH * 2 + WIDTH_GAP
# AC and DEL buttons:
B4 = 3
B4_COLOR = "DarkOrange2"
B4_FG = "black"
# Arrows:
B5 = 4
B5_COLOR = "midnight blue"
