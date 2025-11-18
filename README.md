![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

# Gradient Background Generator

A Python script that generates high-quality, smooth horizontal gradients using linear interpolation. The script blends multiple RGB colors to create a 1920x1080 (HD) image, perfect for slide backgrounds or wallpapers.

## Features

  * **Customizable Colors:** Easily modify the RGB values to create your own palette.
  * **High Definition:** Generates a 1920x1080 image by default.
  * **Smooth Transitions:** Uses mathematical linear interpolation to blend colors without banding.

## Prerequisites

You need **Python 3** and the **Pillow** library installed.

```bash
pip install Pillow
```

## Usage

1.  Open the script in your code editor.
2.  Run the script via the command line:

<!-- end list -->

```bash
python gradientBackground.py
```

3.  The script will generate a file named `gradient_background.png` in the same directory.

## Customization

### Changing Colors

To change the color palette, modify the `colours` list in the script. You can add or remove as many RGB tuples as you like.

```python
colours = [
    (71, 146, 207),  # Blue
    (255, 0, 0),     # Red (Example change)
    # Add more (R, G, B) tuples here...
]
```

### Changing Size

To change the output resolution, update the `width` and `height` variables:

```python
width, height = 3840, 2160  # Example for 4K
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
