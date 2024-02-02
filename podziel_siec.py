import os
import glob
import shutil
from sklearn.model_selection import train_test_split

# Ścieżka do folderu nadrzędnego zawierającego foldery 'cars' i 'bikes'
base_folder = 'Dataset_5_percent'


# Folder docelowy, gdzie będą tworzone nowe foldery
destination_folder = 'Dataset_Siec_Podzielona'

# Utwórz foldery docelowe, jeśli nie istnieją
categories = ['Car', 'Bike']
for category in categories:
    os.makedirs(os.path.join(destination_folder, f"{category}_train"), exist_ok=True)
    os.makedirs(os.path.join(destination_folder, f"{category}_test"), exist_ok=True)

# Funkcja do kopiowania plików do odpowiednich folderów
def copy_files(files, destination):
    for file in files:
        shutil.copy(file, destination)

# Przetwarzaj każdą kategorię osobno
for category in categories:
    # Zbierz wszystkie pliki w folderze dla danej kategorii
    all_files = glob.glob(os.path.join(base_folder, category, "*.*"))

    # Podziel pliki na zestawy uczące i testowe
    train_files, test_files = train_test_split(all_files, test_size=0.3, random_state=42)

    # Skopiuj pliki do odpowiednich folderów
    copy_files(train_files, os.path.join(destination_folder, f"{category}_train"))
    copy_files(test_files, os.path.join(destination_folder, f"{category}_test"))

    print(f"Skopiowano {len(train_files)} plików do folderu {category}_train")
    print(f"Skopiowano {len(test_files)} plików do folderu {category}_test")
