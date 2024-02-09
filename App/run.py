import subprocess
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

#Zdefiniuj swoje dane uwierzytelniające i nazwę kontenera
connection_string = os.getenv('CONNECTION_STRING')
container_name = os.getenv('CONTAINER_NAME')



# Tworzenie klienta usługi blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)



# Definiuj kolejność plików do uruchomienia
pliki_do_uruchomienia = ['get_5_percent.py', 'convert.py', 'podziel.py', 'podziel_siec.py','move.py','move_siec.py']

# Uruchom każdy plik .py po kolei zgodnie z zdefiniowaną kolejnością
for plik in pliki_do_uruchomienia:
    print(f"Running {plik}...")
    subprocess.run(["python", plik])
    print(f"Process Finished.")

dodatkowe_skrypty = ['siec_konwolucyjna_pytorch2.py', 'custom_dataset_cros_vall.py']

# Uruchom dodatkowe skrypty, każdy z własnym plikiem wyjściowym
for plik in dodatkowe_skrypty:
    nazwa_pliku_wyjsciowego = f"result_{plik[:-3]}.txt"  # Usuń .py i dodaj .txt
    print(f"Running {plik}..")
    with open(nazwa_pliku_wyjsciowego, 'w') as plik_wyjsciowy:
        subprocess.run(["python", plik], stdout=plik_wyjsciowy)
    print(f"Process Finished")

    # Przesyłanie wygenerowanych plików do Azure Blob Storage
    blob_client = container_client.get_blob_client(blob=nazwa_pliku_wyjsciowego)
    with open(nazwa_pliku_wyjsciowego, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        print(f"File {nazwa_pliku_wyjsciowego} uploaded to blob storage.")
