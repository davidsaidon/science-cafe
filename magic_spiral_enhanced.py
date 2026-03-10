"""
🌀 MAGIC COLOUR SPIRAL — ENHANCED
==================================
Press 1–9 (or 0) to draw a different shape!
Each number uses a different angle — totally different pattern.
The window stays open so you can keep pressing numbers.

To run: python3 magic_spiral_enhanced.py
Press Escape or close the window to quit.
"""

import turtle

# =============================================
# 🎨 CHANGE THESE TO WHATEVER THE KIDS SHOUT!
# =============================================
COLOURS = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan"]

# Each key (1–9, 0) maps to a different angle → totally different shape
ANGLE_MAP = {
    "1": 59,  # 5-pointed star feel
    "2": 72,  # pentagon spiral
    "3": 91,  # almost-square wobbly spiral
    "4": 100,  # wide open spiral
    "5": 115,  # chunky petal shapes
    "6": 121,  # overlapping petals
    "7": 137,  # the classic golden angle sunflower 🌻
    "8": 144,  # 5-fold symmetry
    "9": 170,  # very tight, dense spiral
    "0": 222,  # mirror-like curves
}

SHAPE_NAMES = {
    "1": "Star Spiral",
    "2": "Pentagon Swirl",
    "3": "Wobbly Square",
    "4": "Open Galaxy",
    "5": "Chunky Petals",
    "6": "Rose Window",
    "7": "Sunflower ✨",
    "8": "Five-Fold Star",
    "9": "Dense Web",
    "0": "Mirror Curves",
}

# ─────────────────────────────────────────────
# Setup
# ─────────────────────────────────────────────
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("✨ Magic Colour Spiral — Press 1 to 0 for different shapes! ✨")
screen.tracer(0)  # We'll update manually for speed

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)
pen.hideturtle()

# Label turtle (shows shape name at top)
label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color("white")
label.goto(0, screen.window_height() // 2 - 40)


def draw_spiral(angle):
    """Clear and draw a fresh spiral with the given angle."""
    screen.tracer(0)
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    pen.pendown()

    for i in range(200):
        pen.color(COLOURS[i % len(COLOURS)])
        pen.forward(i * 1.5)
        pen.left(angle)

    screen.update()
    screen.tracer(1)  # Re-enable live drawing for next call


def on_key(key):
    '''Handle key press events.'''
    angle = ANGLE_MAP[key]
    name = SHAPE_NAMES[key]

    # Update the title label
    label.clear()
    label.write(
        f"Shape {key}: {name}  (angle {angle}°)",
        align="center",
        font=("Arial", 14, "bold"),
    )

    draw_spiral(angle)


# ─────────────────────────────────────────────
# Bind keys 1–9 and 0
# ─────────────────────────────────────────────
for k in ANGLE_MAP:
    screen.onkey(lambda key=k: on_key(key), key=k)

screen.onkey(screen.bye, "Escape")
screen.listen()

# Draw the default shape on launch (key "7" = sunflower)
on_key("7")

# ─────────────────────────────────────────────
# Welcome message in terminal
# ─────────────────────────────────────────────
print()
print("✨ Magic Colour Spiral is running!")
print("─" * 38)
for k, name in SHAPE_NAMES.items():
    angle = ANGLE_MAP[k]
    print(f"  Press {k}  →  {name:20s} (angle {angle}°)")
print("─" * 38)
print("  Press Escape to quit.")
print()

screen.mainloop()
