# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex2 import step_1, step_2
print("Setup Complete")

import pandas as pd
from IPython.display import display

# ----------- step 1 ----------

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv';

# Fill in the line below to read the file into a variable home_data
home_data = pd.read_csv(iowa_file_path);

# Call line below with no argument to check that you've loaded the data correctly
print("Step 1 result is -");
step_1.check();

# --------- step 2 ----------

# Print summary statistics in next line
display(home_data.describe());

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = 10517

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 10

# Checks your answers
print("Step 2 result is -");
step_2.check();