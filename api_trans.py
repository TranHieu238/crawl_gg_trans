import time
import requests
from datasets import load_dataset



data = load_dataset("timdettmers/openassistant-guanaco")
dataset = data['train']['text']

id_test = 0

for first_cell in dataset[0:100]:
    first_cell = first_cell.replace("#","").replace("\n", "").replace("&", "")

    url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=vi&q=" + first_cell
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }

    try:
        id_test += 1
        request_result = requests.get(url, headers=headers).json()
        time.sleep(0.5)
        print(request_result)
        print(
            '[In English]: ' + request_result['alternative_translations'][0]['alternative'][0]['word_postproc'])
        print('[Language Dectected]: ' + request_result['src'])
    except:
        pass
print(id_test)


