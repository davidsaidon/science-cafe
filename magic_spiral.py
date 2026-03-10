"""
🌀 MAGIC COLOUR SPIRAL
======================
Run this script and ask the kids to shout out colours!
Change the COLOURS list below to whatever they suggest.

To run: python3 magic_spiral.py
Press Ctrl+C or close the window to stop.
"""

import random
import turtle

# =============================================
# 🎨 CHANGE THESE TO WHATEVER THE KIDS SHOUT!
# =============================================
COLOURS = ["red", "blue", "green", "orange", "purple", "yellow", "pink", "cyan"]

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("✨ Magic Colour Spiral ✨")

# Create the turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest
pen.width(2)

# Draw the spiral
for i in range(200):
    pen.color(COLOURS[i % len(COLOURS)])
    pen.forward(i * 1.5)
    pen.left(137)  # Try 59, 72, 91, and 137

pen.hideturtle()
screen.mainloop()
