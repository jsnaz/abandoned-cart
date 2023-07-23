from typing import List, Dict

from faker import Faker
from google.cloud import bigquery

from src.customers.schema import schema
import random
client = bigquery.Client()

table_id = "abandoned-cart-393615.data.customers"


def create_customers_table():
    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    print("Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id))


def generate_customers(customers_num: int) -> List[Dict]:
    user_list = []
    fake = Faker()
    genders = ["F", "M"]
    for n in range(customers_num):
        customer_data = {
            "first_name": fake.first_name(),
            "last_name":  fake.last_name(),
            "age": random.randint(18,60),
            "id":  fake.uuid4(),
            "gender": random.choice(genders),
            "country": fake.country(),
            "email": fake.email()
         }
        user_list.append(customer_data)
    return user_list

def populate_customers_table(customers: List[Dict]):
    errors = client.insert_rows_json(table_id, customers)  # Make an API request.
    if not errors:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))


