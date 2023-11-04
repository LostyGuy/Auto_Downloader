import os
import subprocess

complete_tqdm  = 0
complete_requests = 0

def file_check():

    check_tqdm = "pip show tqdm"
    check_requests = "pip show requests"

    out_tqdm = subprocess.run(['powershell.exe', '-Command', check_tqdm], capture_output=True, text=True, check=True).stdout
    out_requests = subprocess.run(['powershell.exe', '-Command', check_requests], capture_output=True, text=True, check=True).stdout

    #print(os.system("powershell.exe -Command pip show me"))

    should_tqdm = "WARNING: Package(s) not found: tqdm"
    should_requests = "WARNING: Package(s) not found: requests"

    print(out_tqdm, out_requests)

    if out_tqdm.strip() == should_tqdm:
        os.system("powershell.exe -Command pip install tqdm")
    else:
        complete_tqdm = 1
    
    if out_requests.strip() == should_requests:
        os.system("powershell.exe - Command pip install requests")
    else:
        complete_requests = 1


file_check()

if (complete_tqdm and complete_requests == 1) or (complete_requests and complete_tqdm == 1):
    os.system("start Auto_app.py")
else:
    file_check()