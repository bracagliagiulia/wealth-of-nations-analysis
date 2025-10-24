# ## Overview
# This app visualizes the relationship between GDP, healthcare expenditure, and life expectancy.

st.markdown("## Overview")
st.write("This app explores the relationship between GDP and Life Expectancy...")

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import csv

# --- Load Data ---
def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

data = load_data('data/worldbank_healthcare_data.csv')

# --- Clean Data ---
def clean_data(data):
    gdp, life = [], []
    for row in data:
        try:
            gdp.append(float(row['gdp_per_capita']))
            life.append(float(row['life_expectancy']))
        except:
            pass
    return gdp, life

gdp, life = clean_data(data)

# --- Streamlit App ---
st.title("🌍 Wealth of Nations Dashboard")
st.markdown("Analyze the relationship between GDP per capita and Life Expectancy.")

st.subheader("Correlation Overview")
correlation = np.corrcoef(gdp, life)[0, 1]
st.write(f"**Correlation between GDP and Life Expectancy:** {correlation:.3f}")

# --- Scatter Plot ---
fig, ax = plt.subplots()
ax.scatter(gdp, life, alpha=0.5, color='teal')
ax.set_xlabel("GDP per Capita (USD)")
ax.set_ylabel("Life Expectancy (years)")
ax.set_title("GDP vs Life Expectancy")
st.pyplot(fig)

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit.")