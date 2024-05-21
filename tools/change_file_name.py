import os
def rename_files(directory):
    for filename in os.listdir(directory):
        if '(' in filename and ')' in filename:
            new_filename = filename.replace('(', '').replace(')', '').replace(' ', '')  # 移除空格
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed '{filename}' to '{new_filename}'")

def remove_spaces(directory):
    for filename in os.listdir(directory):
        if ' ' in filename:
            new_filename = filename.replace(' ', '')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed '{filename}' to '{new_filename}'")

# 指定要處理的目錄
target_directory = '/Users/dingxianglong/Desktop/vscode/yolov8/have_labels_birds/野鴿'

# 呼叫函式進行檔案改名
# rename_files(target_directory)
# 呼叫函式進行去除空格
remove_spaces(target_directory)

