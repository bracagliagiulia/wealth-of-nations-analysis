# librarian/utils.py
"""Utility functions for loading, cleaning, and saving CSV data."""

from pathlib import Path
import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """
    Load CSV into a pandas DataFrame.
    Args:
        filepath: path to CSV file
    Returns:
        pd.DataFrame: raw DataFrame (may contain NaNs)
    """
    p = Path(filepath)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    df = pd.read_csv(p)
    return df


def save_cleaned_data(output_path: str, gdp: list, life: list) -> None:
    """
    Save two aligned lists (gdp, life) to CSV.
    Args:
        output_path: path to save csv
        gdp: list of GDP values
        life: list of Life Expectancy values
    """
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    import csv
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["gdp_per_capita", "life_expectancy"])
        for gd, lf in zip(gdp, life):
            writer.writerow([gd, lf])
