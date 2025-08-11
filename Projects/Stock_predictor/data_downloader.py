# Step 2: Download the Stock Data (Corrected Version)

import nasdaqdatalink
import pandas as pd

# --- Paste your new API Key here ---
nasdaqdatalink.ApiConfig.api_key = 'PF2zHvDxQza5y1BNB7uQ' # <--- PASTE YOUR KEY HERE

print("Downloading stock data with the updated code...")

try:
    # We are using the NEW, correct dataset code: NSE/TATACONSUM
    data = nasdaqdatalink.get('NSE/TATACONSUM', start_date='2010-01-01', end_date='2020-01-01')

    # Save the data to a file
    data.to_csv('stock_data.csv')

    print("\nSuccess! Data was downloaded and saved as 'stock_data.csv'")

except Exception as e:
    # This will print any new errors that might happen
    print("\nAn error occurred:")
    print(e)