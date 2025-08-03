# Sphinx ドキュメント作成ガイド

このドキュメントでは、sphinx-trialプロジェクトでSphinxドキュメントを作成する手順と、自動生成されたファイルと手動作成したファイルの区別を説明します。

## 📋 ファイル分類

### 🤖 Sphinx自動生成ファイル（編集不要）
```
docs/
├── _build/                    # ビルド出力（全て自動生成）
│   └── html/                  # HTMLファイル群
├── _static/                   # 静的ファイル（自動作成）
├── _templates/                # テンプレート（自動作成）
└── Makefile                   # sphinx-quickstartで生成
```

### ✏️ 手動作成・編集が必要なファイル
```
docs/
├── conf.py                    # 設定ファイル（要編集）
├── index.rst                  # メインページ（要作成）
├── installation.rst           # インストールガイド（要作成）
├── tutorial.rst              # チュートリアル（要作成）
├── examples.rst               # 使用例（要作成）
├── api/                       # APIリファレンス（要作成）
│   ├── math.rst
│   ├── text.rst
│   └── utils.rst
└── sphinx_commands.md         # このファイル（要作成）
```

## 🚀 開発者向け：ドキュメント作成手順

### Step 1: 環境セットアップ
```bash
# 依存関係をインストール
uv pip install -e ".[docs]"

# または開発環境全体をセットアップ
python dev_setup.py
```

### Step 2: Sphinxプロジェクト初期化（初回のみ）
```bash
cd docs
uv run sphinx-quickstart \
  --quiet \
  --project="your-project-name" \
  --author="your-name" \
  --release="0.1.0" \
  --language="en" \
  --extensions="sphinx.ext.autodoc,sphinx.ext.viewcode,sphinx.ext.napoleon" \
  --makefile \
  --no-batchfile \
  .
```

**生成されるファイル:**
- `conf.py` - 設定ファイル（要編集）
- `index.rst` - メインページ（要編集）
- `Makefile` - ビルド用Makefile
- `_build/`, `_static/`, `_templates/` - ディレクトリ

### Step 3: conf.py の必須編集
```python
# ライブラリのパスを追加（必須）
import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# 拡張機能（必要に応じて追加）
extensions = [
    'sphinx.ext.autodoc',           # 自動ドキュメント生成
    'sphinx.ext.viewcode',          # ソースコードリンク
    'sphinx.ext.napoleon',          # Google/NumPy docstring形式
    'sphinx_autodoc_typehints',     # 型ヒント表示
]

# テーマ変更（推奨）
html_theme = 'sphinx_rtd_theme'

# autodoc設定（推奨）
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}
autodoc_typehints = 'description'
```

### Step 4: ドキュメント構造の作成
```bash
# APIリファレンス用ディレクトリ作成
mkdir -p docs/api
```

### Step 5: 必要なRSTファイルを作成

#### 5.1 メインページ (index.rst)
```rst
プロジェクト名 documentation
=============================

プロジェクトの概要説明

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   installation
   tutorial
   examples

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   api/module1
   api/module2
```

#### 5.2 APIリファレンス (api/module_name.rst)
```rst
Module Name
===========

.. automodule:: your_package.module_name
   :members:
   :undoc-members:
   :show-inheritance:

Class Name
----------

.. autoclass:: your_package.module_name.ClassName
   :members:
   :undoc-members:
   :show-inheritance:
```

#### 5.3 使用例ページ (examples.rst)
```rst
Examples
========

.. literalinclude:: ../example/basic_usage.py
   :language: python
   :caption: example/basic_usage.py
```

### Step 6: ドキュメントビルド
```bash
# taskipy使用（推奨）
uv run task docs

# 直接実行
uv run python build_docs.py

# Sphinxコマンド直接実行
cd docs
uv run sphinx-build -b html . _build/html
```

### Step 7: 結果確認
```bash
# ローカルサーバーで確認
uv run task docs-serve
# http://localhost:8000 でアクセス

# ファイルを直接開く
open docs/_build/html/index.html
```

