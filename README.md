# Projekt Deep Learning - Konrad Cygan - Klasyfikacja Obrazów

 

## Opis projektu

 

Ten projekt to aplikacja do klasyfikacji obrazów, wykorzystująca techniki uczenia głębokiego. Zawiera zestawy danych obrazów rowerów i samochodów, przygotowane do procesów trenowania i testowania modelu sieci neuronowych. Dane zostały pobrane ze strony Kaggle.com
W ramach projektu zostałe skonfigurowane narzedzie CI/CD Azure Devops oraz Pipeline odpowiedzialny za zarządzanie infrastrukturą oraz infrastruktura na chmurze azure zarządzana za pomocą kodu terraform.
Cała alpikacja jest skonteneryzowana za pomocą dockera oraz uruchomiona na kubernetesie, po zakończeniu działania wyniki sa publikowane w stora accouncie.

 

## Struktura repozytorium

 

Repozytorium składa się z następujących katalogów i plików:

 

- `Data`: Katalogi zawierające obrazy do procesów trenowania i testowania umieszczone w folderze Car-Bike_dataset pobranym z podanej strony.

- `App`:  Folder zawierający aplikację w pythonie

- `azurepipelines`: Pipeline'y CI/CD odpowiedzialne za uruchomienie aplikacji oraz stworzenie infrastruktury

- `Terraform`: Folder zawierający konfigurację IaC platformy Azure

- `Dockerfile`: Dockerfile budujący obraz aplikacji.

- `Requirements.txt`: Lista bibliotek python do zainstalowania.

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

- Azure

- Terraform

- Azure Devops YAML Pipeline

- Docker

- k8s

## Infrastruktura

- Azure Container Registry - przechowywanie obrazów 

- AKS - klaster k8s

- Storage Account - Miejsce przechowywania dannych w tym wypadku wyników skryptów

 

## Wymagania

 

- Python

- Tensorflow

- Torch

- TorchVision

- Sklearn

- numpy

- azure-storage-blob

- Docker

- K8s
 
## Uruchomienie Aplikacji na k8s

Uruchomienie aplikacji jest w pełni zautomatyzowane. Należu do folderu  `Data` zaimportować zbiór danych oraz wypchnąc zmiany do repo. 
Skonfigurowane narzędzia CI/CD automatycznie uruchomią aplikację na uprzednio stworzonym klastrze.


## Uruchomienie Programu Aplikacji

 

- Aby uruchomić program należy najpierw przygotować zbiór danych w tym wypadku zbiór podzielony na Bike oraz Car

- Przekonwertowanie wszystkic zdjęć na jednolity format(.png)

- Następnie można ograniczyć zbiór danych w tym wypadku do 5% aby skrócić czas pracy programy (get_5_percent.py)

- Podzielenie zbioru danych na uczące i testowe(podziel.py oraz podziel_siec.py)

- Przeniesienie danych do ostatecznych folderów - w przypadku sieci konwolucyjnej dodanie klas - w przypadku cross vall usunięcie kolejnych danych aby skrócić czas(move.py, move_siec.py)

- Uruchomienie algorytmów Deep Learning

- Opcjonalnie po przygotowaniu zbioru danych można uruchomic plik `run.py` który uruchomi wszystko w odpowiedniej kolejności i stworyz pliki wynikowe dla dwóch skryptów deep learningowych

 

