import os
import requests
import zipfile
import io

async def get_font():
    url = "https://download.microsoft.com/download/8/6/0/860a94fa-7feb-44ef-ac79-c072d9113d69/Microsoft%20Aptos%20Fonts.zip"
    
    font_folder = "fonts"
    font_path = os.path.join(font_folder, "Aptos.ttf")
    font_bold_path = os.path.join(font_folder, "Aptos.ttf")

    if os.path.exists(font_path) and os.path.exists(font_bold_path):
        print(f"Aptos.ttf & Aptos-Bold.ttf already exists in the '{font_folder}' folder. Skipping download.")
        return
    
    os.makedirs(font_folder, exist_ok=True)
    
    response = requests.get(url)
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    
    for file in zip_file.namelist():
        if file.endswith("Aptos.ttf"):
            zip_file.extract(file, font_folder)
            print(f"Aptos.ttf has been saved to the '{font_folder}' folder.")
        if file.endswith("Aptos-Bold.ttf"):
            zip_file.extract(file, font_folder)
            print(f"Aptos-Bold.ttf has been saved to the '{font_folder}' folder.")
    
    zip_file.close()