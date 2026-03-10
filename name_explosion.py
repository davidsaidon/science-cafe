"""
📛 NAME EXPLOSION
=================
Ask a kid their name, then watch it explode across the screen!

To run: python3 name_explosion.py
"""

import time
import random
import os

# Ask for the name
name = input("\n🎤 What's your name? → ")

# Clear screen
os.system('clear' if os.name != 'nt' else 'cls')

# Emojis to scatter around
emojis = ["⭐", "🚀", "🎉", "💥", "🌈", "✨", "🔥", "🎮", "🤖", "💎", "🦄", "🌟"]

# Print it in a fun growing pattern
for i in range(1, 20):
    emoji = random.choice(emojis)
    spaces = " " * random.randint(0, 30)
    print(f"{spaces}{emoji} {'  '.join(name.upper() * min(i, 5))} {emoji}")
    time.sleep(0.15)

print("\n")
print("=" * 50)
print(f"   🤖 The computer says: Hello {name}!!!")
print(f"   🤖 Your name has {len(name)} letters")
print(f"   🤖 Backwards, you'd be called: {name[::-1]}")
print(f"   🤖 In secret code: {' '.join(str(ord(c)) for c in name)}")
print("=" * 50)

input("\n Press Enter for the next person...")
