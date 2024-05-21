import os

def get_folder_names(path):
    folder_names = []
    for entry in os.scandir(path):
        if entry.is_dir():
            folder_names.append(entry.name)
    return folder_names

# 輸入指定路徑
path = '/Users/dingxianglong/Desktop/vscode/taiwan_birds'

# 取得資料夾名稱
folder_names = get_folder_names(path)

# 輸出結果
print("資料夾名稱:")
for folder_name in folder_names:
    print(folder_name)
