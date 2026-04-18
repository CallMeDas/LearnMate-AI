from langchain_community.document_loaders import WebBaseLoader

url = 'https://docs.mistral.ai/models/model-cards/mistral-small-3-2-25-06'

data = WebBaseLoader(url)
docs = data.load()

print(docs[0].page_content)
