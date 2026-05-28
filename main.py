import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

url = "owid-covid-data.csv"
covid_df = pd.read_csv(url)

# Selecting important columns
covid_df = covid_df[[
    'location',
    'date',
    'total_cases',
    'new_cases',
    'total_deaths',
    'people_vaccinated'
]]

# Removing missing values
covid_df = covid_df.dropna()

# Convert date column
covid_df['date'] = pd.to_datetime(covid_df['date'])

print(covid_df.info())

import pandas as pd
import plotly.express as px
import streamlit as st

# Page title
st.title("COVID-19 Global Trend Dashboard")

# Load data
url = "owid-covid-data.csv"
df = pd.read_csv(url)

# Select required columns
columns = [
    'location',
    'date',
    'total_cases',
    'new_cases',
    'total_deaths',
    'people_vaccinated'
]

# Data cleaning
df = df[columns]
df = df.dropna()
df['date'] = pd.to_datetime(df['date'])

# Sidebar filter
country = st.sidebar.selectbox(
    "Select Country",
    sorted(df['location'].unique())
)

# Filter data
country_df = df[df['location'] == country]

# Line Chart - Total Cases
fig1 = px.line(
    country_df,
    x='date',
    y='total_cases',
    title=f'Total COVID-19 Cases in {country}'
)

st.plotly_chart(fig1)

# Line Chart - Deaths
fig2 = px.line(
    country_df,
    x='date',
    y='total_deaths',
    title=f'Total Deaths in {country}'
)

st.plotly_chart(fig2)

# Vaccination Chart
fig3 = px.bar(
    country_df,
    x='date',
    y='people_vaccinated',
    title=f'Vaccination Progress in {country}'
)

st.plotly_chart(fig3)

# Pie Chart
latest = country_df.iloc[-1]

pie_data = {
    'Category': ['Cases', 'Deaths'],
    'Count': [latest['total_cases'], latest['total_deaths']]
}

pie_df = pd.DataFrame(pie_data)

fig4 = px.pie(st.write(f"People Vaccinated: {int(latest['people_vaccinated'])}"))