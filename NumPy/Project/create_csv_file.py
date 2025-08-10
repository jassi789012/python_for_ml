import pandas as pd
import numpy as np

# The initial, small dataset directly from the video's examples of problematic data
initial_data = {
    'Employee ID': [101, 102, 103, 104, 105, 101, 106, 107, 108, 109, 110],
    'Name': ['Amit Sharma', 'Ria', 'Sunil Kumar', 'Neha Kapoor', 'Pooja Sharma', 'Amit Sharma', 'Pankaj Mishra', 'Vinod', 'Deepika Reddy', 'Rajesh Gupta', 'Manoj Singh'],
    'Age': [30, 25, 35, 28, 32, 30, 40, 33, 29, 38, 45],
    'Salary': [50000, np.nan, 60000, np.nan, np.nan, 50000, -20000, 5000000, 3000000, 75000, 90000],
    'Experience': [5, 2, 10, 3, 7, 5, 15, 8, 4, 12, 20],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Chennai', 'Hyderabad', 'Delhi', 'Kolkata', 'Pune', 'Hyderabad', 'Bangalore', 'Mumbai'],
    'Department': ['Sales', 'Marketing', 'IT', 'HR', 'Finance', 'Sales', 'Operations', 'IT', 'Marketing', 'Finance', 'Sales'],
    'Performance Rating': [4, 3, np.nan, 5, 4, 4, 3, 5, 4, 3, 5]
}

# Add the infinite value as mentioned in the video to an example row
# For simplicity, let's ensure one of the salaries from initial_data is inf
# If 75000 (index 9) was an original value, let's make it inf for demonstration
initial_df = pd.DataFrame(initial_data)
initial_df.loc[9, 'Salary'] = np.inf # Rajesh Gupta's salary will now be infinity

# Define the target number of rows
target_rows = 1000
num_initial_rows = len(initial_df)

# Calculate how many times to repeat the initial dataset
repetitions = target_rows // num_initial_rows
remainder = target_rows % num_initial_rows

# Create the larger DataFrame by repeating the initial one
df = pd.concat([initial_df] * repetitions + [initial_df.head(remainder)], ignore_index=True)

# Important: Employee ID needs to be unique if the video expects unique IDs after cleaning.
# We will regenerate unique IDs, but keep the duplicates in the 'Employee ID' column for demonstration
# of how the video handles finding duplicates based on the initial '101' duplicate.
# For the purpose of making it "similar as it can be", we will keep the pattern of duplicates
# from the initial_df. This means there will be many occurrences of the '101' duplicate pattern.

# Save the DataFrame to a CSV file
file_name = 'Indian_employees_data.csv'
df.to_csv(file_name, index=False)

print(f"File '{file_name}' created successfully with {len(df)} rows.")
print("\nFirst few rows of the created DataFrame (should resemble video's initial data):")
print(df.head(15)) # Show more rows to demonstrate the repetition
print(f"\nDataFrame shape: {df.shape}")

print("\nVerifying presence of specific problematic entries:")
print(f"Number of NaN salaries: {df['Salary'].isna().sum()}")
print(f"Number of negative salaries: {(df['Salary'] < 0).sum()}")
print(f"Number of infinite salaries: {(df['Salary'] == np.inf).sum()}")
print(f"Number of duplicate Employee IDs (based on ID only): {df['Employee ID'].duplicated().sum()}")
print(f"Number of NaN performance ratings: {df['Performance Rating'].isna().sum()}")