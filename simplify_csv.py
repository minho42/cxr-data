import pandas as pd

# Read the original CSV file
df = pd.read_csv('data.csv')

# Filter out rows where 'Finding Labels' is 'No Finding'
df_filtered = df[df['Finding Labels'] != 'No Finding']

# Select the relevant columns and rename them
df_filtered = df_filtered[['Image Index', 'Finding Labels', 'Patient Age', 'Patient Gender', 'View Position']]
df_filtered.columns = ['name', 'label', 'age', 'gender', 'position']

# Change the file extension from .png to .jpg in the 'name' column
df_filtered['name'] = df_filtered['name'].str.replace('.png', '.jpg')

# Save the modified data to a new CSV file
df_filtered.to_csv('data2.csv', index=False)
