rm blackduck-cli.zip
rm -r blackduck/

cd ../solidfire-api-descriptors
powershell ./GenerateDownstreamLocal.ps1 cli
cd -

mkdir -p blackduck/srclib

cd blackduck/srclib


cp ../../setup.cfg .
cp ../../setup.py .
cp ../../README.md .
cp ../../logging.cfg .
cp ../../LICENSE .

cp -r ../../element .

cd ../../

zip -r blackduck-cli.zip blackduck/	