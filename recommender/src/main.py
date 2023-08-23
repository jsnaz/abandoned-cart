from time import sleep

from src.data_fetcher import get_all_articles, get_all_users, retrieve_user_info, get_articles_from_shopping_cart
from src.email_sender import send_email

# 30 mins time interval
SLEEP_INTERVAL_SECONDS = 1800


def get_recommendations(all_articles, cart_articles):
    """
    Make a prediction to return the suggested item the user may want to buy
    :param all_articles: All article from the article table (DataFrame)
    :param cart_articles: Articles corresponding to the articles put in the shopping cart (DataFrame)
    :return: Top 3 suggested products (DataFrame)
    """
    all_articles["score"] = 0

    # Iterate over all the items in the shopping cart and assign a score for each rows of the article table
    for index, cart_row in cart_articles.iterrows():
        all_articles.loc[all_articles["product_type_name"] == cart_row["product_type_name"], "score"] += 1
        all_articles.loc[all_articles["colour_group_name"] == cart_row["colour_group_name"], "score"] += 1
        all_articles.loc[all_articles["product_group_name"] == cart_row["product_group_name"], "score"] += 1
        all_articles.loc[all_articles["garment_group_name"] == cart_row["garment_group_name"], "score"] += 1

    # Get rid of the articles having the same article_id as the ones in the shopping cart
    cart_ids = list(cart_articles["article_id"].values)
    recommendable_articles = all_articles[~all_articles["article_id"].isin(cart_ids)]
    # Sorting by score and print the 3 best recommendations
    top_3_reco = recommendable_articles.sort_values(by=["score"], ascending=False).head(3)

    # Return the recommendations as a Python dictionary
    return top_3_reco.to_dict(orient="records")


def run(user_id, cart_products_ids, all_articles):
    """
    Run the recommendation service and send the recommendations to the customer's email
    :param user_id: user id (string)
    :param cart_products_ids: ids of the products from the cart (list of integer)
    :param all_articles: all article data (Pandas DataFrame)
    :return:
    """

    user_info = retrieve_user_info(user_id)
    print(f"The info of the user {user_id} has been retrieved")

    cart_articles = get_articles_from_shopping_cart(cart_products_ids)
    print("The info of his shopping cart articles has been retrieved")

    recommendations = get_recommendations(all_articles, cart_articles)
    print("The recommendations has been calculated")

    send_email(user_info, cart_articles.to_dict(orient="records"), recommendations)
    print("The email has been sent to the customer")


def get_random_user(all_users):
    """
    Get a random user id from all the users
    :param all_users: data from the users table (Pandas DataFrame)
    :return: user id (string)
    """
    random_user = all_users.sample()
    return random_user["id"].values[0]


def get_random_articles(all_articles):
    """
    Get a list of random product id representing an abandoned cart
    :param all_articles: data from the articles table (Pandas DataFrame)
    :return: List of ids (List of integer)
    """
    random_articles = all_articles.sample(3)
    return list(random_articles["article_id"])


all_articles = get_all_articles()
print("The info of all the articles has been retrieved")
all_users = get_all_users()
print("The info of all the users has been retrieved")

while True:
    random_articles_ids = get_random_articles(all_articles)
    print(f"Products randomly chosen: {random_articles_ids}")

    random_user_id = get_random_user(all_users)
    print(f"User randomly chosen: {random_user_id}")

    run(random_user_id, random_articles_ids, all_articles)

    sleep(SLEEP_INTERVAL_SECONDS)
