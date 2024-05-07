import pandas as pd
from typing import Any


def write_csv(data: list[list[Any]], file_name: str) -> None:
    df = pd.DataFrame(data)
    df.to_csv(file_name)


def read_csv(file_name: str) -> list[Any]:
    df = pd.read_csv(file_name)
    return list(df.iloc[:, 0])
