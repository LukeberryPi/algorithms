# https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

orders_data = {
    'order_number': [1, 2, 3, 4],
    'customer_number': [1, 2, 3, 3]
}

orders_df = pd.DataFrame(orders_data)

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    most_common_customer = orders['customer_number'].mode()

    if most_common_customer.empty:
        return pd.DataFrame(columns=['customer_number'])

    return orders[orders['customer_number'] == most_common_customer[0]].drop_duplicates(subset='customer_number')[["customer_number"]]

print(largest_orders(orders_df))