# CORD-19 Data Exploration

## Project Description

This project explores the CORD-19 dataset to analyze COVID-19 research papers. It includes:

* Data cleaning and preprocessing (using our own **cleaned metadata CSV**)
* Analysis of publication trends
* Top journals publishing COVID-19 papers
* Word frequency analysis for paper titles
* Interactive Streamlit application for dynamic exploration

---

## How to Run

### 1. Jupyter Notebook

1. Open `cord19_data_exploration.ipynb` in Jupyter.
2. Run all cells from top to bottom.

### 2. Streamlit App

1. Install dependencies (if not already installed):

```bash
pip install pandas matplotlib streamlit
```

2. Run the app:

```bash
streamlit run app.py
```

3. Your browser will open at `http://localhost:8501`, where you can interactively explore the dataset.

---

## Key Insights (based on our cleaned CSV)

* Total papers analyzed: \~10 (or the number of rows in your CSV)
* Top journals: Nature, Science, The Lancet, Pediatrics, IEEE Transactions
* Publication trends: Most papers published in 2020–2021
* Common words in titles: covid, vaccine, sars, treatment, public, health

---

## Challenges

* Handling missing data in abstracts and journals
* Processing large datasets (your sample is small, full dataset can be slow)
* Visualizing text data (word cloud skipped due to missing package)

