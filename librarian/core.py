"""
core.py
---------
Core analytical functions for the Wealth of Nations project.

Includes data cleaning and correlation computation utilities.
"""

from typing import List
import pandas as pd
import numpy as np


def clean_gdp_life(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean GDP and life expectancy data.

    Args:
        df (pd.DataFrame): Input DataFrame with at least
            'gdp_per_capita' and 'life_expectancy' columns.

    Returns:
        pd.DataFrame: A cleaned copy where GDP and life expectancy are numeric
        and rows with missing values are dropped.
    """
    df_clean = df.copy()
    df_clean["gdp_per_capita"] = pd.to_numeric(df_clean["gdp_per_capita"], errors="coerce")
    df_clean["life_expectancy"] = pd.to_numeric(df_clean["life_expectancy"], errors="coerce")
    df_clean = df_clean.dropna(subset=["gdp_per_capita", "life_expectancy"])
    return df_clean


def compute_correlation(x: List[float], y: List[float]) -> float:
    """
    Compute the Pearson correlation coefficient between two numeric lists.

    Args:
        x (List[float]): First numeric list.
        y (List[float]): Second numeric list (same length as x).

    Returns:
        float: Pearson correlation coefficient, or np.nan if invalid.
    """
    if not x or not y or len(x) != len(y):
        return float("nan")
    return float(np.corrcoef(np.array(x), np.array(y))[0, 1])
