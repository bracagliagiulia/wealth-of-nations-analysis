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

Project Description: Exploring the Wealth and Health of Nations

This project investigates the relationship between economic and healthcare indicators across countries using publicly available data from the World Bank. The main goal is to understand how national wealth and investments in healthcare relate to overall health outcomes.

We analyze several key indicators for each country, including:

  GDP per capita – a measure of average economic output per person, representing the wealth of a nation.
  
  Healthcare expenditure (% of GDP) – how much a country spends on healthcare relative to its total economic output.
  
  Life expectancy at birth – the average number of years a person is expected to live, reflecting overall health conditions.
  
  Infant mortality rate – the number of infants dying before age one per 1,000 live births, indicating child health outcomes.
  
  Population – the total number of people in the country.

The project follows a step-by-step approach:

  Data Cleaning and Inspection: We load and inspect the dataset to identify missing or invalid values. This ensures our analysis is based on accurate and consistent data.
  
  Descriptive Statistics: We compute averages, maximums, and minimums for GDP per capita and healthcare spending to summarize the overall economic and health landscape.
  
  Comparative Analysis: We classify countries by whether their GDP per capita is above or below the global average, helping to highlight disparities in wealth.
  
  Visualization: We use scatter plots and line charts to visualize relationships between key indicators, such as:
  
  GDP per capita vs Life Expectancy – to explore whether wealthier countries tend to have healthier populations.
  
  Healthcare Expenditure vs Life Expectancy – to examine the impact of healthcare investment on population health.

Exporting Simplified Datasets: We save curated datasets containing only the key indicators to facilitate further analysis or reporting.

Through these steps, the project provides a clear overview of global economic and health patterns, highlights outliers, and enables visual exploration of important correlations. The findings can inform discussions about the links between wealth, healthcare spending, and human well-being.
