from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

#Load PDF
data = PyPDFLoader('document/deeplearning.pdf')
docs = data.load()

#Spiltter
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

#Chunks
chunks  = splitter.split_documents(docs)

#Embeddigns Model
embeddings_model =  MistralAIEmbeddings()

#Store in Chroma DB. 
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings_model,
    persist_directory='chroma_db'
)
