import pandas as pd
from pathlib import Path

def data_loader(ontology) -> pd.DataFrame:
    df = pd.read_csv(ontology)
    required_fields = ["year","exam_month","module","topic","marks","question_type","diagram_required"]

    missing = set(required_fields) - set(df.columns)
    if missing:
        print("[Error] Ontology doesn't contain required values.")

    if df.empty:
        print("[Error] Ontology is empty!")
    
    df.columns = df.columns.str.strip()
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

    df["year"] = pd.to_numeric(df["year"], errors="raise").astype(int)
    df["module"] = pd.to_numeric(df["module"], errors="raise").astype(int)
    df["marks"] = pd.to_numeric(df["marks"], errors="raise").astype(int)
    df["diagram_required"] = pd.to_numeric(df["diagram_required"], errors="raise").astype(int)

    df["question_type"] = df["question_type"].str.lower()

    if (df["module"] < 0).any():
        print("[Error] Invalid module value.")

    print(df)
    return df
