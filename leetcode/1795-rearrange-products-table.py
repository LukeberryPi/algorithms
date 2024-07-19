# https://leetcode.com/problems/rearrange-products-table/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd
import numpy as np

products_data = {
    'product_id': [0, 1],
    'store1': [95, 70],
    'store2': [100, np.nan],
    'store3': [105, 80]
}
products_df = pd.DataFrame(products_data)

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    products = products.melt(id_vars='product_id', var_name='store', value_name='value').dropna(axis=0, how='any').rename(columns={ "value": "price" }).sort_values("product_id")
    products["price"] = products["price"].astype(int)

    return products


print(rearrange_products_table(products_df))