# システムプロンプト
system_prompt = '''
    あなたはユーザーに音楽を教えるAIです。
    ユーザーから送られた文章から、おすすめの音楽を教えてください。
    ユーザーから送られた文章は英語に変換してください。
'''

# 関数
functions = [
    {
        # 関数の名称
        "name": "search_music",
        # 関数の機能説明
        "description": "音楽を探す際に呼び出される。出力はすべて英語で行う",
        # 関数のパラメータ
        "parameters": {
            "type": "object",
            # 各引数
            "properties": {
                "genre": {
                    "type": "string",
                    # 引数の説明
                    "description": "探したい曲のジャンル"
                },
                "mood": {
                    "type": "string",
                    "description": "感情を表す言葉"
                },
                "artist": {
                    "type": "string",
                    "description": "探したいアーティスト名"
                },
                "title": {
                    "type": "string",
                    "description": "探したい曲のタイトル"
                }
            }
        }
    }
]
