@echo off
SET VENV_PATH=venv

REM Check if virtual environment exists
IF NOT EXIST "%VENV_PATH%\Scripts\activate.bat" (
    echo [*] Creating virtual environment...
    python -m venv %VENV_PATH%
    
    echo [*] Activating virtual environment...
    call %VENV_PATH%\Scripts\activate

    echo [*] Installing requirements...
    pip install -r requirements.txt
) ELSE (
    echo [*] Virtual environment found.
    call %VENV_PATH%\Scripts\activate
)

echo [*] Starting FastAPI server...
uvicorn main:app --host 0.0.0.0 --port 8088

pause