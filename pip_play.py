import os
import subprocess

complete_tqdm = 0
complete_requests = 0

def file_check():

    check_tqdm = "pip show tqdm"
    check_requests = "pip show requests"

    out_tqdm = os.popen(f'powershell.exe -Command "{check_tqdm}"')
    out_requests = os.popen(f'powershell.exe - Command "{check_requests}"')

    #print(os.system("powershell.exe -Command pip show me"))

    should_tqdm = "WARNING: Package(s) not found: tqdm"
    should_requests = "WARNING: Package(s) not found: requests"

    if out_tqdm == should_tqdm:
        os.popen("powershell.exe -Command pip install tqdm")
    else:
        complete_tqdm.update(1)
    
    if out_requests == should_requests:
        os.popen("powershell.exe - Command pip install requests")
    else:
        complete_requests.update(1)



file_check()

if complete_tqdm and complete_tqdm == 1:
    os.system("start Auto_app.py")
else:
    file_check()