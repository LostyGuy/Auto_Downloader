import os
import subprocess

complete_tqdm  = 0
complete_requests = 0
index = 0

def file_check():

    global index

    check_tqdm = "pip show tqdm"
    check_requests = "pip show requests"

    out_tqdm = subprocess.run(['powershell.exe', '-Command', check_tqdm], capture_output=True, text=True, check=True, shell = True).stdout
    out_requests = subprocess.run(['powershell.exe', '-Command', check_requests], capture_output=True, text=True, check=True, shell = True).stdout

    #print(os.system("powershell.exe -Command pip show me"))

    should_tqdm = "WARNING: Package(s) not found: tqdm"
    should_requests = "WARNING: Package(s) not found: requests"

    #print(out_tqdm, out_requests)

    if out_tqdm.strip() == should_tqdm:
        os.system("powershell.exe -Command pip install tqdm")
    else:
        complete_tqdm = 1
    
    if out_requests.strip() in should_requests:
        os.system("powershell.exe - Command pip install requests")
    else:
        complete_requests = 1
        
    if complete_requests and complete_tqdm:
         index = 1
         return True
    else:
        return False


file_name = "Auto_app.py"
file_check()

if index == 1:
    os.system(f"start {file_name}")
else:
    file_check()