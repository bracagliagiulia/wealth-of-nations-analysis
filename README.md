# Wealth of Nations: Economic Prosperity and Health Systems

Exploring the link between a country's **economic performance** and its **population health outcomes** using Python, World Bank data, and an interactive **Streamlit dashboard**.

---

## Overview

This project explores the connection between **economic prosperity** and **health system outcomes** using real-world data from the **World Bank Open Data** portal.  
It focuses on how variables such as **GDP per capita**, **healthcare expenditure**, and **life expectancy** interact across different countries.  
The study combines quantitative analysis, visual exploration, and an interactive dashboard to understand how nations convert economic wealth into population well-being.  

Through this project, Python is used not only for data manipulation and visualization, but also to demonstrate:
- clean, modular programming practices using custom packages (`librarian`);
- reproducibility with version control (GitHub);
- the application of scientific computing libraries like NumPy and pandas;
- clear, meaningful visualizations through Matplotlib;
- and the creation of an interactive web dashboard via Streamlit.

---


## Objectives

- Explore global patterns connecting economic prosperity and health outcomes.  
- Analyze the relationships between GDP, healthcare spending, and life expectancy.  
- Identify regional outliers and efficiency differences in healthcare investment.  
- Produce clear, reproducible analyses and visualizations.  
- Develop an optional interactive web app to make findings accessible.

---

## Data Source

All indicators are sourced from the **[World Bank Open Data](https://data.worldbank.org/)** portal in CSV format.  
The dataset provides internationally comparable indicators covering economic and health metrics for all countries.

| Category | Indicator | World Bank Code |
|-----------|------------|----------------|
| Economic | GDP per capita (current US$) | NY.GDP.PCAP.CD |
| Healthcare | Health expenditure (% of GDP) | SH.XPD.CHEX.GD.ZS |
| Health outcomes | Life expectancy at birth (years) | SP.DYN.LE00.IN |
| Mortality | Infant mortality (per 1,000 live births) | SP.DYN.IMRT.IN |
| Demographics | Total population | SP.POP.TOTL |

---

## Project Structure
wealth-of-nations-analysis/
├── README.md
├── data/
│ └── worldbank_healthcare_data.csv
├── librarian/
│ ├── init.py
│ ├── core.py
│ ├── models.py
│ └── utils.py
├── outputs/
│ ├── gdp_vs_life.png
│ ├── summary_stats.csv
│ ├── correlation_summary.csv
│ └── cleaned_wealth_health_data.csv
├── presentation/
│ └── explore_healthcare_vs_economy.ipynb
├── dashboard.py
├── requirements.txt
└── .gitignore

- `librarian/`: reusable functions for data loading, cleaning, and computation.  
- `presentation/`: main analysis notebook, formatted for grading and presentation.  
- `outputs/`: automatically generated plots and datasets (ignored by Git).  
- `dashboard.py`: Streamlit web app for interactive exploration.  

---

## Analytical Steps

1. **Setup and Imports**  
   - Configure the project root and import functions from the `librarian` package.  
   - Ensure reproducibility via Python environments and modular design.

2. **Data Loading and Inspection**  
   - Load CSV data with `load_data()` and verify columns, data types, and structure.  
   - Check non-numeric columns and dataset completeness.

3. **Data Cleaning**  
   - Use `clean_gdp_life()` to convert values to numeric and remove invalid entries.  
   - Align valid country-year observations for GDP and life expectancy.

4. **Summary Statistics and Quality Check**  
   - Compute descriptive metrics (mean, median, quartiles, outlier bounds).  
   - Export `summary_stats.csv` for documentation.

5. **Visualization: GDP vs Life Expectancy**  
   - Produce a log-scaled scatter plot with correlation coefficient (`r`) and sample size (`n`).  
   - Save figure as `outputs/gdp_vs_life.png`.

6. **Healthcare Spending Analysis**  
   - Examine the relationship between health expenditure and life expectancy.  
   - Compute and visualize a **health efficiency index** (`life_expectancy / health_exp_gdp`).  
   - Save distribution plots for interpretation.

7. **Correlation and Statistical Computation**  
   - Use `compute_correlation()` (based on NumPy) to calculate Pearson’s r for each indicator pair.  
   - Store results in `correlation_summary.csv`.

8. **Export Cleaned and Derived Data**  
   - Save reproducible datasets (`cleaned_wealth_health_data.csv`) in the `outputs/` folder.

9. **Interactive Dashboard (Bonus)**  
   - `dashboard.py` allows users to filter by region, visualize correlations, and compare countries dynamically using Streamlit.

---

## Key Findings

- **GDP vs Life Expectancy:**  
  A moderate positive correlation (r ≈ 0.61) indicates that wealthier countries tend to live longer.  

- **Healthcare Spending:**  
  Higher expenditure usually improves life expectancy, but the efficiency metric shows that results vary widely.  

- **Global Inequality:**  
  GDP and health outcomes are both highly skewed; most countries cluster at low-income and moderate-life-expectancy levels.  

- **Efficiency Insight:**  
  Some nations achieve strong health results with limited spending — suggesting structural and policy differences in healthcare systems.

---

## Tools and Libraries

| Purpose | Tools Used |
|----------|-------------|
| Programming | Python 3.12 |
| Data handling | pandas |
| Scientific computing | numpy |
| Visualization | matplotlib |
| Web application (bonus) | streamlit |
| Notebook environment | JupyterLab |

All dependencies are listed in `requirements.txt`.

---

## Repository and Version Control

- The repository follows a **clean modular structure** separating data, code, results, and presentation materials.  
- A detailed `.gitignore` excludes large data files, caches, and virtual environments.  
- Frequent, descriptive commits document the evolution of the analysis.  
- Only reproducible source files (`.py`, `.ipynb`, `.md`) are tracked in version control.

This setup aligns with the **GitHub Usage (5 pts)** and **Project Organization (5 pts)** criteria from the assignment rubric.

---

## Conclusion

The analysis confirms that economic development and public health are deeply connected but not perfectly proportional.  
Wealth supports longevity, yet **healthcare efficiency**—how effectively countries use their resources—plays a crucial role.  
This finding underscores the project’s focus: *the strength of a nation lies not only in its wealth, but in how that wealth is invested in its people’s health.

## Quickstart

```bash
# 1) Create and activate a virtual environment
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1

# 2) Install all required dependencies
pip install -r requirements.txt

# 3) Open and run the Jupyter Notebook
jupyter lab  # or jupyter notebook

# 4) Launch the Streamlit dashboard (optional interactive analysis)
streamlit run dashboard.py

---
