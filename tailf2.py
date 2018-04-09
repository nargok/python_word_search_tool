from __future__ import print_function
import os
import sys
from stat import *

file_name = sys.argv[1]                   # ファイル名を取得
fd = open(file_name)                      # ファイルをオープンする
file_status = os.stat(file_name)          # ファイルの状態を取得する
file_size = file_status[ST_SIZE]          # サイズを取得する
fd.seek(file_size)                        # ファイルポインタの位置をファイル最後尾に設定する

# キーワード読み込み
keyword_file_name = sys.argv[2]
try:
    keyword = open(keyword_file_name)
    keyword_lines = keyword.readlines()
    keyword.close()
except:
    print("\"%s\" not found. Please specify correct search words file." % args.inwords, file=sys.stderr)
    # キーワードファイルがない場合の処理
    sys.exit()

while 1:                                            # 無限ループ
    lines = fd.readlines()
    if lines:
        for line in lines:
            line = line.replace('\n', '')           # 読み込んだ行のNLコード削除
            line = line.replace('\r', '')           # 読み込んだ行のCRコード削除
            for keyword in keyword_lines:
                keyword = keyword.replace('\n', '') # 読み込んだ行のNLコード削除
                keyword = keyword.replace('\r', '') # 読み込んだ行のCRコード削除
                if(len(keyword) == 0):              # キーワード長が0だったら
                    continue
                if keyword in line:                 # 行にキーワードがあるかどうか
                    print("%s" % line)              # 行を出力
