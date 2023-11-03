import urllib.request

#genshin_url = "https://sg-public-api.hoyoverse.com/event/download_porter/trace/ys_global/genshinimpactpc/default?url=https%3A%2F%2Fact.hoyoverse.com%2Fpuzzle%2Fhk4e%2Fpz_wY19_dy4do%2Findex.html%3Fpz_plat%3Dpc%26lang%3Den-us%26game_biz%3Dhk4e_global%26bridge_name%3Dpz_wY19_dy4do"
#file_name = "Genshin_Impact_x64.exe"
# non .exe URL - BIG problem

obs_url = "https://cdn-fastly.obsproject.com/downloads/OBS-Studio-29.1.3-Full-Installer-x64.exe"
obs_filename = "OBS_Studio_x64"
OBS = {'url' : obs_url,'filename' : obs_filename}

notepad_url = "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.5.8/npp.8.5.8.Installer.x64.exe"
notepad_filename = "NotePad++_x64"
NOTEPAD = {'url' : notepad_url,'filename' :  notepad_filename}

CppDEV_url = "https://downloads.sourceforge.net/project/dev-cpp/Binaries/Dev-C%2B%2B%204.9.9.2/devcpp-4.9.9.2_setup.exe?ts=gAAAAABlRSjXezyGj2HfunrUQ2Lc-9-7g0vs7RCd41BglxwijThpbLU6W33t58YXRZBSeSLFHPGm_MTC5qkzY3HaIrBEBS4iOQ%3D%3D&r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Fdev-cpp%2Ffiles%2FBinaries%2FDev-C%252B%252B%25204.9.9.2%2Fdevcpp-4.9.9.2_setup.exe%2Fdownload"
CppDEV_filename = "C++DEV_x64"
CppDEV = {'url' : CppDEV_url,'filename' :  CppDEV_filename}

#get User-Agent automatically
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0'
}

g_input = {}

def menu():

    print("options 1 - OBS,2 - NOTEPAD,3 - C++DEV")
    i = int(input("choose your Pokemon!"))
    if i == 1:
        g_input.update(OBS)
    elif i == 2:
        g_input.update(NOTEPAD)
    elif i == 3:
        g_input.update(CppDEV)
    print(g_input)



def request_file():

    #assigning static values for requests
    URL = g_input('url')
    Filename = g_input('filename')

    #sends request
    request = urllib.request.Request(URL, headers=headers)

    #downloads file from request
    urllib.request.urlretrieve(request.full_url, Filename)


#request_file()
menu()