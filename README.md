# Biodiesel Yield Dataset

This repository contains the biodiesel yield dataset along with a Python script for data preprocessing. The data is intended for analysis and research purposes related to biodiesel production and yield.

## Repository Contents

- **Gnanprakash dataset.csv**  
  The raw dataset file containing biodiesel yield data.
- **preprocessing.py**  
  A Python script that demonstrates basic data preprocessing steps:
  - Removing duplicate rows
  - Handling missing values (using column mean for numerical data and mode for categorical data)
  - Encoding categorical variables (via one-hot encoding)
  - Saving the processed data as a new CSV file (`biodieselyield.csv`)

## Prerequisites

- **Python 3.x**  
- **Pandas Library**  
  Install via pip if not already installed:
  ```bash
  pip install pandas

