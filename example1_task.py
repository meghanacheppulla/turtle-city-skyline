
import turtle
import random

# ---------- SCREEN SETUP ----------
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.bgcolor("#87CEEB")  # sky blue theme
screen.title("Turtle City Skyline")

t = turtle.Turtle()
t.speed(0)          # fastest drawing speed
t.hideturtle()

# ---------- COLOR THEME ----------
building_colors = ["#4B5D67", "#3E4C59", "#2C3E50", "#546E7A", "#37474F"]
window_color = "#FFD54F"   # warm yellow windows
ground_color = "#7CB342"   # green ground


def draw_rectangle(x, y, width, height, color):
    """Draw a filled rectangle starting from bottom-left corner (x, y)."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_windows(x, y, width, height, rows, cols):
    """Draw a grid of small windows inside a building."""
    padding_x = width * 0.15
    padding_y = height * 0.1
    win_w = (width - 2 * padding_x) / cols * 0.6
    win_h = (height - 2 * padding_y) / rows * 0.5

    gap_x = (width - 2 * padding_x) / cols
    gap_y = (height - 2 * padding_y) / rows

    for r in range(rows):
        for c in range(cols):
            wx = x + padding_x + c * gap_x
            wy = y + padding_y + r * gap_y
            draw_rectangle(wx, wy, win_w, win_h, window_color)


def draw_building(x, width, height, rows, cols):
    color = random.choice(building_colors)
    draw_rectangle(x, -200, width, height, color)   # -200 = ground level
    draw_windows(x, -200, width, height, rows, cols)


def draw_ground():
    draw_rectangle(-450, -250, 900, 50, ground_color)


def draw_sun():
    t.penup()
    t.goto(350, 220)
    t.pendown()
    t.fillcolor("#FFEB3B")
    t.begin_fill()
    t.circle(40)
    t.end_fill()


# ---------- DRAW SCENE ----------
draw_sun()
draw_ground()

# Draw a row of buildings with varying width/height
x_pos = -430
while x_pos < 430:
    width = random.randint(60, 100)
    height = random.randint(150, 350)
    rows = random.randint(4, 7)
    cols = random.randint(2, 4)
    draw_building(x_pos, width, height, rows, cols)
    x_pos += width + 10

turtle.done()
