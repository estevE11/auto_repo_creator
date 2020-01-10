$name = Read-Host "Repo name"
$type = Read-Host "Repo type"
$pass = Read-Host "Pass: "

cd R:\dev\python\ProjectInitializationAutomation

python create.py $name $type $pass