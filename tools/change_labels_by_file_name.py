import os

def update_first_column(folder_path, n_value, target_name):
    # 遍历文件夹中的每个文件
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # 检查文件是否为.txt文件
        if filename.endswith('.txt') and target_name in filename:
            try:
                # 读取文件内容
                with open(file_path, 'r') as file:
                    lines = file.readlines()
                
                # 更新每行的第一个元素为自定义的N值
                updated_lines = [f"{n_value} {line.split(' ', 1)[1]}" for line in lines]
                    
                # 写入更新后的内容
                with open(file_path, 'w') as file:
                    file.writelines(updated_lines)
                    
                print(f"已更新文件：{filename}")
            except Exception as e:
                print(f"更新失败：{filename}, {e}")
        else:
            print(f"跳过非符合条件的文件：{filename}")

# 输入文件夹路径
folder_path = "/Users/dingxianglong/Desktop/vscode/yolov8/labels/val"
# 自定义N值
n_value = "10"

# 指定要更改的文件名模式
target_name = "野鴿"  

# 调用函数更新文件
update_first_column(folder_path, n_value, target_name)
