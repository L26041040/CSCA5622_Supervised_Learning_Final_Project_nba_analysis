import pandas as pd

# 讀入整理好的 10 年資料
df = pd.read_csv("NBA_Stats_Standings_2015_2016_to_2024_2025.csv")

# 確認有讀成功
print("Shape:", df.shape)
print(df[["Season", "Team", "W", "L", "Conference"]].head(10))

three_pt = df[["Season", "Team", "3P", "3PA", "3P%"]].copy()
print(three_pt.head())

top_3pt = (
    df.groupby("Team")["3P%"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

print("10 年三分命中率前 10 名：")
print(top_3pt)

yearly_3pt = df.groupby("Season")["3P%"].mean()

print("每年聯盟平均 3P%：")
print(yearly_3pt)

df["WinRate"] = df["W"] / (df["W"] + df["L"])

avg_winrate = (
    df.groupby("Team")["WinRate"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

print("10 年平均勝率前 10 名：")
print(avg_winrate)

best_each_year = (
    df.loc[df.groupby("Season")["WinRate"].idxmax()][
        ["Season", "Team", "WinRate"]
    ]
)

print("每年勝率最高的球隊：")
print(best_each_year)

