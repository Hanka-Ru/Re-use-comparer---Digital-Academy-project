'''Revised script for transformation of Vinted.cz products. Without PL origin'''

import pandas as pd
import uuid

input_path = 'in/tables/Vinted_mango_kalhoty_zeny.csv'
output_path = 'out/tables/vinted_mango_kalhoty_zeny_vystup.csv'

# Define data types
dtype = {
    "brand_title": str,
    "favourite_count": str,
    "id": str,  # Original column "id" to be renamed as "product_id"
    "size_title": str,
 		"total_item_price_amount": float,
    "status": str,
    "title": str,
    "url": str,
  	}

df = pd.read_csv(input_path, dtype=dtype)

# Rename columns
df = df.rename(columns={
    "id": "product_id",
    "size_title": "size",
    "status": "condition",
    "title": "name",
 		"total_item_price_amount": "price"
})

# Filter to include only rows with women's sizes
# Exclude sizes containing "měsíců", "roky", or numeric age-related sizes like "9 let"
df = df[~df['size'].str.contains(r'\d+\s?(let|měsíců|roky)', na=False, case=False)]

# Adding new columns
df['brand_title'] = 'Mango'
df['category'] = 'Ženy'
df['product'] = 'Kalhoty'
df['e_shop'] = 'Vinted'

# Generating a unique UUID for each row in a new column "database_id"
df['database_id'] = [str(uuid.uuid4()) for _ in range(len(df))]

# Define the final columns
final_columns = [
    "brand_title", "favourite_count", "product_id",
    "price", "size", "condition", "name", "url", "category", "product",
    "e_shop", "delivery_from", "database_id"
]

# Select only columns that exist in the DataFrame
existing_columns = [col for col in final_columns if col in df.columns]
df = df[existing_columns]

# Final output
df.to_csv(output_path, index=False)
