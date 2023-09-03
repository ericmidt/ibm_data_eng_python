import glob
import pandas as pd
from datetime import datetime

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process)
    return dataframe

columns=['Name','Market Cap (US$ Billion)']

def extract():
    # Write your code here
    json_file = glob.glob('bank_market_cap_1.json')
    df = pd.DataFrame(extract_from_json(json_file[0]), columns=columns)
    return df


market_cap_df = extract()
print(market_cap_df.head())

# Write your code here
df_rates = pd.read_csv('exchange_rates.csv', index_col=0)
exchange_rate = df_rates.loc['GBP', 'Rates']
print(exchange_rate)


def transform(exchange_rate, df):
    df['Market Cap (US$ Billion)'] = df['Market Cap (US$ Billion)']*exchange_rate
    df['Market Cap (US$ Billion)'] = df['Market Cap (US$ Billion)'].round(3)
    df.rename(columns={'Market Cap (US$ Billion)': 'Market Cap (GBP$ Billion)'}, inplace=True)


def load(dataframe):
    dataframe.to_csv('bank_market_cap_gbp.csv', index=False)


def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second
    now = datetime.now() # get current timestamp
    timestamp = now.strftime(timestamp_format)
    with open("logfile.txt","a") as f:
        f.write(timestamp + ',' + message + '\n')

# Write your code here
log("ETL Job Started")