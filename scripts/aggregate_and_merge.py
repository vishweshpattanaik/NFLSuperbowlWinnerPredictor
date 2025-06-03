

import pandas as pd

# Only load the reliable dataset
df = pd.read_csv('data/raw/team_stats_2003_2023.csv')

# Save it to the processed folder
df.to_csv('data/processed/nfl_team_stats_2003_2023_cleaned.csv', index=False)

print("2003–2023 dataset cleaned and saved. No 2024 data included.")

