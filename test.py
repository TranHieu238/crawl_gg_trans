import time
import requests
from datasets import load_dataset
import json
import concurrent.futures
import numpy as np


def translate_and_save(subset, id_json):
    #mảng lưu dữ liệu sau dịch
    data_j = []
    #Số lượng document trong 1 file json
    len_of_json = 25
    check_id = 0
    id_file = 0
    for id_test, first_cell in enumerate(subset, start=1):
        # Khởi tạo dict lưu kết quả trước và sau khi dịch
        dict_data = {}
        # Đầu vào để dịch
        dict_data['input'] = first_cell
        # Xóa ký tự lạ
        first_cell = first_cell.replace("#", "").replace("\n", "").replace("&", "")
        # Gọi API trans
        url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=vi&q=" + first_cell
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
        }

        try:
            # Kết quả trả về từ API
            request_result = requests.get(url, headers=headers).json()
            time.sleep(0.5)
            # Lưu kết quả sau khi dịch
            dict_data['output'] = request_result[0][0]
            # print(request_result[0][0])
            data_j.append(dict_data)
        except:
            pass
        #kiểm tra xem đã đủ số lượng document để lưu vào file hay chưa
        if id_test % len_of_json == 0:
            # Ghi ra file json
            file_name = f'data_trans_{int(id_json)}_{id_file}.json'
            with open(file_name, 'w', encoding='utf-8') as file:
                json.dump(data_j, file, ensure_ascii=False)
            # khởi tạo lại mảng mới để lưu K document tiếp theo
            data_j = []
            id_file += 1
        check_id += 1
    print(check_id)

def main():
    data = load_dataset("timdettmers/openassistant-guanaco")
    dataset = data['train']['text']

    num_threads = 4  # Số lượng luồng
    subsets = np.array_split(dataset[0:100], num_threads)  # Chia dataset thành các subset

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Chạy các luồng độc lập
        executor.map(translate_and_save, subsets, range(1, num_threads + 1))


if __name__ == '__main__':
    main()