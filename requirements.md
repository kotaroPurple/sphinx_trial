# sphinx-trial プロジェクト要件定義

## プロジェクト概要

- **プロジェクト名**: sphinx-trial
- **管理ツール**: uv
- **目的**: Pythonライブラリの開発とSphinxによるドキュメント作成のサンプル

## ライブラリ構成

### ディレクトリ構造
```
src/sphinx_trial/
├── __init__.py
├── py.typed
├── math/
│   ├── __init__.py
│   ├── calculator.py
│   └── geometry.py
├── text/
│   ├── __init__.py
│   ├── formatter.py
│   └── validator.py
└── utils/
    ├── __init__.py
    ├── logger.py
    └── config.py
```

### 実装する機能

#### 1. math モジュール
- **calculator.py**: 基本的な計算機能
  - `Calculator` クラス: 四則演算メソッド
  - `add()`, `subtract()`, `multiply()`, `divide()` メソッド
- **geometry.py**: 幾何学計算
  - `Circle` クラス: 円の面積・周囲計算
  - `Rectangle` クラス: 長方形の面積・周囲計算

#### 2. text モジュール
- **formatter.py**: テキスト整形機能
  - `TextFormatter` クラス: 文字列の整形
  - `capitalize_words()`, `remove_spaces()`, `truncate()` メソッド
- **validator.py**: バリデーション機能
  - `is_email()`, `is_phone()`, `is_url()` 関数

#### 3. utils モジュール
- **logger.py**: ログ機能
  - `SimpleLogger` クラス: 基本的なログ出力
- **config.py**: 設定管理
  - `Config` クラス: 設定値の読み込み・保存

## 使用例（example ディレクトリ）

### 作成する例
1. **basic_usage.py**: 基本的な使い方
2. **math_examples.py**: math モジュールの使用例
3. **text_examples.py**: text モジュールの使用例
4. **utils_examples.py**: utils モジュールの使用例
5. **advanced_usage.py**: 複数モジュールを組み合わせた例

## ドキュメント構成（docs ディレクトリ）

### Sphinx ドキュメント
1. **API リファレンス**: 自動生成されるAPI文書
2. **チュートリアル**: 基本的な使い方
3. **使用例**: example ディレクトリの内容を含む
4. **インストールガイド**: uvでのインストール方法

### ドキュメント構造
```
docs/
├── source/
│   ├── conf.py
│   ├── index.rst
│   ├── installation.rst
│   ├── tutorial.rst
│   ├── examples.rst
│   └── api/
│       ├── math.rst
│       ├── text.rst
│       └── utils.rst
└── build/
```

## 開発タスク

### Phase 1: ライブラリ実装
- [ ] math モジュールの実装
- [ ] text モジュールの実装
- [ ] utils モジュールの実装
- [ ] 各モジュールの `__init__.py` 更新

### Phase 2: 使用例作成
- [ ] example ディレクトリ作成
- [ ] 各使用例ファイルの実装

### Phase 3: Sphinx ドキュメント
- [ ] Sphinx 初期化と設定
- [ ] API リファレンス自動生成設定
- [ ] チュートリアルとガイド作成
- [ ] 使用例のドキュメント化

### Phase 4: 環境整備
- [ ] pyproject.toml に Sphinx 依存関係追加
- [ ] ドキュメントビルドスクリプト作成
- [ ] README.md 更新

## 成果物

1. **機能豊富なライブラリ**: 3つのモジュールに分かれた実用的な機能
2. **実践的な使用例**: 5つの異なるユースケース
3. **完全なドキュメント**: Sphinxで生成されたプロフェッショナルな文書
4. **開発環境**: uvで管理された再現可能な環境

## 品質基準

- 全ての関数・クラスにdocstring
- 型ヒント完備
- 使用例は実際に動作する
- ドキュメントは初心者にも理解しやすい