'''
Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

Example 1:

Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output: 
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
'''
import pandas as pd


def find_customers(customers: pd.DataFrame, 
                   orders: pd.DataFrame
                   ) -> pd.DataFrame:
    df = customers \
                .loc[~customers['id'] \
                        .isin(orders['customerId'])]
    
    names = df[['name']]
    new_df = names.rename(columns={'name' : 'Customers'})

    return new_df