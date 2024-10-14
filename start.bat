@echo off
echo Installing requirements...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install requirements. Exiting...
    exit /b %errorlevel%
)
echo Running main.py...
python main.py
if %errorlevel% neq 0 (
    echo main.py exited with an error. Exiting...
    exit /b %errorlevel%
)
echo Done!
pause

