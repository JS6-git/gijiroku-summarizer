import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

system_prompt = """あなたはビジネスメールの返信文を作成する専門家です。
受信したメールの内容を読んで、以下のルールで返信文を作成してください：
- 丁寧で簡潔なビジネス文体
- 相手の要件に的確に応える内容
- 件名・本文・署名の形式で出力する
- 署名は「[お名前]」とプレースホルダーにする"""

print("メール返信文自動生成ツール")
print("=" * 40)

# ファイルからメールを読み込む
with open("mail_input.txt", "r", encoding="utf-8") as f:
    received_mail = f.read()

print("メールを読み込みました。")

# 返信のトーンを選択
print("\n返信のトーンを選んでください：")
print("1. 丁寧・フォーマル")
print("2. 普通のビジネス")
print("3. 簡潔・スピード重視")

tone_choice = input("番号を入力(1/2/3): ")

tone_map = {
    "1": "非常に丁寧でフォーマルな文体で",
    "2": "標準的なビジネス文体で",
    "3": "簡潔でスピード感のある文体で"
}

tone = tone_map.get(tone_choice, "標準的なビジネス文体で")

prompt = f"""以下のメールに対して、{tone}返信文を作成してください。

【受信メール】
{received_mail}"""

print("\n返信文を生成中...")

try:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=800,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}]
    )
    
    reply = response.content[0].text
    print("\n" + "=" * 40)
    print("【生成された返信文】")
    print("=" * 40)
    print(reply)
    
    with open("mail_reply_output.txt", "w", encoding="utf-8") as f:
        f.write(reply)
    print("\n返信文を mail_reply_output.txt に保存しました")

except Exception as e:
    print("エラーが発生しました:", e)