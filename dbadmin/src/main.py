from src.articles.create_tables import create_and_populate_article_table, create_dataset
from src.customers.create_table import populate_customers_table, create_customers_table, generate_customers

# creation of dataset
create_dataset()

# creating article table and filling in data
create_and_populate_article_table()

create_customers_table()
users = generate_customers(10000)
populate_customers_table(users)