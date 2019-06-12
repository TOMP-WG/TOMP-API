
cd ./work
del *.yaml
cd ..

cd ../paths
type *.* > ..\tools\work\paths.yaml
cd ../components/schemas
type *.* > ..\..\tools\work\schemas.yaml
cd ..
type *.* > ..\tools\work\components.yaml
cd ..\tools\work\

type ..\..\header ..\start.yaml paths.yaml ..\componentsStart.yaml schemas.yaml > swagger.yaml
copy swagger.yaml ..
cd ..