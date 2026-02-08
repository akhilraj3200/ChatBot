import dspy
from tools import fetch_category_info,fetch_product_info





# category

class CategoryOut(dspy.Signature):
    user_request: str = dspy.InputField()
    category_id: str = dspy.OutputField()
    category_name: str = dspy.OutputField()


# subcategory
class SubCategoryOut(dspy.Signature):
    user_request: str = dspy.InputField()
    sub_category_id: str = dspy.OutputField()
    sub_category_name: str = dspy.OutputField()

# product


class ProductOut(dspy.Signature):
    item_name: str = dspy.InputField()
    item_code: str = dspy.OutputField()


class SKUOut(dspy.Signature):
    user_request: str = dspy.InputField()
    sku_code: str = dspy.OutputField()
    sku_mrp: float = dspy.OutputField()
    same_day_delivery: bool = dspy.OutputField()



class CatalogRouter(dspy.Signature):
    """Decide what catalog entity the user is asking for."""

    user_request: str = dspy.InputField()
    entity_type: str = dspy.OutputField(
        desc="One of: category, subcategory, product, sku"
    )

# class DSPyProductCatalog(dspy.Signature):
#     """You are a product catalog agent that helps user find and manage products.

#     You are given a list of tools to handle user request, and you should decide the right tool to use in order to
#     fulfill users' request."""

#     user_request: str = dspy.InputField()
#     category_id: str = dspy.OutputField()
#     category_name: str = dspy.OutputField()


class DSPyProductCatalog(dspy.Module):
    def __init__(self):
        self.router = dspy.Predict(CatalogRouter)

        self.category = dspy.ReAct(
            CategoryOut,
            tools=[
                fetch_category_info,
            ],
            max_iters=5
        )
        self.subcategory = dspy.ReAct(
            SubCategoryOut,
            tools=[
                fetch_category_info,
            ],
            max_iters=5
        )
        self.product = dspy.ReAct(
            ProductOut,
            tools=[
                fetch_product_info
            ],
            max_iters=5
        )
        self.sku = dspy.ReAct(
            SKUOut,
            tools=[
                fetch_product_info
            ],
            max_iters=5
        )

        self.tools = {
            "get_categories": fetch_category_info,
            "get_products": fetch_product_info
        }

    def forward(self, user_request: str):
        route = self.router(user_request=user_request).entity_type

        if route == "category":
            return self.category(user_request=user_request)

        if route == "subcategory":
            return self.subcategory(user_request=user_request)

        if route == "product":
            return self.product(user_request=user_request)

        if route == "sku":
            return self.sku(user_request=user_request)

        raise ValueError("Unsupported entity type")
