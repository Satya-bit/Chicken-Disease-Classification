import os
from pathlib import Path 
import logging
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:') #Logformat for debugging purpose

project_name="cnnClassifier"

list_of_files=[
    ".github/workflows/.gitkeep",        #To write CI/CD files. Also gitkeep file is created because whenever there is a commit there should be something present in the folder
    f"src/{project_name}/__init__.py",   #This is a constructor file which is used to import files in the app.py for eg to import model.py in app.py
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "reserach/trials.ipynb",
    "templates/index.html"





]

for filepath in list_of_files:
    filepath=Path(filepath)   #To handle the path issue like windows use backward slash but here forward slash is given
    filedir, filename=os.path.split(filepath) #To split the folder and file name


    if filedir !="":
        os.makedirs(filedir, exist_ok=True) # If the directory is already there it wont be created again as exist_ok is true
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): #To create file. If the file is not present in the directory or the file is empty then it will create that file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")

