import os
import shutil

def copy_files(source_folder, dest_folder_x, dest_folder_y, ratio=0.7):
    # 确保目标文件夹存在
    if not os.path.exists(dest_folder_x):
        os.makedirs(dest_folder_x)
    if not os.path.exists(dest_folder_y):
        os.makedirs(dest_folder_y)

    # 遍历源文件夹中的每个文件
    files = os.listdir(source_folder)
    total_files = len(files)
    num_files_to_copy_x = int(total_files * ratio)
    num_files_to_copy_y = total_files - num_files_to_copy_x

    count_x = 0
    count_y = 0
    for filename in files:
        source_file = os.path.join(source_folder, filename)
        # 确定文件应该被复制到哪个文件夹
        if count_x < num_files_to_copy_x:
            dest_file = os.path.join(dest_folder_x, filename)
            try:
                # 复制文件到目的地x
                shutil.copyfile(source_file, dest_file)
                print(f"已复制文件到目的地x: {filename}")
                count_x += 1
            except Exception as e:
                print(f"复制失败到目的地x: {filename}, {e}")
        else:
            dest_file = os.path.join(dest_folder_y, filename)
            try:
                # 复制文件到目的地y
                shutil.copyfile(source_file, dest_file)
                print(f"已复制文件到目的地y: {filename}")
                count_y += 1
            except Exception as e:
                print(f"复制失败到目的地y: {filename}, {e}")

        # 如果目的地x和目的地y的文件都已复制完成，则跳出循环
        if count_x >= num_files_to_copy_x and count_y >= num_files_to_copy_y:
            break

# 源文件夹和目标文件夹路径
source_folder = "/Users/dingxianglong/Desktop/vscode/have_labels_birds/岩鷚"
dest_folder = "/Users/dingxianglong/Desktop/vscode/train/images"
dest_folder_y = "/Users/dingxianglong/Desktop/vscode/val/images"


# 调用函数复制文件
copy_files(source_folder, dest_folder)