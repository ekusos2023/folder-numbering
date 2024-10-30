#folder numbering
import os

def rename_files(folder_path):
    # フォルダ内のファイル一覧を取得
    files = os.listdir(folder_path)
    # 0から始まるカウンターを初期化
    counter = 0
    for file_name in files:
        # ファイル名のパスを作成
        old_path = os.path.join(folder_path, file_name)
        # 新しいファイル名を作成
        new_name = str(counter) + os.path.splitext(file_name)[1]
        new_path = os.path.join(folder_path, new_name)
        # ファイル名を変更
        os.rename(old_path, new_path)
        # カウンターを増やす
        counter += 1
        # 最後のファイルの名前が変更されたら処理を停止
        if counter >= len(files):
            break

# フォルダのパスを指定してファイル名を変更
folder_path = "C:/Users/GTUNE/Desktop/"
rename_files(folder_path)
