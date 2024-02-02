import os
import shutil
import random

def move_random_images(source_folder, destination_folder, percentage=5):
    # Zbieranie wszystkich ścieżek do plików obrazowych
    image_paths = []
    for subdir, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                full_path = os.path.join(subdir, file)
                image_paths.append(full_path)
    
    # Obliczenie liczby plików do przeniesienia
    num_files_to_move = max(1, int(len(image_paths) * (percentage / 100)))
    
    # Wybieranie losowych plików do przeniesienia
    files_to_move = random.sample(image_paths, num_files_to_move)
    
    # Przenoszenie plików
    for file_path in files_to_move:
        # Tworzenie struktury katalogów w folderze docelowym, jeśli nie istnieje
        relative_path = os.path.relpath(file_path, source_folder)
        destination_path = os.path.join(destination_folder, relative_path)
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)
        
        # Przenoszenie pliku
        shutil.move(file_path, destination_path)
        print(f"Przeniesiono {file_path} -> {destination_path}")

# Ścieżka do folderu źródłowego
source_folder = 'Car-Bike-Dataset'

# Ścieżka do folderu docelowego
destination_folder = 'Dataset_5_percent'

# Utworzenie folderu docelowego, jeśli nie istnieje
os.makedirs(destination_folder, exist_ok=True)

# Uruchomienie funkcji
move_random_images(source_folder, destination_folder)
