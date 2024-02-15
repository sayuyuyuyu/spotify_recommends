from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType, OpenAIFunctionsAgent
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

from langchain.schema.messages import (
    SystemMessage,
)

from search_title import SpotifyTool

content = """
SpotifyToolの戻り値のパラメータの説明:
{
    "acousticness": {
        "description": "Confidence measure of whether the track is acoustic.",
        "example_value": 0.00242,
        "range": "0 - 1"
    },
    "danceability": {
        "description": "How suitable a track is for dancing.",
        "example_value": 0.585
    },
    "duration_ms": {
        "description": "Track duration in milliseconds.",
        "example_value": 237040
    },
    "energy": {
        "description": "Perceptual measure of intensity and activity.",
        "example_value": 0.842
    },
    "id": {
        "description": "Spotify ID for the track.",
        "example_value": "2takcwOaAZWiXQijPHIx7B"
    },
    "instrumentalness": {
        "description": "Predicts if a track contains no vocals.",
        "example_value": 0.00686
    },
    "key": {
        "description": "The key the track is in.",
        "example_value": 9,
        "range": "-1 - 11"
    },
    "liveness": {
        "description": "Presence of an audience in the recording.",
        "example_value": 0.0866
    },
    "loudness": {
        "description": "Overall loudness of a track in decibels (dB).",
        "example_value": -5.883
    },
    "mode": {
        "description": "Modality (major or minor) of a track.",
        "example_value": 0
    },
    "speechiness": {
        "description": "Presence of spoken words in a track.",
        "example_value": 0.0556
    },
    "tempo": {
        "description": "Estimated tempo of a track in BPM.",
        "example_value": 118.211
    },
    "time_signature": {
        "description": "Estimated time signature.",
        "example_value": 4,
        "range": "3 - 7"
    },
    "type": {
        "description": "Object type.",
        "allowed_values": "audio_features"
    },
    "valence": {
        "description": "Musical positiveness conveyed by a track.",
        "example_value": 0.428,
        "range": "0 - 1"
    }
}


出力の形式:https://open.spotify.com/track/{id}

"""

llm = ChatOpenAI(temperature=0)

tools = [
    SpotifyTool()
]

from langchain.prompts import MessagesPlaceholder
agent_kwargs = {
    "extra_prompt_messages": [MessagesPlaceholder(variable_name="memory")],
    "system_message": SystemMessage(
            content= content
        ),
}
memory = ConversationBufferMemory(memory_key="memory", return_messages=True)
mrkl = initialize_agent(tools, llm, agent=AgentType.OPENAI_FUNCTIONS, agent_kwargs=agent_kwargs, memory=memory, verbose=True)

# 会話ループ
user = ""
while user != "exit":
    user = input("入力してください:")
    print(user)
    ai = mrkl.invoke(input=user)
    print(ai)