## Write a program that retrieves the dataset for the "exchequer account (historical series)" 
## from the CSO, and stores it into a file called "cso.json"

import requests
import pandas as pd
from io import StringIO

## I used these two links as the basis for below -
## https://stackoverflow.com/questions/32400867/pandas-read-csv-from-url

# URL of the CSV file
csv_url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/CSV/1.0/"

# Sends get request to get URL
response = requests.get(csv_url)

if response.status_code == 200:
    # Read the CSV data into DataFrame
    df = pd.read_csv(StringIO(response.text))
    
    # Convert the DataFrame to JSON and save it to a file
    json_data = df.to_json(orient='records')
    #I used this link to determine best way to store data - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html

    with open("cso.json", "w") as json_file:
        json_file.write(json_data)

    print("Data has been saved as 'cso.json'")
else:
    print("Failed to retrieve data.")
