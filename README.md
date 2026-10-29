# Jev Prompt Reversi

自然言語プロンプトによって思考・着手選択を行うリバーシ（オセロ）AIと、その戦略検証・対局環境を提供するプロジェクトです。

盤面の特徴量（開放度、確定石、危険マスなど）を計算し、自然言語のポリシー（思考方針）を指示としてLLM（JEVモデル）に与えることで、ルールベースの手法をプロンプトエンジニアリングによって実現しています。

---

## 🌟 主な特徴

- **プロンプト駆動型AI (`JevPlayer`)**:
  - 盤面の評価指標（X打ち、C打ち、確定石、開放度、着手可能手）を状態としてモデルに提示。
  - 「どの指標をどの順番で比較・絞り込むか」を自然言語プロンプト（`POLICY`）で指示し、TypeSafe SDKを通じてモデル（`jev-1.14.0`）が最適な手を選択。
- **アルゴリズム再現クローン (`JevClonePlayer`)**:
  - プロンプトで与えた思考ルールをPythonコードで直接実装したクローンプレイヤー。
  - LLMが指示通りに論理推論・比較を行えているかの検証や、API呼び出し不要での高速検証が可能。
- **多様な対戦プレイヤー**:
  - `RandomPlayer`: 合法手の中からランダムに選択。
  - `MonteCarloPlayer`: モンテカルロ法（ランダムプレイアウトシミュレーション）に基づく探索AI。
  - `JevPlayer`: LLMプロンプト推論AI。
  - `JevClonePlayer`: プロンプトルール再現ヒューリスティックAI。
- **デスクトップGUI対局アプリ (`reversi_app.py`)**:
  - Tkinter製のGUIにより、人間 vs AI、または異なるAI同士の対局をリアルタイムにプレイ・観戦可能。
  - 着手可能マスのガイド表示、マルチスレッドによる思考中UIフリーズ防止に対応。
- **詳細な戦略検討・対局分析レポート (`reversi_strategy.md`)**:
  - プロンプトの設計プロセス（Prompt 1〜7）や開放度理論・確定石の評価、各AI間の勝率検証結果などを詳細に記録。

---

## 📁 ディレクトリ構成

```text
jev-prompt-reversi/
├── README.md                 # 本ドキュメント
├── requirements.txt          # 依存パッケージ一覧
├── reversi.py                # リバーシ盤面ロジック・各AIプレイヤー・対戦シミュレータ
├── reversi_app.py            # GUI対局アプリケーション (Tkinter)
├── reversi_strategy.md       # 戦略立案・プロンプト設計変遷・対局分析レポート
├── reversi_history_P6.txt    # Prompt 6 適用時の対局ログ・棋譜データ
├── reversi_history_P7.txt    # Prompt 7 適用時の対局ログ・棋譜データ
├── reversi_history_CP6.txt   # JevClone (Prompt 6 相当) の対局ログ・棋譜データ
└── reversi_history_CP7.txt   # JevClone (Prompt 7 相当) の対局ログ・棋譜データ
```

> [!NOTE]
> **非公開ファイルについて**  
> `reversi_strategy.md` 内に記載されている対人戦の評価棋譜ファイル（`evaluate_students.txt` および `evaluate_me.txt`）は、**プライバシー保護の観点からリポジトリには含めておらず、非公開**としています。

---

## 🚀 セットアップ

### 必要要件
- Python 3.10 以上
- GUI実行用: Tkinter（標準ライブラリ）

### インストール

```bash
git clone https://github.com/wsgames0w0/jev-prompt-reversi.git
cd jev-prompt-reversi
pip install -r requirements.txt
```

> `JevPlayer` を動作させる場合は、`typesafe-sdk` の利用環境および JEV API への接続設定が必要です。APIを利用しない場合でも、`Random`、`MC (MonteCarlo)`、`JevClone` は追加設定なしで動作します。

---

## 🎮 実行方法

### 1. GUI対局アプリケーション

```bash
python reversi_app.py
```

- **メニューバーからの設定**:
  - **対局**: 「新しい対局」でリセット、「終了」で終了。
  - **プレイヤー**: 人間の手番（黒番 / 白番）の切り替え。
  - **AI**: 対戦相手AI（`Random`, `MonteCarlo`, `Jev`, `JevClone`）の選択。

---

### 2. CLI対戦シミュレーション

コマンドラインから指定したAI同士を50ゲーム対戦させ、勝敗数および棋譜を `reversi_history.txt` に出力します。

```bash
python reversi.py <先手(黒)> <後手(白)>
```

#### 引数として指定可能なプレイヤー名:
- `Random` : ランダムプレイヤー
- `MC` : モンテカルロ探索プレイヤー
- `Jev` : プロンプト推論プレイヤー (要 API接続)
- `JevClone` : プロンプト再現クローンプレイヤー

#### 実行例:
```bash
# JevClone と モンテカルロAI を対戦
python reversi.py JevClone MC

# ランダムAI と JevClone を対戦
python reversi.py Random JevClone
```

---

## 🧠 プロンプト思考アーキテクチャ (JevPlayer)

`JevPlayer` は、盤面から抽出した各合法手の特徴量を元に、以下の自然言語プロンプト（ポリシー）に従って手を決定します（Prompt 6 の例）：

```text
次の処理を順に行い、候補を選択する。
なお、数値を比較せずに候補を選択しないこと。
(1) `INFO`内の全候補を対象とする。
(2) その候補の内、Xの値が最小の候補だけを残す。
(3) その候補の内、Cの値が最小の候補だけを残す。
(4) その候補の内、STABLEの値が最大の候補だけを残す。
(5) その候補の内、LIBERTYの値が最小の候補だけを残す。
(6) その候補の内、MOVABLEの値が最小の候補だけを残す。
(7) 最後にその候補が複数残っている場合は、その候補の中からランダムに選ぶ。
```

### 評価指標の意味:
- **`X` (X打ち)**: 隅の斜め隣（危険マス）への着手ペナルティ。
- **`C` (C打ち)**: 隅の隣接マスへの着手ペナルティ（外壁やブロック形成による安全手は除外）。
- **`STABLE` (確定石)**: 隅から連続して裏返される心配のない石の数。
- **`LIBERTY` (開放度)**: 着手によって反転した石・置いた石の周囲にある空きマス数（相手に着手余地を与えないため小さい方が有利）。
- **`MOVABLE` (相手の合法手数)**: 着手後に相手が打てる手の総数（相手の手を制限するため小さい方が有利）。

---

## 📊 対戦ログ形式

`reversi_history_*.txt` には以下のフォーマットで1行ごとに1対局の記録が保存されます。

```text
<黒番プレイヤー>,<白番プレイヤー>,<黒の獲得石数>,<白の獲得石数>,<着手履歴(座標列)>
```

例:
```text
RandomPlayer,JevPlayer,8,56,C4C3E6B4A4A5C2A3D2E2C1B2E1A1A2...
```

---

## 📄 ライセンス

本ソフトウェアは **[MIT License](LICENSE)** に基づいて公開されています。
詳細は [LICENSE](LICENSE) ファイルをご確認ください。

## 更新履歴

- v1
  - 2026年10月29日
