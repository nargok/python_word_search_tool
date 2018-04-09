import os
import sys
from stat import *

file_name = sys.argv[1]                   # ファイル名を取得
fd = open(file_name)                      # ファイルをオープンする
file_status = os.stat(file_name)          # ファイルの状態を取得する
file_size = file_status[ST_SIZE]          # サイズを取得する
fd.seek(file_size)                        # ファイルポインタの位置をファイル最後尾に設定する

while 1:                                  # 無限ループ
    lines = fd.readlines()
    if lines:
        for line in lines:
            line = line.replace('\n', '') # 読み込んだ行のNLコード削除
            line = line.replace('\r', '') # 読み込んだ行のCRコード削除
            print(line)
