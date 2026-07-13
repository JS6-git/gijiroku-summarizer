# 議事録要約ツール

## 概要
議事録のテキストファイルを読み込み、Claude APIを使って自動で要約するツールです。
決定事項・ToDo・次回までの課題の3つに整理して出力します。

## 使い方
1. gijiroku.txtに議事録を貼り付ける
2. python week2_tool.py を実行する
3. summary.txtに要約結果が保存される

## 必要なもの
- Python 3.x
- Anthropic APIキー
- anthropicパッケージ（pip install anthropic）

## セットアップ
1. pip install anthropic を実行する
2. week2_tool.pyのapi_keyに自分のAPIキーを入れる
3. gijiroku.txtに議事録を貼り付けて実行する

## 関連記事
- [Claude APIで議事録要約ツールを作ってみた（Zenn）](https://zenn.dev/js6_dev/articles/77c3bf9877a571)

## ツール一覧

### 議事録要約ツール（week2_tool.py）
議事録テキストを読み込み、決定事項・ToDo・次回課題の3つに整理して要約します。

### メール返信文自動生成ツール（mail_reply.py）
受信メールを読み込み、トーン(丁寧・普通・簡潔)を選ぶだけで返信文を自動生成します。