import os

def check_for_png_files(folder_path):
    # 遍历文件夹中的每个文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            # 检查文件是否以".png"结尾
            if filename.endswith('.png'):
                print(f"{file_path} 包含PNG文件")

# 输入文件夹路径
folder_path = "/Users/dingxianglong/Desktop/vscode/yolov8/have_labels_birds"

# 调用函数递归检查PNG文件
check_for_png_files(folder_path)