import os
from pathlib import Path
from PIL import Image

# Paths (adjust if needed)
png_path = Path(r"C:/Users/HP/.gemini/antigravity-ide/brain/292162ef-e914-4950-a577-107250fd967f/app_demo_1782113566004.png")
pdf_path = Path(r"C:/Users/HP/New folder (3)/resume_sorter/demo.pdf")

if not png_path.is_file():
    raise FileNotFoundError(f"Demo image not found: {png_path}")

# Open the PNG and convert to PDF (RGB mode required)
with Image.open(png_path) as img:
    rgb_img = img.convert("RGB")
    rgb_img.save(pdf_path, "PDF", resolution=100.0)

print(f"PDF created at: {pdf_path}")
