$name = Read-Host "Repo name"
$type = Read-Host "Repo type"

cd R:\dev\python\ProjectInitializationAutomation

python create.py $name $type