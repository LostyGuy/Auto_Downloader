import os
import subprocess

complete_tqdm  = 0
complete_requests = 0
index = 0

def file_check():

    global index

    check_tqdm = "tqdm"
    check_requests = "pip show requests"
    pip_install = "powershell.exe -Command pip install "    


    out_tqdm = subprocess.run(['pip', 'show', check_tqdm], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out_requests = subprocess.run(['pip', 'show', check_requests], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if out_tqdm.returncode == 1:
        os.system(pip_install + check_tqdm)
 
    if out_requests.returncode == 1:
        os.system(pip_install + check_requests)
   


command = "python Auto_app.py"
file_check()

os.system("cls")

print("Installing components completed...")
print("Running app...")

os.system(command)



