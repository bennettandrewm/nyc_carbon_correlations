


'''
This script is used to download data from the New York State Department of Health's Vital Records website.
It uses the Socrata API to download the data and then converts it to a pandas DataFrame.
'''

# make sure to install these packages before running:

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
app_token = "cjJcv35Bsv74QAApVkZBhY5Wm"
client = Socrata("data.ny.gov", app_token = app_token)

# Example authenticated client (needed for non-public datasets):
# client = Socrata(data.ny.gov,
#                  MyAppToken,
#                  username="user@example.com",
#                  password="AFakePassword")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
tolls = client.get("qzve-kjga")  ## ez_pass bridge and tunnnel
emissions = client.get("wq7q-htne") ## building emissions data
#subway =
#hdd = 
#cdd = 

# Convert to pandas DataFrame
emissions_df = pd.DataFrame.from_records(emissions)

print(emissions_df.head())

#%%
# ... existing imports ...
import requests
from bs4 import BeautifulSoup

# ... existing imports ...

# ... existing imports ...

# ... existing imports ...

def scrape_nyc_degree_days():
    url = "https://www.nyserda.ny.gov/About/Publications/Energy-Analysis-Reports-and-Studies/Weather-Data/Monthly-Cooling-and-Heating-Degree-Day-Data"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    nyc_data = {}

    # Find the "New York City" header
    nyc_header = soup.find('h2', string=lambda text: 'New York City' in text if text else False)
    print("New York City header found:", nyc_header)

    if nyc_header:
        # Find the next two tables after this header
        tables = nyc_header.find_all_next('table', limit=2)
        print("Number of tables found:", len(tables))

        for i, table in enumerate(tables):
            print(f"\nProcessing table {i+1}:")
            
            # Extract headers from the first row
            headers = [th.text.strip() for th in table.find('tr').find_all('th')]
            print("Table headers:", headers)
            print("Number of headers:", len(headers))
            
            # Extract the last row
            rows = table.find_all('tr')
            if len(rows) > 1:  # Ensure there's at least one data row
                last_row = [td.text.strip() for td in rows[-1].find_all('td')]
                last_row = last_row[1:]  # Remove the first element of the last row
                print("Last row:", last_row)
                print("Number of data points:", len(last_row))
                
                # Ensure the number of headers matches the number of data points
                if len(headers) != len(last_row):
                    print("Mismatch between headers and data!")
                    print(f"Headers: {headers}")
                    print(f"Data: {last_row}")
                    # Use the minimum length to create the DataFrame
                    min_length = min(len(headers), len(last_row))
                    headers = headers[:min_length]
                    last_row = last_row[:min_length]
                
                # Create DataFrame with only the header and last row
                df = pd.DataFrame([last_row], columns=headers)
                print("DataFrame created successfully")
                print("DataFrame shape:", df.shape)
                print("DataFrame:")
                print(df)
                
                if i == 0:
                    nyc_data['CDD'] = df
                else:
                    nyc_data['HDD'] = df
            else:
                print("No data rows found in the table.")

    return nyc_data

# Scrape the data
nyc_degree_days = scrape_nyc_degree_days()

# Print the results
if 'CDD' in nyc_degree_days:
    print("\nNew York City Cooling Degree Days:")
    print(nyc_degree_days['CDD'])
else:
    print("Cooling Degree Days data for New York City not found.")

if 'HDD' in nyc_degree_days:
    print("\nNew York City Heating Degree Days:")
    print(nyc_degree_days['HDD'])
else:
    print("Heating Degree Days data for New York City not found.")

# Assign to variables
cdd = nyc_degree_days.get('CDD', pd.DataFrame())
hdd = nyc_degree_days.get('HDD', pd.DataFrame())

# ... rest of your existing code ...