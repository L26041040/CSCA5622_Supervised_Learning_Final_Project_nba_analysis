import pandas as pd

# 讀入整理好的 10 年資料
df = pd.read_csv("NBA_Stats_Standings_2015_2016_to_2024_2025.csv")

# 確認有讀成功
print("Shape:", df.shape)
print(df[["Season", "Team", "W", "L", "Conference"]].head(10))
