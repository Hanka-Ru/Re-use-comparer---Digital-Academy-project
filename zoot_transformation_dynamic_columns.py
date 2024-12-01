'''Zoot trasnformation solving the dynamical columns with sizes"

import pandas as pd
import uuid

input_path = 'in/tables/Zoot_Mango_kalhoty.csv'
output_path = 'out/tables/Zoot_Mango_kalhoty_vystup.csv'

dataset = pd.read_csv(input_path)

# constants
brand_name = 'Mango'
condition = 'Nový s visačkou'
category = 'Ženy'
product = 'Kalhoty'
e_shop = 'Zoot'

# Identify all size columns dynamically
size_columns = [col for col in dataset.columns if col.startswith('sizes_') and col.endswith('_size')]

# Melt the DataFrame to bring all sizes under a single "size" column
df_size = dataset.melt(id_vars=['name', 'url', 'currentBestPrice_value'],
                       value_vars=size_columns,
                       var_name='size_type',
                       value_name='size')

# Drop rows - size is NaN
df_size = df_size.dropna(subset=['size'])

# Add the new columns with fixed values
df_size['brand_name'] = brand_name
df_size['condition'] = condition
df_size['category'] = category
df_size['product'] = product
df_size['e_shop'] = e_shop  # New column with fixed value 'Zoot'

# Generate a unique database_id for each unique 'url'
url_to_uuid = {url: str(uuid.uuid4()) for url in df_size['url'].unique()}
df_size['database_id'] = df_size['url'].map(url_to_uuid)

# Rename 'currentBestPrice_value' to 'price'
df_size = df_size.rename(columns={'currentBestPrice_value': 'price'})

# Select and rename final columns
df_final = df_size[['database_id', 'name', 'url', 'brand_name', 'price', 'condition', 'category', 'size', 'product', 'e_shop']]

# Set the data types
df_final = df_final.astype({
    'database_id': 'string',
    'name': 'string',
    'url': 'string',
    'brand_name': 'string',
    'price': 'float',
    'condition': 'string',
    'category': 'string',
    'size': 'string',
    'product': 'string',
    'e_shop': 'string'
})

# Drop duplicate rows based on relevant columns
df_final = df_final.drop_duplicates(subset=['database_id', 'name', 'url', 'brand_name', 'price', 'condition', 'category', 'size', 'product', 'e_shop'])

# Final output
df_final.to_csv(output_path, index=False)
