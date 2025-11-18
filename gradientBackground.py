from PIL import Image, ImageDraw, ImageEnhance

# Define gradient colours using RGB values 
# You can add more colours to create different blended backgrounds
colours = [
    (71, 146, 207),  # blue
    (115, 91, 168),  # purple
    (206, 66, 122),  # magenta
    (235, 131, 55),  # orange
    (234, 80, 73),   # red
]

# Image size (HD slide background)
width, height = 1920, 1080
gradient = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(gradient)

# Draw horizontal smooth gradient
for x in range(width):
    ratio = x / (width - 1)
    idx = int(ratio * (len(colours) - 1))
    next_idx = min(idx + 1, len(colours) - 1)
    local_ratio = (ratio * (len(colours) - 1)) - idx

    # Linear interpolation between colours
    r = int(colours[idx][0] * (1 - local_ratio) + colours[next_idx][0] * local_ratio)
    g = int(colours[idx][1] * (1 - local_ratio) + colours[next_idx][1] * local_ratio)
    b = int(colours[idx][2] * (1 - local_ratio) + colours[next_idx][2] * local_ratio)
    draw.line([(x, 0), (x, height)], fill=(r, g, b))

# Apply brightness and contrast enhancements
brightness_factor = 1.0  # 1.0 means no change, >1.0 brighter, <1.0 darker
contrast_factor = 1.0   # 1.0 means no change, >1.0 more contrast, <1.0 less contrast

enhancer = ImageEnhance.Brightness(gradient)
gradient = enhancer.enhance(brightness_factor)

enhancer = ImageEnhance.Contrast(gradient)
gradient = enhancer.enhance(contrast_factor)

# Save your background
gradient.save("gradient_background.png")
print("Saved as gradient_background.png")
