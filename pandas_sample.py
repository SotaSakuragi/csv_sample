import pandas as pd

df = pd.read_csv(
    "data/data.csv",
    skiprows=3,  # 行を飛ばす
    # usecols=[0, 1],  # 列を配列で指定
    # delimiter=",",  # 区切り文字 デフォルトはカンマ
    dtype={"年月日": "str", "平均気温(℃)": "float"},  # 辞書で各データ型を指定できる 指定無しはstr or float
    parse_dates=["年月日"],  # 日付型のデータはここで指定する
    encoding="shift-jis",
)
# print(df)  # 全表示
# print(df["年月日"])  # 列を指定
# print(df[df["年月日"] == pd.to_datetime("2021-03-30")])  # 検索 複数の場合は条件毎に()で囲んで&,|でつなげる

# print(df[df["平均気温(℃)"] >= 27])

# start = pd.to_datetime("2021/3")
# end = pd.to_datetime("2021/4")
# print(df[(df["平均気温(℃)"] >= 10) & (start <= df["年月日"]) & (df["年月日"] < end)])


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius - 32) / 1.8
    return fahrenheit


df["華氏温度"] = df["平均気温(℃)"].apply(lambda celsius: celsius_to_fahrenheit(celsius))
print(df)

# print(df["平均気温(℃)"].apply(lambda celsius: celsius_to_fahrenheit(celsius)))

df.to_csv("data/special_data.csv")