import os

def create_folders():
    folders = ["data", "models", "images", "outputs"]
    for f in folders:
        os.makedirs(f, exist_ok=True)