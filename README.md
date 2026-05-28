# COVID-19 Global Trend Dashboard

An interactive COVID-19 Dashboard built using Python, Streamlit, Pandas, and Plotly.  
This project helps users visualize COVID-19 statistics such as total cases, deaths, and vaccinations for different countries.

---

# 📌 Features

- 🌍 Country-wise COVID-19 analysis
- 📈 Total Cases Visualization
- ☠️ Total Deaths Visualization
- 💉 Vaccination Progress Tracking
- 📊 Interactive Charts using Plotly
- 🧹 Data Cleaning using Pandas
- ⚡ Fast and Interactive Streamlit Dashboard

---

# 🛠️ Technologies Used

- Python
- Pandas
- Streamlit
- Plotly Express
- Matplotlib

---

# 📂 Project Structure

```bash
COVID-19-Dashboard/
│
├── main.py
├── owid-covid-data.csv
├── README.md
└── requirements.txt
```

---

# 📥 Dataset

Dataset used: **Our World in Data COVID-19 Dataset**

Download Dataset:
https://ourworldindata.org/covid-cases

Place the dataset file inside the project folder:

```bash
owid-covid-data.csv
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/COVID-19-Dashboard.git
```

## 2️⃣ Move into Project Folder

```bash
cd COVID-19-Dashboard
```

## 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

```bash
streamlit run main.py
```

The dashboard will automatically open in your browser.

---

# 📊 Dashboard Visualizations

## 📈 Total Cases Line Chart
Displays total COVID-19 cases over time.

## ☠️ Total Deaths Line Chart
Shows total deaths over time.

## 💉 Vaccination Bar Chart
Displays vaccination progress for the selected country.

## 🥧 Pie Chart
Compares total cases and deaths.

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

- Selected important columns
- Removed missing values
- Converted date column to datetime format

```python
df = df.dropna()
df['date'] = pd.to_datetime(df['date'])
```

---

# 📦 Required Libraries

Create a file named `requirements.txt` and add:

```txt
pandas
streamlit
plotly
matplotlib
```

---

# 🚀 Future Improvements

- Add World Map Visualization
- Add Recovery Statistics
- Add Active Cases Tracking
- Improve UI Design
- Add Real-Time Data Updates

---

# 👨‍💻 Author

SANJU AS

BASVARAJ S

---

# 📜 License

This project is created for educational purposes only.

---
