import random
import string
from dummy import database_category, database_product


def fetch_category_info(database_category=database_category):
    print(("Fetching category information from the database..."))
    """Fetch category information """
    categories = []

    # for category in database_category:
    categories.append({"category_name": database_category.category_name, "category_id": database_category.category_id})
    if len(categories) == 0:
        raise ValueError("No categories found")
    return categories


def fetch_product_info(database_product=database_product):
    print(("Fetching product list information from the database..."))
    print(database_product)
    """Fetch product list information"""
    products = []
    # for product in database_product:
    products.append({"item_name": database_product.item_name, "item_code": database_product.item_code})
    print(products)
    if len(products) == 0:
        raise ValueError(f"No products found for category id {category_id}")
    return products

