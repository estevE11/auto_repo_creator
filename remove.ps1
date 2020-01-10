$user = Read-Host "Username"
$pass = Read-Host "Password" -AsSecureString
$name = Read-Host "Repo name"

cd R:\dev\python\ProjectInitializationAutomation

python remove.py $user $pass $name