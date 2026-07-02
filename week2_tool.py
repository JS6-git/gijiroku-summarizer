import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

system_prompt = "あなたは議事録要約の専門家です。長い議事録を、決定事項・ToDo・次回までの課題の3つに整理して要約してください。"

# ファイルから議事録を読み込む
with open("gijiroku.txt", "r", encoding="utf-8") as f:
    user_input = f.read()

print("議事録を読み込みました。要約中...")

try:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system=system_prompt,
        messages=[{"role": "user", "content": user_input}]
    )
    summary = response.content[0].text
    print("\n--- 要約 ---")
    print(summary)

    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)
    print("\n要約結果を summary.txt に保存しました")
except Exception as e:
    print("エラーが発生しました:", e)