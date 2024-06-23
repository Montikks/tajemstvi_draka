# Tajemství Dračího Království

Tajemství Dračího Království je textová dobrodružná hra založená na příběhu, kde hráči mohou komunikovat s různými NPC, plnit úkoly, bojovat a nakupovat předměty.

## Instalace a Spuštění

1. Klonujte tento repozitář:
   ```sh
   git clone https://github.com/Montikks/tajemstvi_draka.git
   cd tajemstvi_draka

   python -m venv .venv
   .venv\Scripts\activate   # Pro Windows
   source .venv/bin/activate  # Pro Linux/MacOS


   pip install -r requirements.txt
   
   python initialize_db.py

   set FLASK_ENV=development   # Pro Windows
   export FLASK_ENV=development  # Pro Linux/MacOS
   python app.py

## Funkce
  
   Inventář: Zobrazuje hráčovy předměty.
   Úkoly: Zobrazuje úkoly, které hráč může plnit.
   Dovednosti a kouzla: Zobrazuje dovednosti a kouzla, které hráč může použít.
   Akce: Umožňuje hráči komunikovat s NPC, trénovat a bojovat.
   
## Přispívání
Máte-li zájem přispět, otevřete prosím issue nebo pull request. Vaše příspěvky jsou vítány!

## Licence
Tento projekt je licencován pod MIT licencí.


