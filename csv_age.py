# import csv
import pandas as pd

# with open(
#     "data/employees.csv",
#     encoding="utf-8",
# ) as f:
#     reader = csv.DictReader(f)
#     rows_data = [row for row in reader]

df = pd.read_csv("data/employees.csv", encoding="utf-8", parse_dates=["生年月日"])

today = int(pd.to_datetime("today").strftime("%Y%m%d"))
date = df["生年月日"][0]
birthday = int(date.strftime("%Y%m%d"))
# print(today)
# print(birthday)

result = ((today - birthday) // 10000)
print(result)