## 🔄 継続的な更新ワークフロー

### コード変更時
1. **docstringを更新** - 関数・クラスの説明を追加/修正
2. **ドキュメントビルド** - `uv run task docs`
3. **確認** - ブラウザで結果をチェック
4. **コミット** - 変更をgitにコミット

### 新機能追加時
1. **新しいモジュール作成** - `src/your_package/new_module/`
2. **APIリファレンス追加** - `docs/api/new_module.rst`
3. **メインページ更新** - `docs/index.rst`のtoctreeに追加
4. **使用例作成** - `example/new_module_examples.py`
5. **ドキュメントビルド・確認・コミット**

## 📁 ファイル管理のベストプラクティス

### ✅ 編集すべきファイル
- `docs/conf.py` - Sphinx設定
- `docs/index.rst` - メインページ
- `docs/installation.rst` - インストールガイド
- `docs/tutorial.rst` - チュートリアル
- `docs/examples.rst` - 使用例
- `docs/api/*.rst` - APIリファレンス
- ソースコードのdocstring

### ❌ 編集してはいけないファイル
- `docs/_build/` 以下全て
- `docs/_static/` 以下（自動生成される場合）
- `docs/_templates/` 以下（自動生成される場合）

### 🗂️ .gitignoreに追加すべき
```gitignore
# Sphinx documentation
docs/_build/
docs/_static/
docs/_templates/
```

## 🛠️ 利用可能なコマンド

### taskipy（推奨）
```bash
uv run task docs        # ドキュメントビルド
uv run task docs-clean  # ビルドファイル削除
uv run task docs-serve  # ビルド＋ローカルサーバー起動
```

### 直接実行
```bash
uv run python build_docs.py        # ビルド
uv run python build_docs.py clean  # クリーン
```

### Sphinx直接実行
```bash
cd docs
uv run sphinx-build -b html . _build/html     # 基本ビルド
uv run sphinx-build -E -b html . _build/html  # 全再ビルド
uv run sphinx-build -W -b html . _build/html  # 警告をエラー扱い
```

## 🔧 トラブルシューティング

### よくある問題

1. **モジュールが見つからない**
   ```
   WARNING: autodoc: failed to import module 'your_package'
   ```
   **解決:** `conf.py`のパス設定を確認
   ```python
   sys.path.insert(0, os.path.abspath('../src'))
   ```

2. **テーマが見つからない**
   ```
   WARNING: html_theme 'sphinx_rtd_theme' not found
   ```
   **解決:** テーマをインストール
   ```bash
   uv pip install sphinx-rtd-theme
   ```

3. **重複警告**
   ```
   WARNING: duplicate object description
   ```
   **解決:** 通常は無視してOK。気になる場合は`:no-index:`を使用

4. **ビルドが失敗する**
   - パッケージがeditable modeでインストールされているか確認
   - 依存関係が全てインストールされているか確認
   - RSTファイルの構文エラーがないか確認

### デバッグ方法
```bash
# 詳細出力でビルド
cd docs
uv run sphinx-build -v -b html . _build/html

# 警告を詳細表示
uv run sphinx-build -W -v -b html . _build/html
```

## 📚 参考リソース

- [Sphinx公式ドキュメント](https://www.sphinx-doc.org/)
- [reStructuredText記法](https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html)
- [sphinx.ext.autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html)
- [Read the Docs テーマ](https://sphinx-rtd-theme.readthedocs.io/)

## 🎯 まとめ

1. **初期設定**: `sphinx-quickstart`で基本構造を作成
2. **設定編集**: `conf.py`でパスとテーマを設定
3. **コンテンツ作成**: RSTファイルでドキュメント構造を作成
4. **継続更新**: docstring更新 → ビルド → 確認 → コミット

このワークフローに従えば、プロフェッショナルなドキュメントを継続的に維持できます。