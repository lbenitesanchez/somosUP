"""Funciones comunes para generación de datos."""
from __future__ import annotations
from pathlib import Path
import pandas as pd
import numpy as np


def set_seed(seed: int) -> None:
    np.random.seed(seed)


def month_range(start: str, periods: int) -> pd.DatetimeIndex:
    return pd.date_range(start=start, periods=periods, freq='MS')


def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
