import os
from PIL import Image

def convert_images_to_png(root_dir):
    # Obsługiwane formaty plików obrazowych
    supported_formats = ('.jpg', '.jpeg', '.bmp', '.tif', '.tiff', '.gif', '.png')

    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(subdir, file)
            if file_path.lower().endswith(supported_formats):
                # Omit already PNG files
                if file_path.lower().endswith('.png'):
                    continue
                try:
                    with Image.open(file_path) as img:
                        # Zmiana nazwy oryginalnego pliku (opcjonalnie)
                        # os.rename(file_path, file_path + ".backup")
                        # Konwersja i zapis jako PNG
                        img.save(os.path.splitext(file_path)[0] + '.png')
                        print(f"Converted: {file_path} -> {os.path.splitext(file_path)[0] + '.png'}")
                except Exception as e:
                    print(f"Error converting {file_path}: {e}")


def delete_non_png_files(root_dir):
    for subdir, dirs, files in os.walk(root_dir):
        for file in files:
            if not file.lower().endswith('.png'):
                file_path = os.path.join(subdir, file)
                try:
                    os.remove(file_path)
                    print(f"Usunięto plik: {file_path}")
                except Exception as e:
                    print(f"Błąd przy usuwaniu {file_path}: {e}")




# Podaj ścieżkę do katalogu głównego z obrazami
root_dir = 'Dataset_5_percent'
convert_images_to_png(root_dir)
delete_non_png_files(root_dir)



