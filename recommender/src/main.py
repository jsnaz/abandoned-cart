from google.cloud import bigquery

# Create a BigQuery client
client = bigquery.Client()


def get_all_articles():
    """
    Gets data from the articles table
    :return: Dataframe
    """
    query = """
        SELECT *
        FROM `abandoned-cart-393615.data.articles`
    """
    all_articles = client.query(query).to_dataframe()
    return all_articles


def get_articles_from_shopping_cart(article_ids):
    """
    Gets data from BigQuery for the given article ids
    :param article_ids: List of integer
    :return: DataFrame
    """
    str_articles_list = [str(id) for id in article_ids]
    str_article_ids = ",".join(str_articles_list)
    query = f"""
         SELECT *
         FROM `abandoned-cart-393615.data.articles`
         WHERE article_id IN ({str_article_ids})
     """
    all_articles = client.query(query).to_dataframe()
    return all_articles


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
    return top_3_reco


test_ids = [448831026, 510264001, 566941026]
all_articles = get_all_articles()
cart_articles = get_articles_from_shopping_cart(test_ids)
recommendations = get_recommendations(all_articles, cart_articles)
print(recommendations)
