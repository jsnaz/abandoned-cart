from google.cloud import bigquery

schema = [
    bigquery.SchemaField("article_id", "INTEGER"),
    bigquery.SchemaField("product_code", "INTEGER"),
    bigquery.SchemaField("prod_name", "STRING"),
    bigquery.SchemaField("product_type_no", "INTEGER"),
    bigquery.SchemaField("product_type_name", "STRING"),
    bigquery.SchemaField("product_group_name", "STRING"),
    bigquery.SchemaField("graphical_appearance_no", "INTEGER"),
    bigquery.SchemaField("graphical_appearance_name", "STRING"),
    bigquery.SchemaField("colour_group_code", "INTEGER"),
    bigquery.SchemaField("colour_group_name", "STRING"),
    bigquery.SchemaField("perceived_colour_value_id", "INTEGER"),
    bigquery.SchemaField("perceived_colour_value_name", "STRING"),
    bigquery.SchemaField("perceived_colour_master_id", "INTEGER"),
    bigquery.SchemaField("perceived_colour_master_name", "STRING"),
    bigquery.SchemaField("department_no", "INTEGER"),
    bigquery.SchemaField("department_name", "STRING"),
    bigquery.SchemaField("index_code", "STRING"),
    bigquery.SchemaField("index_name", "STRING"),
    bigquery.SchemaField("index_group_no", "INTEGER"),
    bigquery.SchemaField("index_group_name", "STRING"),
    bigquery.SchemaField("section_no", "INTEGER"),
    bigquery.SchemaField("section_name", "STRING"),
    bigquery.SchemaField("garment_group_no", "INTEGER"),
    bigquery.SchemaField("garment_group_name", "STRING"),
    bigquery.SchemaField("detail_desc", "STRING")
    ]