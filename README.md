JEE Admission Decision Support System
A data-driven system that analyzes historical JoSAA cutoff data to estimate admission probability and recommend optimal college–branch combinations based on a student’s JEE rank and preferences.

Overview
Choosing the right college and branch during JoSAA counselling can be confusing due to varying cutoffs, quotas, and categories.
This project simplifies the process by:
Estimating probability of admission into a preferred college–branch
Recommending the best possible college–branch option based on user inputs
Providing data-backed insights using historical trends (2020–2025)

Features
🔹 Admission probability classification:
Very High / Safe / Risky / Very Risky
🔹 Personalized recommendations based on:
JEE Rank (Main / Advanced)
Category & Gender
Home State vs All India Quota
Preferred Branch & College
🔹 Statistical modeling using:
Mean, Median, Standard Deviation
Safe rank interval (Median ± Std Dev)
🔹 Interactive interface for user input
🔹 Data visualization dashboard (Power BI)

Tech Stack
Python (Core Logic)
Pandas, NumPy (Data Processing & Analysis)
Tkinter / Streamlit (User Interface)
Power BI (Data Visualization & Insights)

Dataset
Source: Official JoSAA cutoff data (2020–2025)
Includes: IITs, NITs, IIITs
Cleaned and structured into:
JEE Main dataset
JEE Advanced dataset

Methodology
1. Data Collection & Cleaning
Extracted yearly cutoff data into structured format
Removed invalid entries (e.g., ranks with suffix “P”)
Separated datasets for JEE Main and JEE Advanced
2. Data Transformation
Merged yearly data into master datasets
Retained consistent programs across years
Added state mapping for quota handling
3. Feature Engineering
Computed:
Mean Rank
Median Rank
Standard Deviation
Derived:
Lower Limit = Median − Std Dev
Upper Limit = Median + Std Dev
4. Prediction Logic
Match user inputs with dataset filters
Compare user rank with safe interval:
Rank < Lower Limit → Very High Chance
Within Range → Safe
Above Range → Risk Levels based on deviation
5. Recommendation System
Suggests best college–branch combination
Based on:
Matching constraints
Lowest feasible upper limit

Output
Admission Probability
Risk classification for chosen college–branch
Best Recommendation
Optimal college with preferred branch

Dashboard (Power BI)
Provides insights such as:
Cutoff trends over years
Variability across institutes and branches
Impact of quota, category, and gender
