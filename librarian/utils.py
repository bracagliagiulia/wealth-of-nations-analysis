"""
utils.py
---------
Utility functions for data loading and saving.
"""

from pathlib import Path
import pandas as pd
import csv


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load a CSV dataset into a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    p = Path(filepath)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(p)


def save_cleaned_data(output_path: str, gdp: list, life: list) -> None:
    """
    Save GDP and life expectancy lists to a CSV file.

    Args:
        output_path (str): Output file path.
        gdp (list): GDP per capita values.
        life (list): Life expectancy values.
    """
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["gdp_per_capita", "life_expectancy"])
        writer.writerows(zip(gdp, life))
