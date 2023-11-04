import os
import subprocess

def file_check():
    check_tqdm = "pip show tqdm"
    check_requests = "pip show requests"

    out_tqdm = os.system(f'powershell.exe -Command "{check_tqdm}"')
    print(os.system("powershell.exe -Command pip show me"))
    should_tqdm = ""

file_check()