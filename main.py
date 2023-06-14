from googletrans import Translator
import csv

translator = Translator()
dest = 'vi'
file_path = "D:\CMC project\crawl_gg_trans\input2.csv"  # Thay đổi đường dẫn tới file của bạn
list_trans = []
list_after_tran = []
with open(file_path, "r") as file:
    # Đọc nội dung của file
    csv_reader = csv.reader(file)

    # Lặp qua từng dòng trong file
    for row in csv_reader:
        print('--------------------')
        # Truy cập vào ô đầu tiên của mỗi dòng
        first_cell = row[0]
        print(first_cell)
        list_trans.append(first_cell)
        if(str(first_cell) != None):
            trans = None
            while trans is None :
                try:
                    trans = translator.translate(first_cell,dest)
                    print(f'----->{trans.text}')
                    list_after_tran.append(trans.text)
                except:
                    pass
print(len(list_trans))
print(len(list_after_tran))



