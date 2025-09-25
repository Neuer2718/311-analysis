import argparse
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def _ensure_out_dir(path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def plot_by_month(df: pd.DataFrame, out_path: str) -> None:
    date_col = None
    for c in ("created_date", "Created Date", "Open Date", "Request Created Date"):
        if c in df.columns:
            date_col = c
            break
    if date_col is None:
        raise ValueError("No created/open date column found.")
    s = pd.to_datetime(df[date_col], errors="coerce").dt.to_period("M").dt.to_timestamp()
    counts = s.value_counts().sort_index()
    _ensure_out_dir(out_path)
    plt.figure()
    counts.plot(kind="line", marker="o")
    plt.title("311 Requests per Month")
    plt.xlabel("Month")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def plot_top_complaints(df: pd.DataFrame, out_path: str, k: int = 10) -> None:
    col = None
    for c in ("complaint_type", "Complaint Type"):
        if c in df.columns:
            col = c
            break
    if col is None:
        return
    top = df[col].value_counts().head(k)
    _ensure_out_dir(out_path)
    plt.figure()
    top.plot(kind="bar")
    plt.title(f"Top {k} Complaint Types")
    plt.xlabel("Complaint Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()

def main(in_path: str, plot_month_path: str, plot_complaints_path: str) -> None:
    df = pd.read_csv(in_path)
    plot_by_month(df, plot_month_path)
    plot_top_complaints(df, plot_complaints_path)

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Basic EDA for 311 data")
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--plot-month", required=True)
    ap.add_argument("--plot-complaints", required=True)
    args = ap.parse_args()
    main(args.in_path, args.plot_month, args.plot_complaints)
