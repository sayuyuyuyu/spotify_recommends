import os
from os.path import join, dirname
from dotenv import load_dotenv

from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain import hub
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor

from langchain.memory import ConversationBufferMemory
from langchain.schema.messages import (
    SystemMessage,
)
from langchain.prompts import MessagesPlaceholder

# from tool.search_title import SpotifyTool
# from tool.search_artisit import SearchArtistTool
# from tool.search_recommend import SearchRecommendTool

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

# Agentに渡すプロンプト読み込み
# system_prompt = open('prompt/agentPrompt.txt')
# content = system_prompt.read

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/openai-functions-agent")
prompt.messages

# LLMの用意
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Toolの用意
tools = [
    # SpotifyTool(),
    # SearchArtistTool(),
    # SearchRecommendTool()
]

agent = create_openai_functions_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)



# 会話ループ
user = ""
while user != "exit":
    user = input("user: ")
    ai = agent_executor.invoke(input=user)
    print(ai)


# agent_kwargs = {
#     "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
#     "system_message": SystemMessage(
#             content= content
#         ),
# }
# memory = ConversationBufferMemory(memory_key="memory", return_messages=True)
# mrkl = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, agent_kwargs=agent_kwargs, memory=memory, verbose=True)

# agent = create_openai_functions_agent(llm, tools, prompt)