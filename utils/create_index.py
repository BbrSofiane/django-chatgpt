import os

from dotenv import load_dotenv
from llama_index import GPTVectorStoreIndex
from llama_index import SimpleWebPageReader

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

reader = SimpleWebPageReader(html_to_text=True)

documents = reader.load_data(
    urls=["https://testdriven.io/blog/django-custom-user-model/"]
)

index = GPTVectorStoreIndex.from_documents(documents)

index.set_index_id("django_custom_user_model.json")
index.storage_context.persist("data")
