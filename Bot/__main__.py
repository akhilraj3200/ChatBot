from agent import CatalogRouter, DSPyProductCatalog
from tools import fetch_category_info,fetch_product_info
import os
import dspy
# os.environ["OPENAI_API_KEY"] = "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"
os.environ["HUGGINGFACE_API_KEY"] = "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"
os.environ["GROQ_API_KEY"] = "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"
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
    user_request="product_list"
)

# result = agent(user_request="product_list")

print(result.item_code)