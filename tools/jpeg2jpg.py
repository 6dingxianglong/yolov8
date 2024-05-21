import os

def convert_jpeg_to_jpg(folder_path):
    # 获取文件夹中的所有文件
    files = os.listdir(folder_path)
    
    for file in files:
        # 检查文件扩展名是否为 .jpeg
        if file.lower().endswith('.jpeg'):
            # 构建新文件名
            new_file_name = os.path.splitext(file)[0] + '.jpg'
            # 重命名文件
            os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_file_name))

# 指定要转换文件扩展名的文件夹路径
folder_path = '/Users/dingxianglong/Desktop/vscode/have_labels_birds/turtle'

# 调用函数进行文件扩展名转换
convert_jpeg_to_jpg(folder_path)
