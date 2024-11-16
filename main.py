import tweepy
from dotenv import load_dotenv
import os

load_dotenv()

# 環境変数から値を取得
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY") 
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

# tweepyクライアントの初期化
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# ツイートの代わりにユーザー情報を取得
try:
    me = client.get_me()
    print(f"Connected as: {me.data.username}")
except Exception as e:
    print(f"エラーが発生しました: {e}")

# ツイートを投稿するテスト
try:
    tweet = client.create_tweet(text="Pythonからのテスト投稿です。")
    print(f"ツイートを投稿しました: {tweet.data['text']}")
except Exception as e:
    print(f"エラーが発生しました: {e}")
