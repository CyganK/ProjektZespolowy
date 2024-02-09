# Używamy oficjalnego obrazu Pythona z Docker Hub jako obrazu bazowego
FROM python:3.8-slim

# Ustawiamy katalog roboczy kontenera
WORKDIR /app

# Kopiujemy pliki z bieżącego katalogu do katalogu roboczego kontenera
COPY App /app
COPY Data /app
COPY requirements.txt /app

# Instalujemy wymagane pakiety
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=600 -r requirements.txt

# Polecenie, które zostanie uruchomione podczas startu kontenera
CMD ["python", "run.py"]
