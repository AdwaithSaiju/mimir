import pandas as pd
from pathlib import Path

def data_loader(ontology) -> pd.DataFrame:
    df = pd.read_csv(ontology)
    df.columns = df.columns.str.strip()
    
    required_fields = ["year","exam_month","module","topic","marks","question_type","diagram_required"]
    missing = set(required_fields) - set(df.columns)
    if missing:
        print("[Error] Ontology doesn't contain required values.")
        return pd.DataFrame()

    if df.empty:
        print("[Error] Ontology is empty!")
        return pd.DataFrame()
    
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip().str.lower()

    df["year"] = pd.to_numeric(df["year"], errors="coerce")
    df["module"] = pd.to_numeric(df["module"], errors="coerce")
    df["marks"] = pd.to_numeric(df["marks"], errors="coerce")
    df["diagram_required"] = pd.to_numeric(df["diagram_required"], errors="coerce")

    if df["year"].isna().any() or df["module"].isna().any() or df["marks"].isna().any() or df["diagram_required"].isna().any():
        print("[Error] Non-numeric values found in numeric fields.")
        return pd.DataFrame()

    df["year"] = df["year"].astype(int)
    df["module"] = df["module"].astype(int)
    df["marks"] = df["marks"].astype(int)
    df["diagram_required"] = df["diagram_required"].astype(int)

    df["question_type"] = df["question_type"].str.lower()

    if ((df["module"] < 1) | (df["module"] > 4)).any():
        print("[Error] Invalid module value.")
        return pd.DataFrame()

    if (df["marks"] < 1).any():
        print("[Error] Invalid mark distribution found!")
        return pd.DataFrame()

    if (~df["question_type"].isin(["long", "short"])).any():
        print("[Error] Invalid question type.")
        return pd.DataFrame()
    
    if(~df["diagram_required"].isin([0,1])).any():
        print("[Error] Only 0 and 1 allowed in Diagram required field.")
        return pd.DataFrame()

    print(df)
    return df