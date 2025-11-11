# librarian/core.py
"""Core functions used by notebooks and the dashboard."""

from typing import Tuple, List
import pandas as pd
import numpy as np

def clean_gdp_life(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns cleaned DataFrame with GDP, life expectancy, and country preserved.
    """
    df2 = df.copy()
    df2["gdp_per_capita"] = pd.to_numeric(df2["gdp_per_capita"], errors="coerce")
    df2["life_expectancy"] = pd.to_numeric(df2["life_expectancy"], errors="coerce")
    df2 = df2.dropna(subset=["gdp_per_capita", "life_expectancy"])
    return df2

def compute_correlation(x: List[float], y: List[float]) -> float:
    """Compute Pearson correlation, return np.nan if not computable."""
    if len(x) == 0 or len(y) == 0 or len(x) != len(y):
        return float("nan")
    return float(np.corrcoef(np.array(x), np.array(y))[0, 1])
