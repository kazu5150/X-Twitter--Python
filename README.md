# python tweepyを使ってプログラムからX投稿をやってみる。

このプロジェクトは、Pythonを使用して環境変数を管理し、Twitter APIと連携するアプリケーションです。

## 必要条件

- Python 3.x
- pip
- Xの開発者アカウント

## セットアップ

1. Xの開発者アカウントを取得します。
   - [X開発者ポータル](https://developer.x.com/ja)にアクセスします。
   - アカウントを作成し、開発者として承認を受けます。
   - プロジェクトとアプリを作成し、必要なAPIキーとトークンを取得します。
   - 必要なAPIキーとトークンは、`.env.example`ファイルに記載されています。

2. リポジトリをクローンします。

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

3. 仮想環境を作成し、アクティブにします。

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
   ```

4. 必要なパッケージをインストールします。

   ```bash
   pip install -r requirements.txt
   ```

5. `.env.example`ファイルをコピーして`.env`ファイルを作成し、必要な環境変数を設定します。

   ```bash
   cp .env.example .env
   ```

   `.env`ファイルには、X開発者ポータルで取得した以下の情報を設定してください。

   ```
    BEARER_TOKEN=
    API_KEY=
    API_SECRET=
    ACCESS_TOKEN=
    ACCESS_TOKEN_SECRET=
   ```

## 使用方法

1. アプリケーションを実行します。

   ```bash
   python main.py
   ```

2. アプリケーションの機能を利用して、Twitter APIと連携します。

## 注意事項

- APIキーやシークレットは、他人に知られないように注意してください。
- `.env`ファイルは、`.gitignore`に追加して、GitHubにアップロードされないようにしてください。
- X開発者ポータルの利用規約を遵守してください。

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。詳細は`LICENSE`ファイルを参照してください。
