@echo off
setlocal enabledelayedexpansion

REM Usage: filters.bat filter_file.txt [input.yaml] [output.yaml]

if "%~1"=="" (
  echo Usage: %~nx0 ^<filters-file^> [input.yaml] [output.yaml]
  exit /b 1
)

set "FILTERFILE=%~1"
set "INPUT=%~2"
set "OUTPUT=%~3"

if "%INPUT%"=="" set "INPUT=../../TOMP-API.yaml"
if "%OUTPUT%"=="" set "OUTPUT=TOMP-API-filtered.yaml"

set "PY=python"
set "SCRIPT=filter_openapi.py"

if not exist "%FILTERFILE%" (
  echo Filters file not found: "%FILTERFILE%"
  exit /b 1
)

REM Build argument list from lines in the filter file (skip empty lines and comments)
set "ARGS="
for /f "usebackq delims=" %%L in ("%FILTERFILE%") do (
  set "LINE=%%~L"
  if not "!LINE!"=="" if "!LINE:~0,1!" NEQ "#" (
    set "ARGS=!ARGS! "%%~L""
  )
)

echo Running: %PY% "%SCRIPT%" -i "%INPUT%" -o "%OUTPUT%" --preselect %ARGS%
%PY% "%SCRIPT%" -i "%INPUT%" -o "%OUTPUT%" --preselect %ARGS%
if errorlevel 1 (
  echo Failed to filter OpenAPI.
  exit /b 1
)

echo Done. Output: "%OUTPUT%"
endlocal