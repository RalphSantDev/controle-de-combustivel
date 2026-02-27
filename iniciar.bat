@echo off
cd /d "%~dp0"
echo === Iniciando sistema (Flask) ===

call venv\Scripts\activate

start "" http://127.0.0.1:5000

echo === Python usado: ===
python --version
echo.

echo === Rodando app.py ===
python app.py

echo.
echo === O processo terminou. Se apareceu erro acima, copie e me envie. ===
pause
