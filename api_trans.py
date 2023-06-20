import time
import requests
from datasets import load_dataset
import json


data = load_dataset("timdettmers/openassistant-guanaco")
dataset = data['train']['text']

id_test = 0
data_j = []
for first_cell in dataset[0:1]:
    #khởi tạo dict lưu kết quả trước và sau khi dịch
    dict={}
    #đầu vào để dịch
    dict['input'] = first_cell
    #xóa ký tự lạ
    first_cell = first_cell.replace("#","").replace("\n", "").replace("&", "")
    #call api trans
    url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=vi&q=" + first_cell
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
    }

    try:
        id_test += 1
        #kết quả trả về từ api
        request_result = requests.get(url, headers=headers).json()
        time.sleep(0.5)
        #lưu kết quả sau khi dịch
        dict['output'] = request_result[0][0]
        data_j.append(dict)
    except:
        pass

#Ghi ra file json
with open('data.json', 'w',encoding='utf-8') as file:
    json.dump(data_j, file,ensure_ascii=False)

print(id_test)


