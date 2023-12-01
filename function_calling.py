import openai
from pprint import pprint
import config as cf
import settings
import getFeatureCSV as gF

openai.api_key = settings.OPENAI


def function_test(input):
    res = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": cf.system_prompt},
            {"role": "user", "content": input},
        ],
        functions=cf.functions,
        function_call="auto",
    )
    return res['choices'][0]['message']


if __name__ == '__main__':
    ans = function_test("七尾旅人の「サーカスナイト」みたいな落ち着く曲が聞きたい。ジャズやアコースティックな曲が良い。")

    pprint(ans)
