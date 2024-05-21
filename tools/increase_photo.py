import os
from PIL import Image

def rotate_images_in_folder(input_folder, output_folder, degrees, added_string):
    # 檢查輸入的資料夾是否存在
    if not os.path.isdir(input_folder):
        print(f"輸入資料夾 '{input_folder}' 不存在。")
        return

    # 檢查輸出的資料夾是否存在，如果不存在則創建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 取得輸入資料夾中的所有檔案
    file_list = os.listdir(input_folder)
    
    # 遍歷輸入資料夾中的每個檔案
    for file_name in file_list:
        input_file_path = os.path.join(input_folder, file_name)
        # 檢查檔案是否為圖片
        if os.path.isfile(input_file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                # 打開圖片
                img = Image.open(input_file_path)
                # 旋轉圖片
                rotated_img = img.rotate(degrees, expand=True)
                # 組合輸出檔案路徑
                output_file_name = os.path.splitext(file_name)[0] + added_string + os.path.splitext(file_name)[1]
                output_file_path = os.path.join(output_folder, output_file_name)
                # 保存旋轉後的圖片到輸出資料夾中
                rotated_img.save(output_file_path)
                print(f"已旋轉圖片 '{file_name}' {degrees} 度，保存為 '{output_file_name}'")
            except Exception as e:
                print(f"處理圖片 '{file_name}' 時出錯: {e}")

def resize_images_in_folder(input_folder, output_folder, scale, added_string):
    # 檢查輸入的資料夾是否存在
    if not os.path.isdir(input_folder):
        print(f"輸入資料夾 '{input_folder}' 不存在。")
        return

    # 檢查輸出的資料夾是否存在，如果不存在則創建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 取得輸入資料夾中的所有檔案
    file_list = os.listdir(input_folder)
    
    # 遍歷輸入資料夾中的每個檔案
    for file_name in file_list:
        input_file_path = os.path.join(input_folder, file_name)
        # 檢查檔案是否為圖片
        if os.path.isfile(input_file_path) and file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            try:
                # 打開圖片
                img = Image.open(input_file_path)
                # 縮放圖片
                resized_img = img.resize((int(img.width * scale), int(img.height * scale)), Image.LANCZOS)
                # 組合輸出檔案路徑
                output_file_name = os.path.splitext(file_name)[0] + added_string + os.path.splitext(file_name)[1]
                output_file_path = os.path.join(output_folder, output_file_name)
                # 保存縮放後的圖片到輸出資料夾中
                resized_img.save(output_file_path)
                print(f"已縮放圖片 '{file_name}' 為原大小的 {scale} 倍，保存為 '{output_file_name}'")
            except Exception as e:
                print(f"處理圖片 '{file_name}' 時出錯: {e}")

# 指定輸入和輸出資料夾路徑以及操作參數
input_folder = "/Users/dingxianglong/Desktop/vscode/yolov8/birds_封存/have_labels_birds/岩鷚"
output_folder = "/Users/dingxianglong/Desktop/vscode/yolov8/birds_封存/increase_birds"
rotation_degrees = -10
resize_scale = 0.8  # 50% 的縮放比例
added_string = "L"  # 新增的字串

# 旋轉圖片
# rotate_images_in_folder(input_folder, output_folder, rotation_degrees, added_string)

# 縮放圖片
resize_images_in_folder(input_folder, output_folder, resize_scale, added_string)
