import argparse
import pandas as pd

WANTED = {
    "Created Date": "created_date",
    "Closed Date": "closed_date",
    "Borough": "borough",
    "Incident Zip": "zip",
    "Complaint Type": "complaint_type",
    "Descriptor": "descriptor",
}
DATE_COLS = ["Created Date", "Closed Date", "Open Date", "Request Created Date"]

def _parse_dates(df: pd.DataFrame) -> pd.DataFrame:
    for c in DATE_COLS:
        if c in df.columns:
            df[c] = pd.to_datetime(df[c], errors="coerce")
    return df

def _rename_keep(df: pd.DataFrame) -> pd.DataFrame:
    keep = [c for c in df.columns if c in WANTED]
    if keep:
        df = df[keep].rename(columns=WANTED)
    return df

def main(in_path: str, out_path: str) -> None:
    df = pd.read_csv(in_path)
    df = _parse_dates(df)
    df = _rename_keep(df)
    df = df.drop_duplicates().reset_index(drop=True)
    df.to_csv(out_path, index=False)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Clean 311 CSV")
    p.add_argument("--in", dest="in_path", required=True)
    p.add_argument("--out", dest="out_path", required=True)
    args = p.parse_args()
    main(args.in_path, args.out_path)
