import pandas as pd

# The most important part of the Pandas library is the DataFrame. Kinda like an excel sheet, or a table in an SQL DB.

# ------- copy - pasted ---------
# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# print a summary of the data in Melbourne data
melbourne_data.describe()