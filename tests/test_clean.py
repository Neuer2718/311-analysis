import pandas as pd
from analysis.clean import main as clean_main
from pathlib import Path
import tempfile

def test_clean_runs_and_writes():
    with tempfile.TemporaryDirectory() as d:
        raw = Path(d) / "raw.csv"
        out = Path(d) / "clean.csv"
        pd.DataFrame({
            "Created Date": ["2021-01-01", "bad", "2021-01-01"],
            "Borough": ["X", "Y", "X"],
            "Complaint Type": ["Noise", "Heat", "Noise"]
        }).to_csv(raw, index=False)
        clean_main(str(raw), str(out))
        assert out.exists()
        df = pd.read_csv(out)
        assert len(df) <= 3
