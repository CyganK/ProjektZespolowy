import subprocess

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
