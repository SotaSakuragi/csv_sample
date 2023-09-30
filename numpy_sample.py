import numpy as np

csv_list = np.loadtxt(
    "data/data.csv",
    skiprows=4,  # 行を飛ばす
    usecols=[0, 1],  # 列を指定 1つの場合は数値で指定 1
    dtype="str",  # 数値と文字列が混在している場合は文字列str U(Unicodeのこと)でもOK
    delimiter=",",  # 区切り文字 デフォルトは空白文字
    encoding="shift-jis",
)
print(csv_list[0])
print(csv_list[0][0])
print(csv_list[0][1])
# 下記でも同様
print(csv_list[1])
print(csv_list[1, 0])
print(csv_list[1, 1])
