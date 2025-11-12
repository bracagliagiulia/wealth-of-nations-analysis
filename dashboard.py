"""
Wealth of Nations Dashboard
Analyzes the relationship between GDP per capita, healthcare expenditure, and life expectancy.
Built with Streamlit.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Reuse project package
try:
    from librarian.utils import load_data
    from librarian.core import clean_gdp_life, compute_correlation
    HAVE_LIBRARIAN = True
except Exception:
    HAVE_LIBRARIAN = False

# --- PAGE SETUP ---
st.set_page_config(page_title="Wealth of Nations Dashboard 🌍", layout="wide")
st.title("🌍 Wealth of Nations — Health & Economy")
st.caption("Interactive exploration of GDP per capita, healthcare spending, and life expectancy (World Bank data).")

# --- PATHS ---
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / "data" / "worldbank_healthcare_data.csv"

# --- LOAD DATA (cached) ---
@st.cache_data
def load_df(path: Path) -> pd.DataFrame:
    try:
        if HAVE_LIBRARIAN:
            # Use your reusable loader
            df = load_data(str(path))
        else:
            df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        return pd.DataFrame()

df_raw = load_df(DATA_PATH)

if df_raw.empty:
    st.error("❌ Data not found. Make sure `data/worldbank_healthcare_data.csv` exists.")
    st.stop()

st.success("✅ Data loaded")
with st.expander("Preview data (first 10 rows)", expanded=False):
    st.dataframe(df_raw.head(10), use_container_width=True)

# --- CLEAN DATA ---
def clean_more(df: pd.DataFrame) -> pd.DataFrame:
    """Coerce key numeric columns and drop invalids; reuse package if available."""
    if HAVE_LIBRARIAN:
        base = clean_gdp_life(df)  # ensures gdp_per_capita & life_expectancy numeric, drops NaNs
    else:
        base = df.copy()
        for c in ["gdp_per_capita", "life_expectancy"]:
            base[c] = pd.to_numeric(base.get(c), errors="coerce")
        base = base.dropna(subset=["gdp_per_capita", "life_expectancy"])
        base = base[(base["gdp_per_capita"] > 0) & (base["life_expectancy"] > 0)]

    # Health spend & year optional
    if "health_exp_gdp" in base.columns:
        base["health_exp_gdp"] = pd.to_numeric(base["health_exp_gdp"], errors="coerce")
    if "year" in base.columns:
        base["year"] = pd.to_numeric(base["year"], errors="coerce").astype("Int64")
    return base

df = clean_more(df_raw)

# --- OPTIONAL REGION TAGGING (non-blocking) ---
# Light mapping to avoid breaking if countries not in list
REGIONS = {
    "Europe": {"France","Germany","Italy","Spain","United Kingdom","Sweden","Norway"},
    "Asia": {"China","Japan","India","South Korea","Indonesia","Thailand"},
    "Africa": {"Nigeria","Egypt","South Africa","Kenya","Morocco"},
    "Americas": {"United States","Canada","Brazil","Mexico","Argentina"},
    "Oceania": {"Australia","New Zealand"},
}
def to_region(country: str) -> str:
    if not isinstance(country, str):
        return "Other"
    for r, names in REGIONS.items():
        if country in names:
            return r
    return "Other"

if "country" in df.columns:
    df["region"] = df["country"].apply(to_region)

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filters")

# Year slider (if present)
if "year" in df.columns and df["year"].notna().any():
    years = sorted([int(y) for y in df["year"].dropna().unique()])
    sel_year = st.sidebar.slider("Year", min_value=min(years), max_value=max(years), value=max(years), step=1)
    df = df[df["year"] == sel_year]
    st.caption(f"📅 Showing data for year **{sel_year}**")
else:
    st.caption("📅 Dataset has no `year` column; showing all rows.")

# Region filter (if present)
if "region" in df.columns:
    regions = ["All"] + sorted(df["region"].unique().tolist())
    sel_region = st.sidebar.selectbox("Region", regions, index=0)
    if sel_region != "All":
        df = df[df["region"] == sel_region]

# Country search (optional quick filter)
if "country" in df.columns:
    q = st.sidebar.text_input("Search country (contains)")
    if q:
        df = df[df["country"].str.contains(q, case=False, na=False)]

# --- CORRELATION (GDP vs Life) ---
x = pd.to_numeric(df["gdp_per_capita"], errors="coerce").to_numpy()
y = pd.to_numeric(df["life_expectancy"], errors="coerce").to_numpy()
mask = ~np.isnan(x) & ~np.isnan(y)
if mask.sum() >= 2:
    r = compute_correlation(x[mask].tolist(), y[mask].tolist()) if HAVE_LIBRARIAN else float(np.corrcoef(x[mask], y[mask])[0, 1])
    st.metric("📈 Correlation (GDP vs Life Expectancy)", f"{r:.3f}", help=f"Computed on n = {int(mask.sum())} observations")
else:
    st.metric("📈 Correlation (GDP vs Life Expectancy)", "N/A", help="Not enough valid points")

# --- LAYOUT ---
col1, col2 = st.columns(2, gap="large")

# Plot 1: GDP vs Life (log x)
with col1:
    st.subheader("💰 GDP vs Life Expectancy")
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(x[mask], y[mask], alpha=0.6)
    ax.set_xscale("log")
    ax.set_xlabel("GDP per capita (US$, log scale)")
    ax.set_ylabel("Life expectancy (years)")
    title_suffix = ""
    if "region" in df.columns:
        title_suffix = f" — {sel_region}" if 'sel_region' in locals() and sel_region != "All" else ""
    ax.set_title(f"GDP vs Life Expectancy{title_suffix}")
    plt.tight_layout()
    st.pyplot(fig)

# Plot 2: Health spend vs Life (if available)
with col2:
    st.subheader("🏥 Health Expenditure vs Life Expectancy")
    if "health_exp_gdp" in df.columns and df["health_exp_gdp"].notna().any():
        hx = pd.to_numeric(df["health_exp_gdp"], errors="coerce").to_numpy()
        mask2 = ~np.isnan(hx) & ~np.isnan(y)
        if mask2.sum() >= 2:
            r2 = compute_correlation(hx[mask2].tolist(), y[mask2].tolist()) if HAVE_LIBRARIAN else float(np.corrcoef(hx[mask2], y[mask2])[0, 1])
            fig2, ax2 = plt.subplots(figsize=(6,4))
            ax2.scatter(hx[mask2], y[mask2], alpha=0.6)
            ax2.set_xlabel("Current health expenditure (% of GDP)")
            ax2.set_ylabel("Life expectancy (years)")
            ax2.set_title(f"Health Expenditure vs Life (r = {r2:.2f}, n = {int(mask2.sum())})")
            plt.tight_layout()
            st.pyplot(fig2)
        else:
            st.info("Not enough valid points to plot health expenditure vs life expectancy.")
    else:
        st.info("Column `health_exp_gdp` not found in dataset.")

# Distribution (GDP)
st.subheader("📊 GDP per Capita — Distribution")
fig3, ax3 = plt.subplots(figsize=(8,3.8))
pd.to_numeric(df["gdp_per_capita"], errors="coerce").plot(kind="hist", bins=30, edgecolor="black", ax=ax3)
ax3.set_xlabel("GDP per capita (US$)")
ax3.set_ylabel("Number of countries")
plt.tight_layout()
st.pyplot(fig3)

# Summary table (compact)
st.subheader("🔍 Summary Statistics (filtered)")
show_cols = [c for c in ["country","region","year","gdp_per_capita","health_exp_gdp","life_expectancy"] if c in df.columns]
st.dataframe(df[show_cols].head(20), use_container_width=True)

# Download filtered data
csv_bytes = df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download filtered data (CSV)", data=csv_bytes, file_name="wealth_health_filtered.csv", mime="text/csv")

st.markdown("---")
st.markdown("Made with ❤️ by Giulia — Streamlit + Python 3.12")
