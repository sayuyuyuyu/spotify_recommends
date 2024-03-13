from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

from tools.sql import run_query_tool, list_tables, describe_tables_tool
from tools.report import write_report_tool
from handlers.chat_model_start_handler import ChatModelStartHandler

# 環境変数の読み込み
load_dotenv()

# チャットモデルスタートハンドラの初期化
handler = ChatModelStartHandler()
chat = ChatOpenAI(callbacks=[handler])

# 利用可能なテーブルのリストを取得
tables = list_tables()

# プロンプトの設定
prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(
            content=(
                "You are an AI that has access to a SQLite database.\n"
                f"The database has tables of: {tables}\n"
                "Do not make any assumptions about what tables exist "
                "or what columns exist. Instead, use the 'describe_tables' function"
            )
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

# メモリの設定
memory = ConversationBufferMemory(
    memory_key="chat_history", return_messages=True)

# ツールの設定
tools = [run_query_tool, describe_tables_tool, write_report_tool]

# エージェントの初期化
agent = OpenAIFunctionsAgent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

# エージェントの実行
agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
    memory=memory
)

agent_executor(
    "Calculate the average HP for each Pokemon type. Output the results in a HTML report.")