import os
import shutil

def move_folders_by_name(src_dir, strings_to_match, dest_dirs):
    # 确保目标文件夹存在，如果不存在则创建
    for dest_dir in dest_dirs:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

    # 遍历源文件夹中的子文件夹
    for folder_name in os.listdir(src_dir):
        folder_path = os.path.join(src_dir, folder_name)
        if os.path.isdir(folder_path):
            # 检查子文件夹名称是否包含任何指定的字符串
            for i, strings in enumerate(strings_to_match):
                for string in strings:
                    if string in folder_name:
                        shutil.move(folder_path, dest_dirs[i])
                        print(f"移动文件夹 '{folder_name}' 到目标文件夹 {i+1}")
                        break
                else:
                    continue
                break
            else:
                print(f"文件夹 '{folder_name}' 不符合任何指定的字符串，未移动")

# 设置源文件夹路径和目标文件夹路径
src_directory = "/Users/dingxianglong/Desktop/vscode/taiwan_birds"
dest_directories = ["/Users/dingxianglong/Desktop/vscode/rank1", 
                    "/Users/dingxianglong/Desktop/vscode/rank2",
                    "/Users/dingxianglong/Desktop/vscode/rank3"]

# 指定要匹配的字符串列表
strings_to_match = [
    ["赫氏角鷹", "草鴞","山麻雀","黑面琵鷺",
     "遺鷗","黑嘴端鳳頭燕鷗","白腹軍艦鳥","粉嘴鰹鳥",
     "卷羽鵜鶘","短尾信天翁","黑腳信天翁","洪氏環企鵝"],

    ["黃鸝","林鵰","鴛鴦","花臉鴨","水雉","雉尾水雉",
     "彩鷸","唐白鷺","黑頭白鹮","小剪尾","日本松雀鷹",
     "北雀鷹","赤腹鷹","鳳頭蒼鷹","松雀鷹","雀鷹","灰面鵟鷹","灰面鷲鵟",
     "灰澤鵟","灰鷂","花澤鵟","鵲鷂","澤鵟","東方澤鵟","東方澤鷂",
     "黑翅鳶","黑鳶","魚鷹","東方蜂鷹","蜂鷹","雕頭鷹","大冠鷲",
     "燕隼","紅隼","遊隼","隼","短耳鴞","長耳鴞","鵂鶹","黃魚鴞",
     "褐鷹鴞","領角鴞","蘭嶼角鴞,","優雅角鴞","黃嘴角鴞","東方角鴞",
     "灰林鴞","褐林鴞","藍胸鶉","藍腹鷴","環頸雉","黑長尾雉","帝雉",
     "花翅山椒鳥","野鵐","繡眼鵐","紫壽帶","綬帶鳥","朱鸝","黃山雀",
     "赤腹山雀","仙八色鶇","八色鳥","烏頭翁","八哥","白喉噪眉","白喉笑鶇",
     "棕噪眉","竹鳥","臺灣畫眉","白頭鶇","大赤啄木","綠啄木","琵嘴鷸",
     "青頭潛鴨","金鵐","紅頭綠鳩","玄燕鷗","白眉燕鷗","黑嘴鷗","紅燕鷗",
     "粉紅燕鷗","蒼燕鷗","小燕鷗","鳳頭燕鷗","班嘴環企鵝" ],

    ["燕鴴","半蹼鷸","白腰杓鷸","大杓鷸","麻鷺","鉛色水鶇","臺灣山鷓鴣","深山竹雞",
     "臺灣藍鵲","紅尾伯勞","白眉林鴝","黃腹琉璃","煤山雀","綠背山雀","青背山雀",
     "臺灣戴菊","火冠戴菊鳥","飯島柳鶯","艾吉柳鶯","紋翼畫眉","白尾鴝",
     "林三趾鶉","臺灣朱雀","長尾鳩","紅腰杓鷸","栗背林鴝","黃胸藪眉","白耳畫眉"
     "黑頭文鳥","冠羽畫眉","岩鷚","董雞","黑尾鷸","大濱鷸","紅腹濱鷸"]
]

# 调用函数
move_folders_by_name(src_directory, strings_to_match, dest_directories)