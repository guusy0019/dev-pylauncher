# PyLauncher

Windows 用のショートカットランチャーアプリケーションです。ショートカットをグループ化して管理し、簡単に起動できるようにします。

![基本ページ](./images/base_page.png)

## 主な機能

- ショートカットの一括管理
- ワークスペース機能によるショートカットのグループ化
- カスタマイズ可能な UI（テーマ、スケーリング、言語設定）
- ショートカットの一括起動・停止
- 多言語対応（日本語、英語）

## インストール方法

1. リポジトリをクローン

```bash
git clone https://github.com/your-username/pylauncher.git
cd pylauncher
```

2. 仮想環境を作成して有効化

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. 依存関係をインストール

```bash
pip install -r requirements.txt
```

4. アプリケーションを起動

```bash
python main.py or F5
```

## 使用方法

1. ショートカットの追加

   - 「ショートカットを選択」ボタンから追加したいショートカットを選択
   - ショートカット名を入力して保存

2. ワークスペースの作成
   ![ワークスペースページ](./images/workspace_page.png)

   - 複数のショートカットをグループ化して管理
   - ワークスペース名を付けて保存

3. ショートカットの起動

   - 個別に起動
   - チェックボックスで複数選択して一括起動

4. 設定
   ![代替テキスト](./images/config_page.png)
   - テーマの変更
   - スケーリングの調整
   - 言語の切り替え

## 開発環境

- Python 3.12
- customtkinter
- cx_Freeze（ビルド用）

## 作者

[guusy0019]

## バージョン履歴

- v1.0.0 (2024-04-06)
  - 初期リリース
  - 基本的な機能の実装
