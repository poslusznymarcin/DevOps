# Używamy lekkiego obrazu Pythona
FROM python:3.9-slim

# Ustawiamy folder roboczy w kontenerze
WORKDIR /app

# Kopiujemy Twój skrypt do kontenera
COPY serwis.py .

# Komenda startowa
CMD ["python", "serwis.py"]
