from __future__ import print_function
import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('keywords', help="specify file that includes keywords to be searched.")
    # 第1引数でキーワードファイルを指定する
    parser.add_argument('targetfile', help='specify target file')

    args = parser.parse_args() # 引数をパースする

    # キーワード読み込み
    try:
        keyword = open(args.keywords) # キーワードファイルをオープンする
        keyword_lines = keyword.readlines() # キーワードファイルを読み込む
        keyword.close() # キーワードファイルをクローズする
    except:
        print("\"%s\" not found. Please specify correct search words file." % args.inwords, file=sys.stderr)
        # キーワードファイルがない場合の処理
        sys.exit()

    # ターゲット読み込み
    try:
        target = open(args.targetfile)
        target_lines_init = target.readlines()
        target.close()
    except:
        print("\"%s\" not found. Please specify correct target file." % args.targetfile, file=sys.stderr)
        sys.exit()

    for keyword in keyword_lines:
        keyword_flag = 0                    # キーワードが見つかったフラグ
        i = 1                               # 行番号の初期化
        keyword = keyword.replace('\n', '') # キーワードのNLコード削除
        keyword = keyword.replace('\r', '') # キーワードのCRコード削除
        if(len(keyword) == 0):              # キーワード長が0だったら
            continue

        for target in target_lines_init:
            if keyword in target:

                target = target.replace('\n', '')
                target = target.replace('\r', '')
                if(keyword_flag == 0): # キーワードが見つかったフラグが立っていない場合

                    print("Search word: %s" %  keyword) # キーワード表示
                    keyword_flag = 1                    # フラグを立てる
                print("%d: %s" % (i, target))           # 検索対象行　行と検索対象行を出力
            i = i + 1

if __name__ == '__main__':
    main()
