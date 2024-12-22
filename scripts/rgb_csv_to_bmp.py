import csv
from PIL import Image

# Example: 16x16 image (adjust based on your actual data size)
# width, height = 16, 36  # You can modify this to match your actual image dimensions

output_file = 'output_palette.raw' 

# Read the CSV file
with open('out_pal.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    hex_colors = []
    for row in reader:
        for color in row:
            # Strip spaces, and split by commas if necessary (e.g., "FEFEFE, DCDCDC")
            cleaned_colors = [c.strip() for c in color.split(',')]  # Split by commas and strip spaces
            hex_colors.extend(cleaned_colors)

    for color in hex_colors[:32]:
        print(color)

    # # Create a new blank image with RGB mode
    # image = Image.new('RGB', (width, height))

    # Convert hex colors to RGB tuples and populate the image
    pixels = []
    for color in hex_colors:
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        pixels.append((r, g, b))

# Write the pixel data to a raw output file
    with open(output_file, 'wb') as f:
        for pixel in pixels:
            # Write each pixel as 3 bytes (RGB) to the file
            f.write(bytes(pixel))  # `bytes(pixel)` converts the tuple (r, g, b) into a bytes object

    print(f"Raw image data written to {output_file} successfully!")


    # for pixel in pixels[:16]:
    #     print(pixel)

    # # Fill the image with the pixel data
    # image.putdata(pixels)

    # # Save the image as a BMP file
    # image.save('output_image.bmp')

    # print("BMP image created successfully!")