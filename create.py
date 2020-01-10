import sys
import os
from github import Github

path = "R:/dev/"

username = "estevE11" #Insert your github username here
password = sys.argv[3]#open("pass.txt", "r").read() #Write your github password in the pass.txt file

def create():
    if len(sys.argv) < 2:
        print("You must enter the name of the repo and the type")
        return
    
    #Creating folder
    folderName = str(sys.argv[1])
    repo_type = parse_type(sys.argv[2])
    repo_path = path + repo_type + "/" + str(folderName)
    exists = False
    try:
        os.makedirs(repo_path)
    except:
        print("Dir exists! No problem brother!")
        exists = True
    
    #Loging into github and creating the repo
    user = Github(username, password).get_user()
    repo = user.create_repo(folderName)
    print("Succesfully created repository {}".format(folderName))

    #Making first commit and push
    os.chdir(repo_path)
    if not exists:
        open(repo_path + "/README.md", 'a').close()
        gignore_bp = open("R:\dev\python\ProjectInitializationAutomation/gitignores/" + repo_type + ".ig", "r").read()
        gignore = open(repo_path + "/.gitignore", 'w')
        gignore.write(gignore_bp)
        gignore.close()
        
    os.system("git init")
    os.system("git add .")
    os.system('git commit -m "Automatic first commit"')
    os.system("git remote add origin https://github.com/estevE11/" + folderName + ".git")
    os.system("git push -u origin master")
    print("First commit pushed")
    print("Opening VSCode")
    os.system("code .")

def parse_type(inp):
    if inp == "py":
        inp = "python"
    elif inp == "j":
        inp = "java"
    return inp

if __name__ == "__main__":
    create()
