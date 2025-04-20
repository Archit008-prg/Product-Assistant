import os
from dotenv import load_dotenv

load_dotenv()

PRODUCT_BRAND = "Samsung"
PRODUCT_CATEGORIES = [
    "Smartphones", "Televisions", "Refrigerators",
    "Washing Machines", "Laptops", "Air Conditioners"
]

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL_NAME = "models/gemini-1.5-pro-latest"
TEMPERATURE = 0.3
