# Cursorおためし

あらすじを書く

タイトル：ChatGPTとVScodeを融合したエディタ「Cursor」を使ってみた

X（旧Twitter）で

先日のOpenAI Dev Dayで利用されている画面が話題になった「Cursor」というエディタが気になったので使ってみました。

## TL;DR

・VScodeをフォークしているのでVScodeで出来ることはあらかたできる

・コーディング支援用に調整されたシステムプロンプトを内蔵したChatGPTライクのタブがある

・コマンドでコード生成、コードをChatGPTに投げることがとてもかんたん

・ある程度は無料でGPT4も使える

## 導入

OSを選択してDL

https://cursor.sh/

### 初期設定

`Shortcuts`

自分の使いやすいIDEで

`Vim/Emacs`

`Codebase-wide`

`Language`

AIとの対話で使いたい言語を指定

日本語なら`「Always respond in 日本語」`みたいなシステムプロンプトが自動で入る

`Command Line`

なんかまずいらしいので触らない方がよき

https://qiita.com/Kazu634/items/28c3f87e91cf52a940c0

`VScode Extensions`

VScodeを既に入れてたら、入れてる拡張機能を引き継げる

**Use Extensions**で引継ぎ

Cursorアカウントにログインが求められる

## 使い方

### チャットタブ

右側にチャットタブが出ます

### コマンド系

Ctrl+L：選択したコードをチャットに貼り付け

コードを選択してCtrl+Lで、その部分がスニペット形式で張り付けれる

ターミナル等でのエラー箇所はその部分全部が自動で選択されてる状態になるからCtrl+L押すだけでエラー調べられる！

Ctrl+K：コード上でやりたいとこを投げてコード生成させる

コード上で押すと入力メニュー出現

あとは実現したいことを書けばインタラクティブにコードが生成される！革新！

### 大事な設定

入力データの学習
