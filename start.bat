@echo off
chcp 65001 >nul
title Computer Monitor Bot
echo ========================================
echo    Запуск Computer Monitor Bot
echo ========================================

REM Переходим в директорию скрипта
cd /d "%~dp0"

REM Активируем виртуальное окружение (если есть)
if exist "venv\Scripts\activate.bat" (
    echo [INFO] Активация виртуального окружения...
    call venv\Scripts\activate.bat
) else (
    echo [INFO] Виртуальное окружение не найдено, используем системный Python
)

REM Проверяем наличие Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python не установлен или не добавлен в PATH
    pause
    exit /b 1
)

REM Проверяем наличие зависимостей
echo [INFO] Проверка зависимостей...
pip install -r requirements.txt


REM Запускаем бота
echo [INFO] Запуск бота...
echo [INFO] Бот запущен. Закройте это окно для остановки.
python main.py

REM Если скрипт завершился, ждем нажатия
echo.
echo [INFO] Бот завершил работу
pause