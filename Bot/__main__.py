from agent import CatalogRouter, DSPyProductCatalog
from tools import fetch_category_info,fetch_product_info
import os
import dspy



# agent = dspy.ReAct(
#     DSPyProductCatalog,
#     tools = [
#         fetch_category_info,
#         fetch_product_info
#     ]
# )
print("Configuring the agent with OpenAI GPT-4o-mini...")

# dspy.configure(lm=dspy.LM("openai/gpt-4o-mini"))
lm = dspy.LM(
    model="groq/moonshotai/kimi-k2-instruct"
)
dspy.configure(lm=lm)
# print("Agent initialized. Processing user request...")
# chat_type = dspy.Predict(CatalogRouter)
# result = chat_type(
#     user_request="please send me the category list available"
# )
# print('Chat type prediction completed. Result:')
# print(result.entity_type)

extractor = DSPyProductCatalog()

# extractor = dspy.Predict(DSPyProductCatalog)
result = extractor(
    user_request="fetch product with procuct id ELX-DRG-VIT"
)

# result = agent(user_request="product_list")

print(result)