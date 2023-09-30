import pandas as pd

df = pd.read_csv("data/employees.csv", encoding="utf-8", parse_dates=["生年月日"])


def getAge(birthday):
    """日付から現在の年齢を返す関数"""
    today = int(pd.to_datetime("today").strftime("%Y%m%d"))
    birthday = int(birthday.strftime("%Y%m%d"))
    return int((today - birthday) / 10000)


# 生年月日を使って年齢を算出(処理であることを明確にするために無名関数にする)
df["年齢"] = df["生年月日"].apply(lambda date: getAge(date))
df["バリウム検査"] = (df["年齢"] == 30) | (df["年齢"] >= 35)


# 関数をそのまま渡しても同じだが、関数であることが分かりづらい
# df["年齢"] = df["生年月日"].apply(getAge)

todaystr = pd.to_datetime("today").strftime("%Y%m%d")
df.to_csv(f"data/{todaystr}.csv")

