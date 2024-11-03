#!/usr/bin/env python 

import datetime

# Define the Gauntlet color palette in RGB format
palette = [
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),
    (0, 0, 0),          # Black
    (255, 255, 255),    # White
    (255, 0, 0),        # Red
    (0, 255, 255),      # Cyan
    (128, 0, 128),      # Purple
    (0, 255, 0),        # Green
    (255, 255, 0),      # Yellow
    (192, 192, 192),    # Light Gray
    (128, 128, 128),    # Dark Gray
    (255, 165, 0),      # Orange
    (139, 69, 19),      # Brown
    (144, 238, 144),    # Light Green
    (0, 0, 255),        # Blue
    (230, 230, 250),    # Light Purple
    (139, 0, 0),        # Dark Red
    (255, 255, 224)     # Light Yellow
]

current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")  # Format: YYYY-MM-DD_HH-MM-SS
palette_file = f'gauntlet_palette_{current_datetime}.pal'

#Open a binary file for writing
with open(palette_file, 'wb') as f:
    for r, g, b in palette:
        # Write Blue, Green, Red,
        f.write(bytes([r, g, b, 255])) 

# print("Palette written to gauntlet_palette.pal")

# with open('gauntlet_palette.pal', 'wb') as f:
#     for r, g, b in palette:
#         # Pack each color into a single 32-bit integer (little-endian)
#         # The format will be BGRA
#         color = (b) | (g << 8) | (r << 16) | (255 << 24)  # Alpha is 255
#         f.write(color.to_bytes(4, byteorder='little'))  # Write as 4 bytes

print("Palette written")