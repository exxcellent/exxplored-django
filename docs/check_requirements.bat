@echo off

REM Check if Python 3.11.4 is installed
where python > nul 2>&1
if %errorlevel% neq 0 (
    echo Python 3.11.4 is not installed.
) else (
    python --version | findstr /C:"Python 3.11.4" > nul
    if %errorlevel% neq 0 (
        echo Python 3.11.4 is not installed.
    ) else (
        echo Python 3.11.4 is installed.
    )
)

REM Check if Poetry 1.5.1 is installed
where poetry > nul 2>&1
if %errorlevel% neq 0 (
    echo Poetry 1.5.1 is not installed.
) else (
    poetry --version | findstr /C:"Poetry version 1.5.1" > nul
    if %errorlevel% neq 0 (
        echo Poetry 1.5.1 is not installed.
    ) else (
        echo Poetry 1.5.1 is installed.
    )
)

pause
