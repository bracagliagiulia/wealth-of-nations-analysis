# The Wealth of Health: Exploring the Link Between Healthcare Systems and National Prosperity

Healthy nations are wealthy nations — exploring how economics and healthcare intertwine.

## Overview
This project investigates how the **quality and strength of a nation's healthcare system** relate to its **economic prosperity** and **overall quality of life**.  

Using data from the **World Bank Open Data portal**, the analysis explores how indicators such as **healthcare expenditure**, **life expectancy**, **infant mortality**, and **GDP per capita** interact across different countries and over time.  

The goal is to uncover patterns showing whether nations with **stronger economies** tend to build **higher-quality healthcare systems**, and how that translates into **better population health and longevity**.

## Objectives
- Examine global patterns in healthcare investment and outcomes.
- Analyze correlations between **GDP per capita**, **healthcare spending**, and **health outcomes** (life expectancy, mortality rates).
- Visualize differences between countries and regions.
- Build an interactive dashboard for exploring healthcare and economic data over time.

## Data Source
All data for this project is obtained from the **World Bank Open Data portal**.  
The project uses historical data covering economic, healthcare, and population indicators for countries around the world.

Data is accessed via the **Python package `world_bank_data`**:
- World Bank Open Data: [https://data.worldbank.org/](https://data.worldbank.org/)
- Python package documentation: [https://pypi.org/project/world-bank-data/](https://pypi.org/project/world-bank-data/)

## Indicators to Analyze
The project focuses on these key indicators:

| Category | Indicator | World Bank Code |
|----------|-----------|----------------|
| **Economic** | GDP per capita (current US$) | `NY.GDP.PCAP.CD` |
| **Healthcare Spending** | Health expenditure (% of GDP) | `SH.XPD.CHEX.GD.ZS` |
| **Health Outcomes** | Life expectancy at birth (years) | `SP.DYN.LE00.IN` |
| **Mortality** | Infant mortality rate (per 1,000 live births) | `SP.DYN.IMRT.IN` |
| **Population** | Total population | `SP.POP.TOTL` |




