import requests
import pandas as pd

url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=a02d6a18858b23e06659a80250f09ab4"

try:
    # Send a GET request to the API
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = response.json()
        print(data)

        # Create a DataFrame from the dictionary
        df = pd.DataFrame(data)

        df.drop(columns=['success', 'timestamp', 'base', 'date'], inplace=True)

        # Now you can work with the DataFrame
        print(df.head())
    else:
        print(f"API request failed with status code {response.status_code}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

csv_filepath = 'exchange_rates_1.csv'
df.to_csv(csv_filepath)