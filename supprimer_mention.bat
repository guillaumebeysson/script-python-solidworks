@echo off
setlocal

:: Vérifie si Python est installé
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Erreur : Python n'est pas installé.
    pause
    exit /b
)

:: Exécute le script Python
python supprimer_mention.py
pause
