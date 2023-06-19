from json import loads
from requests import get
import csv
import time
from deep_translator import GoogleTranslator
from googletrans import Translator
import requests


def read_csv_column(filepath, column_name):
    texts = []

    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            text = row[column_name]
            texts.append(text)

    return texts


# Sử dụng hàm để đọc dữ liệu từ cột "text"
filepath = 'F:\Downloads\B19DCCN630-BTTH2\oasst1-train.csv'  # Thay đổi đường dẫn đến file CSV của bạn
column_name = 'text'  # Thay đổi tên cột của bạn

texts = read_csv_column(filepath, 'text')

id_test = 0
for first_cell in texts[0:200]:
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


