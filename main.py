"""Starter analysis for Financial Dashboard."""
from pathlib import Path
import pandas as pd

HERE = Path(__file__).resolve().parent
OUT = HERE / "output"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(HERE / "finance.csv")

print("\n=== Financial Dashboard ===")
print("\nDataset preview:\n", df.head().to_string(index=False))
print("\nMissing values:\n", df.isna().sum().to_string())

df["profit"] = df["revenue"] - df["expenses"]
df["budget_variance"] = df["expenses"] - df["budget"]
print("Total revenue:", df["revenue"].sum())
print("Total expenses:", df["expenses"].sum())
print("Total profit:", df["profit"].sum())
print(df.to_string(index=False))
df.to_csv(OUT / "analysis_results.csv", index=False)

print("\nOutput folder:", OUT)
