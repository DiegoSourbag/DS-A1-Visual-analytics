import pandas as pd

csv_files_crashes = ['data/stats_crashes_202106_overview.csv', 
                     'data/stats_crashes_202107_overview.csv', 
                     'data/stats_crashes_202108_overview.csv',
                     'data/stats_crashes_202109_overview.csv',
                     'data/stats_crashes_202110_overview.csv',
                     'data/stats_crashes_202111_overview.csv',
                     'data/stats_crashes_202112_overview.csv']

crashes_columns = ['Date', 'Daily Crashes', 'Daily ANRs']

dfs_crashes = [pd.read_csv(file, usecols=crashes_columns, encoding='utf-16') for file in csv_files_crashes]

# Concatenate all DataFrames into one, resetting the index
df_crashes = pd.concat(dfs_crashes, ignore_index=True)

df_crashes['Date'] = pd.to_datetime(df_crashes["Date"], format='%Y-%m-%d')

csv_files_sales_1 = ['data/sales_202106.csv',
                   'data/sales_202107.csv',
                   'data/sales_202108.csv',
                   'data/sales_202109.csv',
                   'data/sales_202110.csv',]

csv_files_sales_2 = ['data/sales_202111.csv',
                   'data/sales_202112.csv']

# List of columns to use
sales_cols_1=['Transaction Date', 'Transaction Type', 'Product id', 'Sku Id', 'Buyer Country', 'Buyer Postal Code', 'Amount (Merchant Currency)']

 # Denk niet of 'Financial Status' hetzelfde is als 'Transaction Type', maar voor nu het meest dichtbij. Twijfel ook over 'Charged Amount' en 'Amount (Merchant Currency)'
sales_cols_2=['Order Charged Date', 'Financial Status','Product ID', 'SKU ID', 'Country of Buyer', 'Postal Code of Buyer', 'Charged Amount']

# Convert to DataFrame
dfs_sales_1 = [pd.read_csv(file, usecols=sales_cols_1, encoding='utf-8') for file in csv_files_sales_1]
dfs_sales_2 = [pd.read_csv(file, usecols=sales_cols_2, encoding='utf-8') for file in csv_files_sales_2]

# Concatenate all DataFrames into one, resetting the index
df_sales_1 = pd.concat(dfs_sales_1, ignore_index=True)
df_sales_2 = pd.concat(dfs_sales_2, ignore_index=True)

# Convert 'Transaction Date' to pd atetime
df_sales_1['Transaction Date'] = pd.to_datetime(df_sales_1['Transaction Date'], format='%b %d, %Y')
df_sales_2['Order Charged Date'] = pd.to_datetime(df_sales_2['Order Charged Date'], format='%Y-%m-%d')

# Rename columns to match
df_sales_2 = df_sales_2.rename(columns={'Order Charged Date': 'Transaction Date',
                                          'Financial Status': 'Transaction Type',
                                          'Product ID': 'Product id',
                                          'SKU ID': 'Sku Id',
                                          'Country of Buyer': 'Buyer Country',
                                          'Postal Code of Buyer': 'Buyer Postal Code',
                                          'Charged Amount': 'Amount (Merchant Currency)'})

# Concatenate both DataFrames
df_sales = pd.concat([df_sales_1, df_sales_2], ignore_index=True)

# Filter the DataFrame
df_sales = df_sales[
    ((df_sales['Transaction Type'] == 'Charge') | (df_sales['Transaction Type'] == 'Charged')) &
    (df_sales['Product id'] == 'com.vansteinengroentjes.apps.ddfive')
      ]

csv_files_ratings = ['data/stats_ratings_202106_country.csv',
                        'data/stats_ratings_202107_country.csv',
                        'data/stats_ratings_202108_country.csv',
                        'data/stats_ratings_202109_country.csv',
                        'data/stats_ratings_202110_country.csv',
                        'data/stats_ratings_202111_country.csv',
                        'data/stats_ratings_202112_country.csv']

ratings_columns = ['Date', 'Country', 'Daily Average Rating', 'Total Average Rating']

dfs_ratings = [pd.read_csv(file, usecols=ratings_columns, encoding='utf-16') for file in csv_files_ratings]

# Concatenate all DataFrames into one, resetting the index
df_ratings = pd.concat(dfs_ratings, ignore_index=True)

df_ratings['Date'] = pd.to_datetime(df_ratings["Date"], format='%Y-%m-%d')

print(df_crashes, df_sales, df_ratings)