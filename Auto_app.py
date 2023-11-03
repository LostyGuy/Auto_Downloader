import urllib.request

genshin_url = "https://sg-public-api.hoyoverse.com/event/download_porter/trace/ys_global/genshinimpactpc/default?url=https%3A%2F%2Fact.hoyoverse.com%2Fpuzzle%2Fhk4e%2Fpz_wY19_dy4do%2Findex.html%3Fpz_plat%3Dpc%26lang%3Den-us%26game_biz%3Dhk4e_global%26bridge_name%3Dpz_wY19_dy4do"
obs_url = "https://cdn-fastly.obsproject.com/downloads/OBS-Studio-29.1.3-Full-Installer-x64.exe"

def request_file():
    file_name = "Genshin_Impact_x64.exe"
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0'
    }

    # Use urllib.request.urlretrieve to download the file
    request = urllib.request.Request(genshin_url, file_name, headers=headers)

    urllib.request.urlretrieve(request.full_url, file_name)


request_file()

