# Mój pierwszy projekt Python

To jest przykładowy projekt Python.

## Jak uruchomić

1. Zainstaluj wymagane narzędzia, jeśli jeszcze nie masz:
   - Debian/Ubuntu: `sudo apt update && sudo apt install -y python3-venv python3-pip`
2. Utwórz i aktywuj środowisko wirtualne w katalogu projektu:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
3. Zainstaluj zależności:
   - `pip install -r requirements.txt`
4. Uruchom aplikację:
   - `python app/main.py`

Alternatywnie można uruchomić skrypt setup:
- `bash scripts/setup.sh`

## Co robi projekt

Wyświetla w konsoli prosty tekst powitalny.

## www server run 

uvicorn <MODULE_PATH>:<APP_INSTANCE> --reload

example:
uvicorn app.api.books:app --reload


