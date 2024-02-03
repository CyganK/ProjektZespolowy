# Projekt Deep Learning - Konrad Cygan - Klasyfikacja Obrazów

 

## Opis projektu

 

Ten projekt to aplikacja do klasyfikacji obrazów, wykorzystująca techniki uczenia głębokiego. Zawiera zestawy danych obrazów rowerów i samochodów, przygotowane do procesów trenowania i testowania modelu sieci neuronowych. Dane zostały pobrane ze strony Kaggle.com

 

## Struktura repozytorium

 

Repozytorium składa się z następujących katalogów i plików:

 

- `Car-Bike`: Katalogi zawierające obrazy do procesów trenowania i testowania umieszczone w folderze Car-Bike_dataset pobranym z podanej strony.

- `Dataset`: Podzielone zbiory danych do trenowania i testowania dla cros vall.

- `Dataset_5_percent`: Mniejsze wersje zbiorów danych, zawierające 5% oryginalnych danych.

- `Dataset_Podzielona`: Specjalnie podzielone zbiory danych do eksperymentów dla cros vall.

- `Dataset_Siec_Podzielona`: Specjalnie podzielone zbiory danych do eksperymentów dla sieci konwolucyjnej.

- `Dataset_Siec`: Zbiory danych dostosowane do trenowania sieci konwolucyjnej.

- Skrypty Pythona:

  - `convert.py`: Skrypt do konwersji danych.

  - `result_custom_dataset_cros_vall.txt`: Wyniki pliku custom_dataset_cros_vall.py.

  - `result_siec_konwolucyjna_pytorch2.txt`: Wyniki pliku siec_konwolucyjna_pytorch2.py.

  - `custom_dataset_cros_vall.py`: Skrypt do przeprowadzania walidacji krzyżowej.

  - `get_5_percent.py`: Skrypt do przygotowywania 5% zbiorów danych.

  - `move_siec.py`, `move.py`: Skrypty do manipulacji zbiorami danych.

  - `podziel_siec.py`, `podziel.py`: Skrypty do dzielenia zbiorów danych.

  - `siec_konwolucyjna_pytorch2.py`: Główny skrypt do trenowania sieci konwolucyjnej.

  - `run.py`: Plik uruchamiający wszystkie skrypty w odpowiedniej kolejności.

 

## Technologie

 

- Python

- PyTorch (dokładne wersje zależności są określone w pliku `requirements.txt`)

 

## Wymagania

 

- Python

- Tensorflow

- Torch

- TorchVision

- Sklearn

- numpy

 

## Uruchomienie

 

- Aby uruchomić program należy najpierw przygotować zbiór danych w tym wypadku zbiór podzielony na Bike oraz Car

- Przekonwertowanie wszystkic zdjęć na jednolity format(.png)

- Następnie można ograniczyć zbiór danych w tym wypadku do 5% aby skrócić czas pracy programy (get_5_percent.py)

- Podzielenie zbioru danych na uczące i testowe(podziel.py oraz podziel_siec.py)

- Przeniesienie danych do ostatecznych folderów - w przypadku sieci konwolucyjnej dodanie klas - w przypadku cross vall usunięcie kolejnych danych aby skrócić czas(move.py, move_siec.py)

- Uruchomienie algorytmów Deep Learning

- Opcjonalnie po przygotowaniu zbioru danych można uruchomic plik `run.py` który uruchomi wszystko w odpowiedniej kolejności i stworyz pliki wynikowe dla dwóch skryptów deep learningowych

 

