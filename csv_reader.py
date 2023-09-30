import csv

with open("data/data.csv", encoding="shift-jis") as f:
    # 不要なコメント部分を読み込まないようにする
    next(f)
    next(f)
    next(f)

    reader = csv.reader(f)  # ヘッダーから読み込み開始

    # 方法①
    rows_data = []  # 全体のデータ配列の初期化
    for row in reader:  # 1行ずつをrowとして取得
        rows_data.append(row)  # 1行のデータ配列を全体のデータ配列に追加

    # 方法②
    # リスト内包表記でもOK
    # rows_data = [[data for data in row] for row in reader]

    print(rows_data[2][0])
    # print(rows_data)  # 全体を取得
    # print(row[0])
