from langchain_community.document_loaders import CSVLoader
from pprint import pprint


import openai
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import settings
import os

os.environ["OPENAI_API_KEY"] = settings.OPENAI

# Document Loaders
loader = CSVLoader(file_path='data/Dayly_mix.csv', encoding='utf-8')
data = loader.load()
data = data[:100]

import openai
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

faiss_index_path = "data/faiss_index"

embeddings = OpenAIEmbeddings()
faiss_index = FAISS.from_documents(data, embeddings)

llm = ChatOpenAI(model="gpt3.5-turbo", temperature=0.2)
embeddings = OpenAIEmbeddings(client=openai.ChatCompletion)

retriever = faiss_index.as_retriever()
pprint(retriever.get_relevant_documents("popular score high"))
# db = FAISS.from_documents(data, embeddings)

# query = "most popularity score"
# docs = db.similarity_search(query)

# print(docs[0].page_content)