"""
models.py
----------
Simple dataclasses used to represent records in the project.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CountryYear:
    """Container for a single country-year record."""
    country: str
    year: Optional[int]
    gdp_per_capita: Optional[float]
    health_exp_gdp: Optional[float]
    life_expectancy: Optional[float]
    infant_mortality: Optional[float]
    population: Optional[float]
