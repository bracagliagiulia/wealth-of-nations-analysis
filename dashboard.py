"""
Wealth of Nations Dashboard
Analyzes the relationship between GDP per capita, healthcare expenditure, and life expectancy.
Built with Streamlit.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- PAGE SETUP ---
st.set_page_config(page_title="Wealth of Nations Dashboard 🌍", layout="centered")

st.title("🌍 Wealth of Nations Dashboard")
st.markdown("""
This interactive dashboard explores the relationship between **GDP per capita**,  
**Healthcare expenditure**, and **Life Expectancy** across countries using World Bank data.
""")

# --- LOAD DATA ---
@st.cache_data
def load_data(filepath: str) -> pd.DataFrame:
    """Load data from a CSV file and return a DataFrame."""
    try:
        df = pd.read_csv(filepath)
        st.success("✅ Data loaded successfully!")
        return df
    except FileNotFoundError:
        st.error("❌ File not found. Please place your CSV in the 'data/' folder.")
        return pd.DataFrame()

data = load_data("data/worldbank_healthcare_data.csv")

# --- CHECK DATA ---
if data.empty:
    st.warning("⚠️ No data loaded. Please ensure your CSV file is available.")
    st.stop()

st.subheader("📊 Data Preview")
st.dataframe(data.head())

# --- CLEAN DATA ---
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dataset: drop missing or invalid GDP and Life Expectancy rows."""
    df = df.copy()
    required_cols = ["gdp_per_capita", "life_expectancy"]
    for col in required_cols:
        if col not in df.columns:
            st.error(f"Column '{col}' is missing in the dataset!")
            return pd.DataFrame()
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=required_cols)
    df = df[(df["gdp_per_capita"] > 0) & (df["life_expectancy"] > 0)]
    return df

data_clean = clean_data(data)

# --- REGION GROUPING ---
regions = {
    "Europe": ["France", "Germany", "Italy", "Spain", "United Kingdom", "Sweden", "Norway"],
    "Asia": ["China", "Japan", "India", "South Korea", "Indonesia", "Thailand"],
    "Africa": ["Nigeria", "Egypt", "South Africa", "Kenya", "Morocco"],
    "Americas": ["United States", "Canada", "Brazil", "Mexico", "Argentina"],
    "Oceania": ["Australia", "New Zealand"],
}

def assign_region(country: str) -> str:
    """Assign a region based on country name."""
    for region, countries in regions.items():
        if country in countries:
            return region
    return "Other"

if "country" in data_clean.columns:
    data_clean["region"] = data_clean["country"].apply(assign_region)
else:
    data_clean["region"] = "Unknown"

# --- CORRELATION METRIC ---
gdp = data_clean["gdp_per_capita"].to_numpy()
life = data_clean["life_expectancy"].to_numpy()

if len(gdp) != len(life):
    st.warning("⚠️ GDP and Life Expectancy arrays do not match in length.")
    correlation = np.nan
else:
    correlation = np.corrcoef(gdp, life)[0, 1]

st.metric(label="📈 Correlation (GDP vs Life Expectancy)", value=f"{correlation:.3f}" if not np.isnan(correlation) else "N/A")

# --- SIDEBAR REGION FILTER ---
st.sidebar.header("Filter Options")
selected_region = st.sidebar.selectbox(
    "Select Region:",
    options=["All"] + list(regions.keys())
)

if selected_region != "All":
    data_filtered = data_clean[data_clean["region"] == selected_region]
else:
    data_filtered = data_clean

st.markdown(f"### Data for Region: {selected_region}")
st.dataframe(data_filtered[["country", "gdp_per_capita", "life_expectancy"]].head())

# --- PLOTS ---
st.subheader("💰 GDP vs Life Expectancy")
fig, ax = plt.subplots()
ax.scatter(data_filtered["gdp_per_capita"], data_filtered["life_expectancy"], alpha=0.6, color="teal")
ax.set_xlabel("GDP per Capita (USD)")
ax.set_ylabel("Life Expectancy (Years)")
ax.set_title(f"GDP vs Life Expectancy ({selected_region})")
st.pyplot(fig)

st.subheader("📊 GDP Distribution")
fig2, ax2 = plt.subplots()
ax2.hist(data_filtered["gdp_per_capita"], bins=30, color="purple", alpha=0.7)
ax2.set_xlabel("GDP per Capita (USD)")
ax2.set_ylabel("Number of Countries")
ax2.set_title(f"GDP Distribution ({selected_region})")
st.pyplot(fig2)

# --- SUMMARY STATISTICS ---
st.markdown("### 🔍 Summary Statistics")
st.write(data_filtered[["gdp_per_capita", "life_expectancy"]].describe())

st.markdown("---")
st.markdown("Made with ❤️ by Giulia using Streamlit and Python 3.12")