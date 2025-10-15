# Wealth of Nations Analysis

Exploring economic and healthcare indicators using basic Python code.

---

## Overview

This project analyzes **GDP per capita**, **healthcare spending**, **life expectancy**, **infant mortality**, and **population** using simple Python techniques.  
It demonstrates how economic prosperity and healthcare outcomes are interrelated across countries using World Bank Open Data.

---

## Objectives

- Examine global patterns in healthcare and economics.  
- Analyze correlations between GDP, healthcare spending, and health outcomes.  
- Create basic plots to visualize trends and disparities.  

---

## Data Source

All data comes from the **[World Bank Open Data](https://data.worldbank.org/)** portal in CSV format.  
The dataset includes multiple health and economic indicators for countries worldwide.

### Indicators Used

| Category | Indicator | World Bank Code |
|-----------|------------|----------------|
| Economic | GDP per capita (current US$) | NY.GDP.PCAP.CD |
| Healthcare | Health expenditure (% of GDP) | SH.XPD.CHEX.GD.ZS |
| Health outcomes | Life expectancy at birth (years) | SP.DYN.LE00.IN |
| Mortality | Infant mortality (per 1,000 live births) | SP.DYN.IMRT.IN |
| Population | Total population | SP.POP.TOTL |

---

## Project Structure

wealth-of-nations-analysis/
│
├── README.md
│
├── data/
│ └── worldbank_healthcare_data.csv
│
├── notebook/
│ └── explore_healthcare_vs_economy.ipynb
│
└── requirements.txt
