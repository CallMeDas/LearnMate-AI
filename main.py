
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI, MistralAIEmbeddings
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma


load_dotenv()

embedding_model = MistralAIEmbeddings(model="mistral-embed")

vectorstore = Chroma(
    persist_directory='chroma_db',
    embedding_function=embedding_model
)

retriever = vectorstore.as_retriever(
    search_type = 'mmr',
    search_kwargs = {
        'k': 4,
        'fetch_k': 10,
        'lambda_mult': 0.5
    }
)

llm = ChatMistralAI(model='mistral-small-latest')


#Prompt Templete
prompt = ChatPromptTemplate.from_messages([
    ('system', 
     ''' You are an AI assistant.
     Use Only the provideed context to answer the questions.
     If the answer is not present in the context,
     say: I coulnot find the answer in the Documents.'''),
     ('human', 
      '''Context {context}
      Questions: {question}'''
      )
])

print('RAG System')
print('Press 0 to exit.')

while True:
    query = input('Your: ')
    if query =='0':
        break
    print("1. Before retrieval")
    docs = retriever.invoke(query)
    print("2. After retrieval")
    context = "\n\n".join([doc.page_content for doc in docs])
    print("Context:", context)

    final_prompt = prompt.invoke({ "context": context, "question": query})
    response = llm.invoke(final_prompt)

    print(f"\n {response.content}")

