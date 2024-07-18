# https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_customers(customers, orders):
    customers_that_never_bought = customers[~customers["id"].isin(orders["customerId"])]
    return customers_that_never_bought[["name"]].rename(columns={"name": "Customers"})

