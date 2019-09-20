@echo off
echo deprecated. The swagger.yaml in the root directory should be used.
pause
rem cd ./work
rem del *.yaml
rem cd ..
rem 
rem cd ../paths
rem type *.* > ..\tools\work\paths.yaml
rem cd ../components/schemas
rem type *.* > ..\..\tools\work\schemas.yaml
rem cd ..
rem type *.* > ..\tools\work\components.yaml
rem cd ..\tools\work\
rem 
rem type ..\..\header ..\start.yaml paths.yaml ..\componentsStart.yaml schemas.yaml > swagger.yaml
rem copy swagger.yaml ..
rem cd ..