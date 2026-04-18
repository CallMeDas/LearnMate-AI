from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter


load_dotenv()

embeddings = MistralAIEmbeddings(model="mistral-embed")
data = PyPDFLoader('document/deeplearning.pdf')
docs = data.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

chunks  = splitter.split_documents(docs)


template = ChatPromptTemplate([
    ("system", "You are an AI that summarizes text clearly and concisely."),
    ("human", "{data}")
])


model = ChatMistralAI(model= 'mistral-small-2506')


prompt = template.format_messages(data = chunks[0].page_content)

result = model.invoke(prompt)

print(result.content) 