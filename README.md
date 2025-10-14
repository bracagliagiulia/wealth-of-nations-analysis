# wealth-of-nations-analysis
Exploring economic and healthcare indicators using basic Python code.

## Overview
This project analyzes GDP per capita, healthcare spending, life expectancy, infant mortality, and population using basic Python. The analysis demonstrates how economic prosperity and healthcare systems are interconnected across countries.

## Objectives
- Examine global patterns in healthcare investment and economic performance.
- Analyze correlations between GDP per capita, healthcare spending, and health outcomes.
- Create basic visualizations to identify patterns and trends.

## Data Source
All data comes from the **World Bank Open Data portal** in CSV format. The dataset contains historical indicators for countries worldwide.

### Links
- [World Bank Open Data](https://data.worldbank.org/)
- Indicators are accessed using their respective World Bank codes (see below).

## Indicators
| Category | Indicator | World Bank Code |
|----------|-----------|----------------|
| Economic | GDP per capita (current US$) | NY.GDP.PCAP.CD |
| Healthcare | Health expenditure (% of GDP) | SH.XPD.CHEX.GD.ZS |
| Health outcomes | Life expectancy at birth (years) | SP.DYN.LE00.IN |
| Mortality | Infant mortality rate (per 1,000 live births) | SP.DYN.IMRT.IN |
| Population | Total population | SP.POP.TOTL |

## Project Structure
wealth-of-nations-analysis/ >>
  README.md # Project overview and instructions
  data/ # CSV files from World Bank >>
    worldbank_healthcare_data.csv
  notebook/ # Jupyter Notebook for exploration >>
    explore_healthcare_vs_economy.ipynb
  requirements.txt # Python packages needed

### Key Points
- The **data folder** stores CSV files used in the analysis.
- The **notebook folder** contains the Jupyter Notebook which loads the dataset, performs basic analysis, and visualizes results using Python.
- Python standard libraries are used, mainly `csv` for data reading and `matplotlib.pyplot` for plotting.
- The project is designed to be simple, reproducible, and easy to run using basic Python.






