from langchain_community.document_loaders import CSVLoader
from pprint import pprint

import openai
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import settings
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

os.environ["OPENAI_API_KEY"] = settings.OPENAI

# Document Loaders
loader = CSVLoader(file_path='data/myplaylist.csv', encoding='utf-8')
data = loader.load()
data = data[:100]

faiss_index_path = "data/faiss_index"

embeddings = OpenAIEmbeddings()
faiss_index = FAISS.from_documents(data, embeddings)
# model="gpt-4-0125-preview",
llm = ChatOpenAI(temperature=1)
embeddings = OpenAIEmbeddings(client=openai.ChatCompletion)

retriever = faiss_index.as_retriever(k=30)

# Llama2プロンプトテンプレート
template = """<s>[INST] <<SYS>>
あなたは誠実で優秀な日本人のアシスタントです。前提条件の情報を用いて回答してください。
パラメータをそのまま回答することは禁止します。パラメータの説明を以下に提示するので、それに基づいて楽曲の特徴を説明してください。
どの様な基準で楽曲を選んだのか最初に教えてください。

パラメータの説明
acousticness	曲がアコースティックである確率を0.0から1.0で表したもの。1.0は曲がアコースティックである確率が高いことを示す。
danceability	曲がダンスに適しているかを0.0から1.0で表したもの。この値はテンポ、リズムの安定性、ビートの強さなどから計算され、1.0は曲がダンスに非常に適していることを示す。
energy	曲がエネルギッシュである程度を0.0から1.0で表したもの。この値は活動的な音、速いテンポ、騒々しさなどから計算され、1.0は曲が非常にエネルギッシュであることを示す。
instrumentalness	曲がインストゥルメンタルである確率を0.0から1.0で表したもの。1.0は曲がインストゥルメンタル（つまり、ボーカルなし）である確率が高いことを示す。
liveness	曲がライブで演奏されている確率を0.0から1.0で表したもの。1.0は曲がライブで演奏されている確率が高いことを示す。
loudness	曲の全体的な音の大きさをデシベルで表したもの。この値は曲全体にわたって平均化され、値は約-60から0dbまでの範囲である。
speechiness	曲に話し言葉が含まれている確率を0.0から1.0で表したもの。1.0は曲が話し言葉で構成されている確率が高いことを示す。
valence	曲が陽性の感情（例えば、幸せ、楽観的、陽気）を伝える確率を0.0から1.0で表したもの。1.0は曲が陽性の感情を強く伝えることを示す。
tempo	曲の全体的な推定テンポをBPM（ビート・パー・ミニット）で表したもの。
key	曲の全体的なキー（音階）を示す整数。この値はピッチクラス表記法によるもので、0 = C, 1 = C#/Db, 2 = D, と続く。
mode	曲のモード（主音がメジャーかマイナーか）を示す整数。1はメジャー、0はマイナーを示す。
time_signature	曲の拍子記号（1小節あたりの拍数）を示す整数。
<</SYS>>

前提条件：{context}

質問：{question} [/INST]"""

# LangChain LCELでチェインを構築
prompt = ChatPromptTemplate.from_template(template)
output_parser = StrOutputParser()
setup_and_retrieval = RunnableParallel(
    {"context": retriever, "question": RunnablePassthrough()}
)
chain = setup_and_retrieval | prompt | llm | output_parser

# チェインを起動して、回答をストリーミング出力
for s in chain.stream("自然を感じられる曲を3曲お勧めしてください"):
    print(s, end="", flush=True)
