import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

def plot_create(param):
    # データをロード
    year_data = pd.read_csv('data/MyTopSongs2023.csv')
    # plotをリセット
    plt.clf()
    # ヒストグラム作成
    sns.distplot(a=year_data[param], bins=30,
                 hist=True, kde=True, color='blue')
    # 罫線を追加
    plt.grid(True, linewidth=0.5)
    # 指定ディレクトリに画像を保存
    save_path = 'pic/2023dist/'+param+'_dist.png'
    plt.savefig(save_path)


if __name__ == "__main__":
    # 音楽特徴パラメータのリスト
    sound_features = ['acousticness', 'danceability', 'energy', 'instrumentalness',
                      'liveness', 'loudness', 'popularity', 'speechiness', 'tempo', 'valence', 'key']

    # リストをぐるぐる回して画像作る
    for param in sound_features:
        plot_create(param)
