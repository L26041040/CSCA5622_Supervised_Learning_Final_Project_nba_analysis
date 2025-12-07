# NBA Win Prediction (2015–2025)

This project predicts NBA team wins using supervised machine learning models.
The dataset was created by merging 10 seasons of team statistics and standings
from Basketball-Reference.

## Contents
- Data cleaning summary
- Exploratory data analysis (EDA)
- Feature selection
- Model training (Linear Regression, Random Forest, KNN)
- Model comparison and discussion

## How to Run
1. Install requirements: `pip install pandas numpy scikit-learn matplotlib seaborn`
2. Run `nba_analysis.ipynb`

## Dataset
NBA_Stats_Standings_2015_2016_to_2024_2025.csv  
Contains standardized team stats across 10 NBA seasons.

## Results
Random Forest achieved the best prediction performance:
- MSE ≈ 63
- R² ≈ 0.63

## Author
Juichen Hung
