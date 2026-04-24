import os

folders = [
    "core",
    "fractals",
    "projections",
    "interactive",
    "physics",
    "assets",
    "legacy"
]

files = [
    "README.md",
    "main.py",
    "banner.svg",
    "core/fractal_engine.py",
    "core/renderer.py",
    "core/config.py"
]

# create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# create empty files
for file in files:
    with open(file, "w") as f:
        pass

print("✅ Project structure created successfully!")