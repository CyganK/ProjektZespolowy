import os
import shutil
import glob
import random

def copy_images_to_class_folders(source_root_folder, dest_root_folder, extension="*.png"):
    # Definiowanie podfolderów, które będą przetwarzane
    subfolders = ['Bike_train', 'Bike_test', 'Car_train', 'Car_test']

    for subfolder in subfolders:
        source_folder = os.path.join(source_root_folder, subfolder)
        print(source_folder)
        # Sprawdzanie, czy folder źródłowy istnieje
        if not os.path.exists(source_folder):
            print(f"Folder źródłowy nie istnieje: {source_folder}")
            continue

        image_files = glob.glob(os.path.join(source_folder, extension))
        print(image_files)
        random.shuffle(image_files)  # Mieszanie plików
        half = len(image_files) // 2  # Punkt podziału

        # Definiowanie ścieżek folderów docelowych
        dest_class_1_folder = os.path.join(dest_root_folder, subfolder, 'klasa_1')
        print(dest_class_1_folder)
        dest_class_2_folder = os.path.join(dest_root_folder, subfolder, 'klasa_2')
        print(dest_class_2_folder)

        # Tworzenie folderów docelowych, jeśli nie istnieją
        os.makedirs(dest_class_1_folder, exist_ok=True)
        os.makedirs(dest_class_2_folder, exist_ok=True)

        # Kopiowanie plików
        for file in image_files[:half]:
            shutil.copy(file, dest_class_1_folder)
            print(f"Skopiowano {file} do {dest_class_1_folder}")
        for file in image_files[half:]:
            shutil.copy(file, dest_class_2_folder)
            print(f"Skopiowano {file} do {dest_class_2_folder}")

# Ścieżka do folderu źródłowego
source_root_folder = 'Dataset_Siec_Podzielona'
# Ścieżka do folderu docelowego
dest_root_folder = 'Dataset_Siec'

# Uruchomienie funkcji
copy_images_to_class_folders(source_root_folder, dest_root_folder)
