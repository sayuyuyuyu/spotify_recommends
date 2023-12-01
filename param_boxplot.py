import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

def plot_create(param):
    # データをロード
    year_data = pd.read_csv('data/data_by_year.csv')
    # plotをリセット
    plt.clf()
    # 箱ひげ図作成
    sns.boxplot(data=year_data[param])
    save_path = 'pic/boxplot_pic/'+param+'_box.png'
    plt.savefig(save_path)

def get_quantile():
    # データフレームを作成
    df = pd.DataFrame(columns=['Parameter Name', 'First Quartile', 'Second Quartile', 'Third Quartile'])
    # 音楽特徴パラメータのリスト
    sound_features = ['acousticness', 'danceability', 'energy', 'instrumentalness',
                      'liveness', 'loudness', 'popularity', 'speechiness', 'tempo', 'valence', 'key']

    # リストをぐるぐる回して画像作る
    for param in sound_features:
            # データをロード
        year_data = pd.read_csv('data/data_by_year.csv')
        data=year_data[param]
        # 四分位数の計算
        q1 = data.quantile(q=0.25)
        q2 = data.quantile(q=0.5)
        q3 = data.quantile(q=0.75)

        df.loc[len(df)] = [param, q1, q2, q3]
    return df

if __name__ == "__main__":
    d= get_quantile()
    print(d.to_markdown())
    # # 音楽特徴パラメータのリスト
    # sound_features = ['acousticness', 'danceability', 'energy', 'instrumentalness',
    #                   'liveness', 'loudness', 'popularity', 'speechiness', 'tempo', 'valence', 'key']

    # # リストをぐるぐる回して画像作る
    # for param in sound_features:
    #     plot_create(param)
