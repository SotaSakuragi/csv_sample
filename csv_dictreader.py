import csv

with open(
    "data/data.csv",
    encoding="shift-jis",
) as f:
    # 不要なコメント部分を読み込まないようにする
    next(f)
    next(f)
    next(f)

    # reader = csv.DictReader(f)  # ヘッダーから読み込み開始
    reader = csv.DictReader(f, fieldnames=["date", "temp"])
    # 方法①
    rows_data = []  # 全体のデータ配列の初期化
    for row in reader:  # 1行ずつをrowとして取得
        rows_data.append(row)  # 1行のデータ辞書を全体のデータ配列に追加

    # 方法②
    # rows_data = [row for row in reader]

    # print(rows_data)
    print(rows_data[50])
    print(rows_data[50]["date"])
    print(rows_data[50]["temp"])
