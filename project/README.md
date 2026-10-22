# HW1: Data Analysis Basics

## Process

I downloaded the Fremont Bridge bicycle count CSV from Seattle Open Data and saved it as `data/bicycle_data.csv`. I created `analysis/hw1.ipynb` in JupyterLab and used pandas to read and inspect the data.

I converted the Date column to datetime and the count columns to nullable integers. I added columns for the East + West total, hour, and year, then created a separate dataframe containing the 2016 records.

I found 30 rows with missing total counts and excluded them from the analysis. No hourly timestamps were absent within the recorded date range. Using valid records from all years, I calculated the mean total count for each hour, plotted the results with matplotlib, and used `idxmax()` to identify the busiest hour: 17:00, averaging approximately 349.21 bicycles.

## Running the notebook

The notebook uses pandas and matplotlib. Download the CSV from https://data.seattle.gov/api/views/65db-xm6k/rows.csv and save it as `project/data/bicycle_data.csv` relative to the repository root. Open `project/analysis/hw1.ipynb` and run the cells from top to bottom.

The data directory is excluded from Git using `.gitignore`.