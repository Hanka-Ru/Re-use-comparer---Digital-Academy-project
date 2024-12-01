'''Zalando transformation of input data, solves dynamical columns at sizes'''

import csv
import uuid

input_file = 'in/tables/Zalando_mango_kalhoty_muzi.csv'
output_file = 'out/tables/Zalando_mango_kalhoty_muzi_vystup.csv'

with open(input_file, mode='r', encoding='utf-8') as infile, open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)

    # Header for output file
    writer.writerow(["database_id", "name", "url", "brand_name", "price", "size", "condition", "category", "product", "e_shop"])

    # Filters for  "Mango" or "Mango Kids"
    filtered_data = [row for row in reader if "mango" in row["brand_name"].lower()]

    for row in filtered_data:
        name = str(row["name"])
        url = str(row["url"])
        price_current = float(row["price_current"])

        # Value for size
        sizes = [key for key in row.keys() if key.startswith("sizes_") and key.endswith("_size")]

        # Checking of availibility
        for size_column in sizes:
            stock_status_column = size_column.replace("_size", "_stockStatus")
            size = str(row.get(size_column, "")).strip()  # Získání velikosti a odstranění případných bílých znaků
            stock_status = row.get(stock_status_column, "").strip().upper()  # Kontrola dostupnosti

            # Condition for available size only
            if size and stock_status != 'OUT_OF_STOCK':
                # Vytvoření jedinečného ID pro kombinaci produktu a velikosti
                database_id = str(uuid.uuid4())
                brand_name = "Mango"
                condition = "Nový s visačkou"  # Přejmenováno na "condition"
                category = "Muži"            # Překlad na "category"
                product = "Kalhoty"           # Překlad na "product"
                e_shop = "Zalando"          # Přidaný nový sloupec s názvem "e-shop"

                # Final output
                writer.writerow([
                    database_id, name, url, brand_name, price_current,
                    size, condition, category, product, e_shop
                ])
