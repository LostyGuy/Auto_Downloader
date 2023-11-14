import urllib.request
from tqdm import tqdm
import os
import subprocess

#genshin_url = "https://sg-public-api.hoyoverse.com/event/download_porter/trace/ys_global/genshinimpactpc/default?url=https%3A%2F%2Fact.hoyoverse.com%2Fpuzzle%2Fhk4e%2Fpz_wY19_dy4do%2Findex.html%3Fpz_plat%3Dpc%26lang%3Den-us%26game_biz%3Dhk4e_global%26bridge_name%3Dpz_wY19_dy4do"
#file_name = "Genshin_Impact_x64.exe"
# non .exe URL - BIG problem

obs_url = "https://cdn-fastly.obsproject.com/downloads/OBS-Studio-29.1.3-Full-Installer-x64.exe"
obs_filename = "OBS_Studio_x64.exe"
OBS = {'url' : obs_url,'filename' : obs_filename}

notepad_url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.8/npp.8.5.8.Installer.x64.exe"
notepad_filename = "NotePad++_x64.exe"
NOTEPAD = {'url' : notepad_url,'filename' :  notepad_filename}

steam_url = "https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe"
steam_filename = "Steam_x64.exe"
STEAM = {'url' : steam_url,'filename' :  steam_filename}

#get User-Agent automatically
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0'
}

g_input = {}

win_login = os.getlogin()

def menu():

    print("options 1 - OBS,2 - NOTEPAD,3 - STEAM")
    i = int(input("choose your Pokemon! "))
    if i == 1:
        g_input.update(OBS)
    elif i == 2:
        g_input.update(NOTEPAD)
    elif i == 3:
        g_input.update(STEAM)



def request_file():

    #assigning static values for requests
    URL = g_input.get('url')
    Filename = g_input.get('filename')

    #sends request
    request = urllib.request.Request(URL, headers=headers)

    #downloads file from request
    #urllib.request.urlretrieve(request.full_url, Filename)
    with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, dynamic_ncols=True) as t:
        with urllib.request.urlopen(request) as response:
            with open(Filename, 'wb') as file:
                total_size = int(response.info().get('Content-Length',0))
                t.total = total_size
                while True:
                    chunk = response.read(1024)
                    if not chunk:
                        break
                    file.write(chunk)
                    t.update(len(chunk))
                    
                    if t.n == total_size:
                        global download_comp
                        download_comp = 1

def folder_opening():
    if download_comp == 1:
        os.system(f"copy {g_input.get('filename')} C:\Users\{win_login}\Downloads")
        
        



menu()
#then
request_file()
print(download_comp)
