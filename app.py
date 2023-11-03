import requests

genshin_url = "https://sg-public-api.hoyoverse.com/event/download_porter/trace/ys_global/genshinimpactpc/default?url=https%3A%2F%2Fact.hoyoverse.com%2Fpuzzle%2Fhk4e%2Fpz_wY19_dy4do%2Findex.html%3Fpz_plat%3Dpc%26lang%3Den-us%26game_biz%3Dhk4e_global%26bridge_name%3Dpz_wY19_dy4do"
file_name = "Genshin_Impact_x64.exe"

headers = {'User-Agent': 'Your Custom User-Agent String'}

response = requests.get(genshin_url, headers=headers)

if response.status_code == 200:
    with open(file_name, 'wb') as file:
        file.write(response.content)
    print(f"File downloaded and saved as {file_name}")
else:
    print(f"Failed to download the file. Status code: {response.status_code}")
