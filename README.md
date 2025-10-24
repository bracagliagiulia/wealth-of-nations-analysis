# Wealth of Nations Analysis

Exploring economic and healthcare indicators using Python, including an interactive **Streamlit dashboard**.

---

## Overview

This project analyzes **GDP per capita**, **healthcare spending**, **life expectancy**, **infant mortality**, and **population** using Python.  
It demonstrates how economic prosperity and healthcare outcomes are interrelated across countries using World Bank Open Data.  
The analysis includes both static visualizations in Jupyter Notebook and an interactive Streamlit dashboard for exploration.

---

## Objectives

- Examine global patterns in healthcare and economics.  
- Analyze correlations between GDP, healthcare spending, and health outcomes.  
- Identify outliers and efficiency differences in healthcare spending.  
- Create both static and interactive visualizations.  
- Group countries by region for comparative insights.

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
├── dashboard.py  
└── requirements.txt  

---

## Analysis Steps

1. **Load and Inspect Data**  
   - Read CSV using Python.  
   - Verify headers, sample rows, and data types.

2. **Data Cleaning**  
   - Remove rows with missing or invalid GDP or Life Expectancy values.  
   - Align datasets for valid country-year entries.  
   - Implemented as a **function `clean_data()`** with docstring.

3. **Descriptive Statistics**  
   - Average, maximum, minimum GDP per capita.  
   - Average, maximum, minimum healthcare expenditure.  
   - Group by **region** using a dictionary for aggregated statistics.

4. **Correlation Analysis**  
   - Compute **Pearson correlation coefficients**:  
     - GDP vs Life Expectancy  
     - GDP vs Healthcare Expenditure  
     - Life Expectancy vs Healthcare Expenditure  
   - Encapsulated in **function `compute_correlation()`**.

5. **Visualizations**  
   - Scatter plots for GDP vs Life Expectancy and Healthcare Expenditure vs Life Expectancy.  
   - Histograms and box plots for GDP and healthcare spending.  
   - Scatter plots with **color coding by region**.  
   - Time trends for selected countries over decades.  
   - Trend lines or regression for predictive insights.

6. **Interactive Streamlit Dashboard**  
   - `dashboard.py` allows users to explore data interactively.  
   - Provides correlation summary, scatter plots, and filters by region.  
   - Built using **Streamlit**, **matplotlib**, and **numpy**.

7. **Export Cleaned Data**  
   - Cleaned GDP and Life Expectancy dataset saved to `outputs/gdp_life_expectancy_cleaned.csv`.

---

## Key Findings

- **GDP vs Life Expectancy:** Moderate positive correlation; wealthier countries generally have longer life expectancy.  
- **Healthcare Expenditure:** Low global correlation with GDP and Life Expectancy, indicating differences in efficiency.  
- **Outliers:** Some countries spend a lot but have poor health outcomes; others achieve good outcomes with modest spending.  
- **GDP Distribution:** Highly skewed; a few countries have extremely high GDP per capita.  
- **Regional Insights:** Grouping by region highlights patterns invisible in global averages.

---

## Future Directions

- Fit **regression models** to predict Life Expectancy from GDP and healthcare spending.  
- Extend analysis to **income groups or regions**.  
- Add **interactive filtering** and **time-series exploration** in Streamlit.  
- Investigate **healthcare efficiency metrics** across countries.  
- Expand dashboard to include other indicators such as **infant mortality** and **population trends**.

<<<<<<< HEAD
---

## Tools Used
=======
 ## Tools Used
>>>>>>> 6ae6c72c33d1021de424402096c0a3220c8ad802

- Python 3.14 and Python 3.12
- Libraries: streamlit, matplotlib, numpy, pandas, csv
- Jupyter Notebook for static exploration
- Streamlit for interactive dashboard

---

## How to Run 

1. Place the CSV dataset in the `data/` folder.  
2. For notebook analysis: run `explore_healthcare_vs_economy.ipynb` sequentially.  
3. For interactive dashboard: activate the virtual environment and run:

```powershell
.\venv_streamlit\Scripts\Activate.ps1
streamlit run dashboard.py

---
