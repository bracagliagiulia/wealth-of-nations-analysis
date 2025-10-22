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
├── data/  
│   └── worldbank_healthcare_data.csv  
├── notebook/  
│   └── explore_healthcare_vs_economy.ipynb  
├── outputs/  
│   └── gdp_life_expectancy_cleaned.csv  
└── requirements.txt  

---

## Analysis Steps

1. **Load and inspect data:**  
   - Read CSV into Python and check headers and sample rows.  

2. **Data Cleaning:**  
   - Remove rows with missing or invalid GDP and Life Expectancy values.  
   - Align datasets for valid country-year entries.  

3. **Descriptive Statistics:**  
   - Average GDP per capita  
   - Countries above/below average GDP  
   - Maximum and minimum GDP per capita  
   - Average, maximum, and minimum healthcare expenditure  

4. **Visualizations:**  
   - Line plots for GDP trends  
   - Scatter plots:  
     - GDP vs Life Expectancy  
     - Healthcare Expenditure vs Life Expectancy  
   - Histograms for GDP distribution  
   - Scatter plots with correlation annotations  
   - Time trends for selected countries  

5. **Correlation Analysis:**  
   - Pearson correlation coefficients between:  
     - GDP vs Life Expectancy  
     - GDP vs Healthcare Expenditure  
     - Life Expectancy vs Healthcare Expenditure  

6. **Export Cleaned Data:**  
   - Save cleaned GDP and Life Expectancy dataset to `outputs/gdp_life_expectancy_cleaned.csv`  

---

## Key Findings

- **GDP vs Life Expectancy:** Moderate positive correlation; wealthier countries generally have longer life expectancy.  
- **Healthcare expenditure:** Low correlation with GDP and Life Expectancy globally, indicating efficiency differences.  
- **Outliers:** Some countries spend a lot but have poor health outcomes, while others achieve good outcomes with modest spending.  
- **GDP distribution:** Highly skewed with a few countries having extremely high GDP per capita.  

---

## Future Directions

- Analyze correlations **by region** or **income group** to identify regional patterns.  
- Fit **regression models** to predict Life Expectancy based on GDP and healthcare spending.  
- Explore **time-series trends** for multiple countries over decades.  
- Create **color-coded scatter plots** by region or income category.  
- Investigate **efficiency of healthcare spending** and its impact on health outcomes.  

---

## How to Run

1. Place the CSV dataset in the `data/` folder.  
2. Run the notebook `explore_healthcare_vs_economy.ipynb` sequentially.  
3. Use `outputs/gdp_life_expectancy_cleaned.csv` for any additional analyses.  

---

## Tools Used

- Python 3.14  
- Libraries: `matplotlib`, `numpy`, `csv`  
- Jupyter Notebook for interactive exploration and plotting  

---
