from PIL import Image
import os

src = "b_1bed54cd1a07039dbf2d0f278dd9c191.jpg"
img = Image.open(src).convert("RGBA")

# favicon.ico (multi-size ICO, just use 32x32 as base)
fav_sizes = [(16, 16), (32, 32), (48, 48)]
icons = [img.resize(s, Image.LANCZOS) for s in fav_sizes]
img32 = icons[1]
img32.save("favicon.ico", format="ICO", sizes=[(32, 32)])

# favicon-32.png
img.resize((32, 32), Image.LANCZOS).save("favicon-32.png")

# favicon-192.png
img.resize((192, 192), Image.LANCZOS).save("favicon-192.png")

# favicon-512.png
img.resize((512, 512), Image.LANCZOS).save("favicon-512.png")

# apple-touch-icon.png (180x180)
img.resize((180, 180), Image.LANCZOS).save("apple-touch-icon.png")

# og-default.png (1200x630)
img.resize((1200, 630), Image.LANCZOS).save("og-default.png")

# babel-icon.png
img.resize((256, 256), Image.LANCZOS).save("babel-icon.png")

# lumera-logo.svg - can't convert PNG to SVG trivially, skip or warn
print("Done! lumera-logo.svg skipped (SVG can't be auto-generated from raster)")
