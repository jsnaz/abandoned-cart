from google.cloud import bigquery

PROJECT = "abandoned-cart-393615"
# Create a BigQuery client
client = bigquery.Client()


def get_image_path(article_id):
    """
    Make the image path stored in Google Cloud Storage from the article id
    :param article_id: article id (integer)
    :return: image path (string)
    """
    bucket_name = 'abandoned-cart-raw-data'
    base_folder = 'articles_image'
    article_id_str = str(article_id)
    article_id_padded = article_id_str.zfill(10)
    folder_path = article_id_padded[:3]
    image_filename = article_id_padded + '.jpg'
    image_path = f'{base_folder}/{folder_path}/{image_filename}'
    image_public_url = f"https://storage.googleapis.com/{bucket_name}/{image_path}"
    return image_public_url


def get_all_articles():
    """
    Gets data from the articles table
    :return: Dataframe
    """
    query = f"""
        SELECT *
        FROM `{PROJECT}.data.articles`
    """
    all_articles = client.query(query).to_dataframe()
    # Add a new column containing the image path of the article
    all_articles["url"] = all_articles["article_id"].apply(lambda article_id: get_image_path(article_id))
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
         FROM `{PROJECT}.data.articles`
         WHERE article_id IN ({str_article_ids})
     """
    cart_articles = client.query(query).to_dataframe()
    # Add a new column containing the image path of the article
    cart_articles["url"] = cart_articles["article_id"].apply(lambda article_id: get_image_path(article_id))
    return cart_articles


def get_all_users():
    """
    Gets data from the articles table
    :return: Dataframe
    """
    query = f"""
        SELECT *
        FROM `{PROJECT}.data.customers`
    """
    all_users = client.query(query).to_dataframe()
    return all_users


def retrieve_user_info(user_id):
    query = f'''
        SELECT 
            first_name, 
            last_name,
            gender,
            email
        FROM `{PROJECT}.data.customers`
        WHERE id = "{user_id}"'''
    user_info = client.query(query).to_dataframe().iloc[0]
    # to save client data to dictionary instead of series type
    return {"firstname": user_info["first_name"], "lastname": user_info["last_name"], "gender": user_info["gender"],
            "email": user_info["email"]}
