import os
import subprocess

command = "python Auto_app.py"

def file_check():

    global index

    check_tqdm = "tqdm"
    check_requests = "requests"
    pip_install = "powershell.exe -Command pip install "    


    out_tqdm = subprocess.run(['pip', 'show', check_tqdm], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out_requests = subprocess.run(['pip', 'show', check_requests], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if out_tqdm.returncode == 1:
        os.system(pip_install + check_tqdm)
 
    if out_requests.returncode == 1:
        os.system(pip_install + check_requests)
   

file_check()
os.system('cls')

print("components completed...")
print("Running app...")

#run Auto_app.py
os.system(command)



