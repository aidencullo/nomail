import pandas as pd
from typing import List, Any


def write_csv(data: List[List[Any]], file_name: str) -> None:
    df = pd.DataFrame(data)
    df.to_csv(file_name)


def read_csv(file_name: str) -> List[Any]:
    df = pd.read_csv(file_name)
    return list(df.iloc[:, 0])
