import os

def find_missing_files(folder_x, folder_y):
    files_x = set([file.split('.')[0] for file in os.listdir(folder_x)])
    files_y = set([file.split('.')[0] for file in os.listdir(folder_y)])
    
    missing_files = files_x - files_y
    
    print("Files missing in folder y:")
    for file in missing_files:
        print(file)

# 資料夾路徑
folder_labels = "/Users/dingxianglong/Desktop/vscode/yolov8/have_labels_birds/野鴿"
folder_images = "/Users/dingxianglong/Desktop/vscode/yolov8/have_labels_birds/野鴿/野鴿_labels"

find_missing_files(folder_labels, folder_images)
find_missing_files(folder_images,folder_labels)