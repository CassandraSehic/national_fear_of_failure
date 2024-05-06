import pandas as pd

# Read the CSV file
gdp_data = pd.read_csv('/workspaces/fof/data/country_gdp.csv')

# Read the SAV file
gem_data = pd.read_spss('/workspaces/fof/data/GEM2018NatData.sav')

# Convert 'country_name' columns to lowercase
gdp_data['country_name'] = gdp_data['country_name'].str.lower()
gem_data['country_name'] = gem_data['country_name'].str.lower()

# Merge the dataframes by 'country_name'
merged_data = pd.merge(gdp_data, gem_data, on='country_name')

# Define the output file path
output_file = '/workspaces/fof/data/mergedata1.csv'

# Write the merged data to the output file
merged_data.to_csv(output_file, index=False)

# Print a success message
print(f"Merged data saved to {output_file}")