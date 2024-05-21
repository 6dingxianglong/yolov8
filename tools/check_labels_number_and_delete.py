import os

def find_missing_numbers(folder_path):
    # 获取文件夹中所有文件名中的数字
    numbers = set()
    for filename in os.listdir(folder_path):
        # 提取文件名中的数字部分
        file_number = ''.join(filter(str.isdigit, filename))
        if file_number:
            numbers.add(int(file_number))

    # 获取文件夹中的最小和最大数字
    min_number = min(numbers)
    max_number = max(numbers)

    # 查找缺失的数字
    missing_numbers = [num for num in range(min_number, max_number + 1) if num not in numbers]
    print(missing_numbers)
    return missing_numbers

def delete_files_with_numbers(folder_path, numbers_to_delete):
    # 遍历文件夹中的每个文件
    for filename in os.listdir(folder_path):
        # 提取文件名中的数字部分
        file_number = ''.join(filter(str.isdigit, filename))
        if file_number:
            file_number = int(file_number)
            # 如果文件名中的数字在要删除的列表中，则删除该文件
            if file_number in numbers_to_delete:
                file_path = os.path.join(folder_path, filename)
                try:
                    os.remove(file_path)
                    print(f"已删除文件: {filename}")
                except Exception as e:
                    print(f"删除文件失败: {filename}, {e}")

# 文件夹路径
folder_labels = "/Users/dingxianglong/Desktop/vscode/yolov8/have_labels_birds/野鴿/labels_野鴿"
folder_images = "/Users/dingxianglong/Desktop/vscode/yolov8/have_labels_birds/野鴿"

# 查找缺失的数字
missing_numbers = find_missing_numbers(folder_labels)

# 删除另一个文件夹中具有缺失数字的文件
delete_files_with_numbers(folder_images, missing_numbers)

