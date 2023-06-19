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

def get_proxies():
    response = requests.get('https://proxy.sodalab.dev/random')
    proxy = response.text.strip()
    proxies_def = {
        "http://": f"http://{proxy}",
        'https//': f'https://{proxy}',
    }
    return proxies_def

# Sử dụng hàm để đọc dữ liệu từ cột "text"
filepath = 'F:\Downloads\B19DCCN630-BTTH2\oasst1-train.csv'  # Thay đổi đường dẫn đến file CSV của bạn
column_name = 'text'  # Thay đổi tên cột của bạn

texts = read_csv_column(filepath, 'text')
# print(typePLOAK(texts))
list_after_tran = []

# print(len(texts[0:1000]))
str_token = ""
for first_cell in texts[0:1000]:
    first_cell.replace("*", " ")
    if len(str_token) + len(first_cell) < 5000:
        str_token = str_token + " * " + first_cell
        continue
    else:
        if len(str_token) != 0:
            list_after_tran.append(str_token)

            # try:
            doc = GoogleTranslator(source='auto', target='vi').translate(str_token)
            time.sleep(3)
            # except:
            #     time.sleep(10)
            #     doc = GoogleTranslator(source='auto', target='vi').translate(str_token)

            str_token = ""

            print(doc)

# for i in list_after_tran:
#     print(len(i))
# print(len(list_after_tran))

