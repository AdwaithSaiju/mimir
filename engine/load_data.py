import pandas as pd
from pathlib import Path

def data_loader(ontology) ->  pd.DataFrame:
    df = pd.read_csv(ontology)
    print(df.head(5))
    return df
    


