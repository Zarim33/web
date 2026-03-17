import base64
import os

# Create a robust, simple BMP generation function (No external dependencies)
def create_color_bmp(filename, width, height, r, g, b):
    # BMP Header
    file_size = 54 + 3 * width * height
    padding = (4 - (width * 3) % 4) % 4
    pixel_data_size = (width * 3 + padding) * height
    
    header = bytearray([
        0x42, 0x4D,             # Signature
        file_size & 0xFF, (file_size >> 8) & 0xFF, (file_size >> 16) & 0xFF, (file_size >> 24) & 0xFF,
        0, 0, 0, 0,             # Reserved
        54, 0, 0, 0,            # Offset to data
        40, 0, 0, 0,            # DIB Header Size
        width & 0xFF, (width >> 8) & 0xFF, (width >> 16) & 0xFF, (width >> 24) & 0xFF,
        height & 0xFF, (height >> 8) & 0xFF, (height >> 16) & 0xFF, (height >> 24) & 0xFF,
        1, 0,                   # Planes
        24, 0,                  # Bits per pixel
        0, 0, 0, 0,             # Compression (none)
        pixel_data_size & 0xFF, (pixel_data_size >> 8) & 0xFF, (pixel_data_size >> 16) & 0xFF, (pixel_data_size >> 24) & 0xFF,
        0, 0, 0, 0,             # X ppm
        0, 0, 0, 0,             # Y ppm
        0, 0, 0, 0,             # Colors in palette
        0, 0, 0, 0              # Important colors
    ])
    
    # Pixel Data (BGR order, bottom-up)
    row = bytearray([b, g, r] * width) + bytearray(padding)
    data = row * height
    
    with open(filename, "wb") as f:
        f.write(header + data)
    print(f"Created {filename}")

# Create files in the AuraSite directory
base_dir = r"C:\Users\Miraz\AuraSite"
os.makedirs(base_dir, exist_ok=True)

# Generate Placeholders
# Logo: Purple
create_color_bmp(os.path.join(base_dir, "logo.png"), 100, 100, 155, 89, 182) # Purple
# Menu: Dark Grey
create_color_bmp(os.path.join(base_dir, "menu.png"), 400, 300, 40, 40, 40) # Dark Grey

# Base Finds (Various Colors)
colors = [
    (231, 76, 60),   # Red
    (230, 126, 34),  # Orange
    (241, 196, 15),  # Yellow
    (46, 204, 113),  # Green
    (52, 152, 219),  # Blue
    (155, 89, 182),  # Purple
    (236, 240, 241)  # White
]

for i, color in enumerate(colors):
    filename = os.path.join(base_dir, f"base{i+1}.png")
    create_color_bmp(filename, 300, 180, *color)

print("All placeholder images created successfully.")