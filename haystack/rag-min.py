from haystack.document_stores import InMemoryDocumentStore
from haystack.utils import build_pipeline, add_example_data, print_answers

# We are model agnostic :) Here, you can choose from: "anthropic", "cohere", "huggingface", and "openai".
provider = "openai"
API_KEY = "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" # ADD YOUR KEY HERE

# We support many different databases. Here we load a simple and lightweight in-memory database.
document_store = InMemoryDocumentStore(use_bm25=True)

# Download and add Game of Thrones TXT articles to Haystack DocumentStore.
# You can also provide a folder with your local documents.
add_example_data(document_store, "./data/ifaal")

# Build a pipeline with a Retriever to get relevant documents to the query and a PromptNode interacting with LLMs using a custom prompt.
pipeline = build_pipeline(provider, API_KEY, document_store)

# Ask a question on the data you just added.
result = pipeline.run(query="que propose artissimo ?")

# For details, like which documents were used to generate the answer, look into the <result> object
print_answers(result, details="medium")
