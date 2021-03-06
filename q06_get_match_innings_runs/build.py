# %load q06_get_match_innings_runs/build.py
# Default Imports
from greyatomlib.pandas_project.q01_read_csv_data_to_df.build import read_csv_data_to_df

# You have been given dataset already in 'ipl_df'.
ipl_df = read_csv_data_to_df('data/ipl_dataset.csv')

# Solution

def get_match_innings_runs():
    ipl1=ipl_df['runs'].groupby([ipl_df['match_code'],ipl_df['inning']]).sum()
    return ipl1





