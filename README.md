# Tajemství Dračího Království

Tajemství Dračího Království je webová hra inspirovaná Dračími Doupětem, vytvořená pomocí Flasku. Hráči mohou vytvářet postavy, prozkoumávat svět, bojovat s nepřáteli a interagovat s NPC.

## Požadavky

- Python 3.8+
- Flask
- Flask-SQLAlchemy

## Instalace

1. Klonujte repozitář:
   ```sh
   git clone https://github.com/Montikks/tajemstvi_drak.git
   cd tajemstvi_draka

## Spuštění aplikace

Vytvořte a aktivujte virtuální prostředí:
    
    python -m venv .venv
    source .venv/bin/activate # Na Windows použijte: .venv\Scripts\activate

Nainstalujte závislosti:

    pip install -r requirements.txt

Inicializujte databázi:

    python -c "from app import db, app; with app.app_context(): db.create_all()"

Spusťte aplikaci:

    python app.py


