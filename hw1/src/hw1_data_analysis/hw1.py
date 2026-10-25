from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# Find the CSV beside this script, or directly inside src/.
script_dir = Path(__file__).resolve().parent
data_path = script_dir / "bicycle_data.csv"
if not data_path.exists():
    data_path = script_dir.parent / "bicycle_data.csv"

# 1. Read the data.
df = pd.read_csv(data_path)

# 2. Date contains hourly timestamps and should be datetime.
# The original Total, West, and East columns contain bicycle counts.
# Counts should be integers; nullable Int64 also allows missing values.
df["Date"] = pd.to_datetime(
    df["Date"], format="%m/%d/%Y %I:%M:%S %p"
)
count_columns = df.columns[1:]
df[count_columns] = df[count_columns].astype("Int64")

# 3. Add East + West total, hour of day, and year.
west_col = "Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"
east_col = "Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"

df["Total"] = df[west_col] + df[east_col]
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

# 4. Keep only 2016 records.
df_2016 = df.loc[df["Year"] == 2016].copy()

# 5. In the downloaded data, 2016 has 1 time point with missing counts:
# 2016-03-13 02:00. Exclude this row instead of treating missing counts as zero.
missing_points = df_2016["Total"].isna().sum()
clean_2016 = df_2016.dropna(subset=["Date", "Total"]).copy()

print("Rows in 2016:", len(df_2016))
print("Time points with missing counts:", missing_points)
print("Rows used for analysis:", len(clean_2016))

# 6. Average the East + West count across valid days for each hour.
hourly_mean = clean_2016.groupby("Hour")["Total"].mean()

ax = hourly_mean.plot(kind="line", marker="o", figsize=(10, 4))
ax.set_title("Fremont Bridge: Average Bicycle Counts by Hour (2016)")
ax.set_xlabel("Hour of day")
ax.set_ylabel("Average daily bicycle count (East + West)")
ax.set_xticks(range(24))
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = script_dir.parent.parent / "counts_by_hour.png"
plt.savefig(plot_path, dpi=150)
plt.close()

# 7. The busiest hour in 2016 is 17:00 (5 PM), averaging about 399.03 bicycles.
busiest_hour = hourly_mean.idxmax()
busiest_mean = hourly_mean.max()

print(f"Busiest hour: {busiest_hour:02d}:00")
print(f"Mean bicycle count: {busiest_mean:.2f}")
print("Saved plot:", plot_path)
