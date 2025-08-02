# 🎯 Claude Code Usage Monitor (日本語版)

**このリポジトリは、[Maciek-roboblog/Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) のフォークであり、日本円でのコスト表示機能を追加し、READMEを日本語化したものです。**

[![PyPI Version](https://img.shields.io/pypi/v/claude-monitor-ja.svg)](https://pypi.org/project/claude-monitor-ja/)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![codecov](https://codecov.io/gh/Maciek-roboblog/Claude-Code-Usage-Monitor/branch/main/graph/badge.svg)](https://codecov.io/gh/Maciek-roboblog/Claude-Code-Usage-Monitor)

Claude AIのトークン使用量をリアルタイムで監視する美しいターミナルツールです。高度な分析、機械学習ベースの予測、リッチなUIを備えています。トークン消費量、バーンレート、コスト分析を追跡し、セッション制限に関するインテリジェントな予測を取得できます。

![Claude Token Monitor Screenshot](https://raw.githubusercontent.com/Maciek-roboblog/Claude-Code-Usage-Monitor/main/doc/sc.png)

---

## 📑 目次

- [✨ 主な機能](#-主な機能)
- [🚀 インストール](#-インストール)
  - [⚡ uv を使用した最新のインストール (推奨)](#-uv-を使用した最新のインストール-推奨)
  - [📦 pip を使用したインストール](#-pip-を使用したインストール)
  - [🛠️ その他のパッケージマネージャー](#️-その他のパッケージマネージャー)
- [📖 使用方法](#-使用方法)
  - [ヘルプの表示](#ヘルプの表示)
  - [基本的な使用方法](#基本的な使用方法)
  - [設定オプション](#設定オプション)
  - [利用可能なプラン](#利用可能なプラン)
- [🙏 このリリースをテストするご協力をお願いします！](#-このリリースをテストするご協力をお願いします)
- [✨ 機能と仕組み](#-機能と仕組み)
  - [現在の機能](#現在の機能)
  - [Claude セッションの理解](#claude-セッションの理解)
  - [プランごとのトークン制限](#プランごとのトークン制限)
  - [スマート検出機能](#スマート検出機能)
- [🚀 使用例](#-使用例)
  - [一般的なシナリオ](#一般的なシナリオ)
  - [ベストプラクティス](#ベストプラクティス)
- [🔧 開発インストール](#-開発インストール)
- [トラブルシューティング](#トラブルシューティング)
  - [インストールに関する問題](#インストールに関する問題)
  - [実行時の問題](#実行時の問題)
- [📞 お問い合わせ](#-お問い合わせ)
- [📚 その他のドキュメント](#-その他のドキュメント)
- [📝 ライセンス](#-ライセンス)
- [🤝 貢献者](#-貢献者)
- [🙏 謝辞](#-謝辞)



## ✨ 主な機能

### 🚀 **v3.0.0 メジャーアップデート - 完全なアーキテクチャの書き換え**

- **🔮 MLベースの予測** - P90パーセンタイル計算とインテリジェントなセッション制限検出
- **🔄 リアルタイム監視** - 設定可能なリフレッシュレート (0.1-20 Hz) とインテリジェントな表示更新
- **📊 高度なリッチUI** - 美しい色分けされたプログレスバー、テーブル、WCAG準拠のコントラストを持つレイアウト
- **🤖 スマート自動検出** - カスタム制限検出による自動プラン切り替え
- **📋 強化されたプランサポート** - 更新された制限: Pro (44k), Max5 (88k), Max20 (220k), Custom (P90ベース)
- **⚠️ 高度な警告システム** - コストと時間の予測を伴う多段階アラート
- **💼 プロフェッショナルなアーキテクチャ** - 単一責任の原則 (SRP) に準拠したモジュラー設計
- **🎨 インテリジェントなテーマ設定** - 自動ターミナル背景検出機能を備えた科学的な配色
- **⏰ 高度なスケジューリング** - 自動検出されたシステムタイムゾーンと時間形式の設定
- **📈 コスト分析** - キャッシュトークン計算を含むモデル固有の価格設定
- **🔧 Pydantic検証** - 自動検証によるタイプセーフな設定
- **📝 包括的なロギング** - 設定可能なレベルでのオプションのファイルロギング
- **🧪 広範なテスト** - 完全なカバレッジを持つ100以上のテストケース
- **🎯 エラー報告** - 本番監視用のオプションのSentry統合
- **⚡ パフォーマンス最適化** - 高度なキャッシュと効率的なデータ処理

### 📋 デフォルトのカスタムプラン

**カスタムプラン**は、5時間のClaude Codeセッション用に特別に設計されたデフォルトオプションです。次の3つの重要なメトリックを監視します。
- **トークン使用量** - トークン消費量を追跡
- **メッセージ使用量** - メッセージ数を監視
- **コスト使用量** - 長時間のセッションで最も重要なメトリック

カスタムプランは、過去192時間 (8日間) のすべてのセッションを分析し、実際の使用量に基づいてパーソナライズされた制限を計算することで、使用パターンに自動的に適応します。これにより、特定のワークフローに合わせた正確な予測と警告が保証されます。


## 🚀 インストール
### ⚡ uv を使用した最新のインストール (推奨)

**uv が最適な選択である理由:**
- ✅ 自動的に隔離された環境を作成 (システムとの競合なし)
- ✅ Pythonのバージョン問題なし
- ✅ 「externally-managed-environment」エラーなし
- ✅ 簡単な更新とアンインストール
- ✅ すべてのプラットフォームで動作

モニターをインストールして使用する最も速く簡単な方法:

[![PyPI](https://img.shields.io/pypi/v/claude-monitor-ja.svg)](https://pypi.org/project/claude-monitor-ja/)

#### PyPIからのインストール

```bash
# uv を使用して PyPI から直接インストール (最も簡単)
uv tool install claude-monitor-ja

# どこからでも実行
claude-monitor-ja  # または cmonitor, ccmonitor (短縮形)
```


#### ソースからのインストール

```bash
# ソースからクローンしてインストール
git clone https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor.git
cd Claude-Code-Usage-Monitor
uv tool install .

# どこからでも実行
claude-monitor-ja
```


#### 初めての uv ユーザー向け

まだ uv がインストールされていない場合は、次のコマンドで入手できます。

```bash
# Linux/macOSの場合:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windowsの場合:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# インストール後、ターミナルを再起動してください
```


### 📦 pip を使用したインストール

```bash
# PyPI からインストール
pip install claude-monitor-ja

# claude-monitor-ja コマンドが見つからない場合は、~/.local/bin を PATH に追加します:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc  # またはターミナルを再起動

# どこからでも実行
claude-monitor-ja  # または cmonitor, ccmonitor (短縮形)
```


>
> **⚠️ PATH 設定**: WARNING: The script claude-monitor-ja is installed in '/home/username/.local/bin' which is not on PATH と表示された場合は、上記の export PATH コマンドに従ってください。
>
> **⚠️ 重要**: 最新のLinuxディストリビューション (Ubuntu 23.04+, Debian 12+, Fedora 38+) では、「externally-managed-environment」エラーが発生する場合があります。--break-system-packages を使用する代わりに、次のことを強くお勧めします。
> 1. **uv を使用する** (上記参照) - より安全で簡単です
> 2. **仮想環境を使用する** - python3 -m venv myenv && source myenv/bin/activate
> 3. **pipx を使用する** - pipx install claude-monitor-ja
>
> 詳細な解決策については、トラブルシューティングセクションを参照してください。

### 🛠️ その他のパッケージマネージャー

#### pipx (隔離された環境)
```bash
# pipx でインストール
pipx install claude-monitor-ja

# どこからでも実行
claude-monitor-ja  # または claude-code-monitor, cmonitor, ccmonitor, ccm (短縮形)
```


#### conda/mamba
```bash
# conda 環境で pip を使用してインストール
pip install claude-monitor-ja

# どこからでも実行
claude-monitor-ja  # または cmonitor, ccmonitor (短縮形)
```


## 📖 使用方法

### ヘルプの表示

```bash
# ヘルプ情報を表示
claude-monitor-ja --help
```

#### 利用可能なコマンドラインパラメータ

| パラメータ | タイプ | デフォルト | 説明 |
|-----------|------|---------|-------------|
| --plan | string | custom | プランタイプ: pro, max5, max20, または custom |
| --custom-limit-tokens | int | None | カスタムプランのトークン制限 (0より大きい必要があります) |
| --view | string | realtime | 表示タイプ: realtime, daily, または monthly |
| --timezone | string | auto | タイムゾーン (自動検出)。例: UTC, America/New_York, Europe/London |
| --time-format | string | auto | 時間形式: 12h, 24h, または auto |
| --theme | string | auto | 表示テーマ: light, dark, classic, または auto |
| --refresh-rate | int | 10 | データリフレッシュレート (秒単位) (1-60) |
| --refresh-per-second | float | 0.75 | ディスプレイリフレッシュレート (Hz) (0.1-20.0) |
| --reset-hour | int | None | 毎日のリセット時間 (0-23) |
| --log-level | string | INFO | ロギングレベル: DEBUG, INFO, WARNING, ERROR, CRITICAL |
| --log-file | path | None | ログファイルのパス |
| --debug | flag | False | デバッグロギングを有効にする |
| --version, -v | flag | False | バージョン情報を表示 |
| --clear | flag | False | 保存された設定をクリア |

#### プランオプション

| プラン | トークン制限 | コスト制限 | 説明 |
|------|-------------|------------------|-------------|
| pro | 19,000 | $18.00 | Claude Pro サブスクリプション |
| max5 | 88,000 | $35.00 | Claude Max5 サブスクリプション |
| max20 | 220,000 | $140.00 | Claude Max20 サブスクリプション |
| custom | P90ベース | (デフォルト) $50.00 | ML分析による自動検出 |

#### コマンドエイリアス

このツールは、次のいずれかのコマンドを使用して呼び出すことができます。
- claude-monitor-ja (プライマリ)
- claude-code-monitor (フルネーム)
- cmonitor (短縮形)
- ccmonitor (短縮形の代替)
- ccm (最短)

#### フラグ保存機能

モニターは、毎回指定する必要がないように、設定を自動的に保存します。

**保存されるもの:**
- 表示タイプ (--view)
- テーマ設定 (--theme)
- タイムゾーン設定 (--timezone)
- 時間形式 (--time-format)
- リフレッシュレート (--refresh-rate, --refresh-per-second)
- リセット時間 (--reset-hour)
- カスタムトークン制限 (--custom-limit-tokens)

**設定の場所:** ~/.claude-monitor-ja/last_used.json

**使用例:**
```bash
# 初回実行 - 設定を指定
claude-monitor-ja --plan pro --theme dark --timezone "America/New_York"

# 以降の実行 - 設定は自動的に復元されます
claude-monitor-ja --plan pro

# このセッションの保存された設定を上書き
claude-monitor-ja --plan pro --theme light

# 保存されたすべての設定をクリア
claude-monitor-ja --clear
```

**主な機能:**
- ✅ セッション間でパラメータが自動的に永続化されます
- ✅ CLI引数は常に保存された設定を上書きします
- ✅ アトミックなファイル操作により破損を防ぎます
- ✅ 設定ファイルが破損した場合でも正常にフォールバックします
- ✅ プランパラメータは保存されません (毎回指定する必要があります)

### 基本的な使用方法

#### uv ツールインストールの場合 (推奨)
```bash
# デフォルト (自動検出付きカスタムプラン)
claude-monitor-ja

# 代替コマンド
claude-code-monitor  # 完全な説明名
cmonitor             # 短縮エイリアス
ccmonitor            # 短縮代替
ccm                  # 最短エイリアス

# モニターを終了
# Ctrl+C を押して正常に終了します
```

#### 開発モード

ソースから実行する場合は、src/ ディレクトリから python -m claude_monitor を使用します。

### 設定オプション

#### プランの指定

```bash
# P90自動検出付きカスタムプラン (デフォルト)
claude-monitor-ja --plan custom

# Pro プラン (~44,000 トークン)
claude-monitor-ja --plan pro

# Max5 プラン (~88,000 トークン)
claude-monitor-ja --plan max5

# Max20 プラン (~220,000 トークン)
claude-monitor-ja --plan max20

# 明示的なトークン制限付きカスタムプラン
claude-monitor-ja --plan custom --custom-limit-tokens 100000
```

#### カスタムリセット時間

```bash
# 午前3時にリセット
claude-monitor-ja --reset-hour 3

# 午後10時にリセット
claude-monitor-ja --reset-hour 22
```

#### 使用状況表示の設定

```bash
# ライブアップデート付きリアルタイム監視 (デフォルト)
claude-monitor-ja --view realtime

# テーブル形式で集計された毎日のトークン使用量
claude-monitor-ja --view daily

# テーブル形式で集計された毎月のトークン使用量
claude-monitor-ja --view monthly

```

#### パフォーマンスと表示の設定

```bash
# リフレッシュレートの調整 (1-60秒、デフォルト: 10)
claude-monitor-ja --refresh-rate 5

# ディスプレイリフレッシュレートの調整 (0.1-20 Hz、デフォルト: 0.75)
claude-monitor-ja --refresh-per-second 1.0

# 時間形式の設定 (デフォルトで自動検出)
claude-monitor-ja --time-format 24h  # または 12h

# 特定のテーマを強制
claude-monitor-ja --theme dark  # light, dark, classic, auto

# 保存された設定をクリア
claude-monitor-ja --clear
```

#### タイムゾーン設定

デフォルトのタイムゾーンは**システムから自動検出されます**。任意の有効なタイムゾーンで上書きできます。

```bash
# 米国東部時間を使用
claude-monitor-ja --timezone America/New_York

# 東京時間を使用
claude-monitor-ja --timezone Asia/Tokyo

# UTC を使用
claude-monitor-ja --timezone UTC

# ロンドン時間を使用
claude-monitor-ja --timezone Europe/London
```

#### ロギングとデバッグ

```bash
# デバッグロギングを有効にする
claude-monitor-ja --debug

# ファイルにログを記録
claude-monitor-ja --log-file ~/.claude-monitor-ja/logs/monitor.log

# ログレベルを設定
claude-monitor-ja --log-level WARNING  # DEBUG, INFO, WARNING, ERROR, CRITICAL
```

### 利用可能なプラン

| プラン | トークン制限 | 最適な用途 |
|------|-----------------|----------|
| **custom** | P90自動検出 | インテリジェントな制限検出 (デフォルト) |
| **pro** | ~19,000 | Claude Pro サブスクリプション |
| **max5** | ~88,000 | Claude Max5 サブスクリプション |
| **max20** | ~220,000 | Claude Max20 サブスクリプション |

#### 高度なプラン機能

- **P90分析**: 履歴使用量の90パーセンタイル分析
- **コスト追跡**: キャッシュトークン計算を含むモデル固有の価格設定
- **制限検出**: 95%の信頼度でインテリジェントなしきい値検出
- **キャッシュサポート**: キャッシュ作成と読み取りトークンコストを含む
- **モデル固有**: Claude 3.5、Claude 4、および将来のモデルに適応

## 🚀 v3.0.0 の新機能

### 主な変更点

#### **完全なアーキテクチャの書き換え**
- 単一責任の原則 (SRP) に準拠したモジュラー設計
- Pydanticベースのタイプセーフな設定と検証
- オプションのSentry統合による高度なエラー処理
- 100以上のテストケースを含む包括的なテストスイート

#### **機能強化**
- **P90分析**: 90パーセンタイル計算を使用した機械学習ベースの制限検出
- **更新されたプラン制限**: Pro (44k), Max5 (88k), Max20 (220k) トークン
- **コスト分析**: キャッシュトークン計算を含むモデル固有の価格設定
- **リッチUI**: 自動ターミナル背景検出機能を備えたWCAG準拠のテーマ

#### **新しいCLIオプション**
- --refresh-per-second: 設定可能なディスプレイリフレッシュレート (0.1-20 Hz)
- --time-format: 自動12時間/24時間形式検出
- --custom-limit-tokens: カスタムプランの明示的なトークン制限
- --log-file および --log-level: 高度なロギング機能
- --clear: 保存された設定をリセット
- コマンドエイリアス: claude-code-monitor, cmonitor, ccmonitor, ccm (利便性のため)

#### **破壊的変更**
- パッケージ名が claude-usage-monitor から claude-monitor-ja に変更されました
- デフォルトプランが pro から custom (自動検出付き) に変更されました
- 最小Pythonバージョンが3.9+に引き上げられました
- コマンド構造が更新されました (上記の例を参照)


## ✨ 機能と仕組み

### v3.0.0 アーキテクチャの概要

新バージョンは、単一責任の原則 (SRP) に従ったモジュラーアーキテクチャで完全に書き直されています。

### 🖥️ ユーザーインターフェース層

| コンポーネント | 説明 |
| -------------------- | --------------------- |
| **CLIモジュール** | Pydanticベース |
| **設定/構成** | タイプセーフ |
| **エラー処理** | Sentry対応 |
| **リッチターミナルUI** | 適応型テーマ |

---

### 🎛️ 監視オーケストレーター

| コンポーネント | 主な責任 |
| ------------------------ | ---------------------------------------------------------------- |
| **中央制御ハブ** | セッション管理 · リアルタイムデータフロー · コンポーネント連携 |
| **データマネージャー** | キャッシュ管理 · ファイルI/O · 状態永続化 |
| **セッションモニター** | リアルタイム · 5時間ウィンドウ · トークン追跡 |
| **UIコントローラー** | リッチディスプレイ · プログレスバー · テーマシステム |
| **分析** | P90計算 · バーンレート · 予測 |

---

### 🏗️ 基盤層

| コンポーネント | コア機能 |
| ------------------- | ------------------------------------------------------- |
| **コアモデル** | セッションデータ · 設定スキーマ · タイプセーフ |
| **分析エンジン** | MLアルゴリズム · 統計 · 予測 |
| **ターミナルテーマ** | 自動検出 · WCAGカラー · コントラスト最適化 |
| **Claude APIデータ** | トークン追跡 · コスト計算 · セッションブロック |

---

**🔄 データフロー:**
Claude 設定ファイル → データ層 → 分析エンジン → UIコンポーネント → ターミナル表示


### 現在の機能

#### 🔄 高度なリアルタイム監視
- 設定可能な更新間隔 (1-60秒)
- 高精度ディスプレイリフレッシュ (0.1-20 Hz)
- CPU使用量を最小限に抑えるインテリジェントな変更検出
- コールバックシステムによるマルチスレッドオーケストレーション

#### 📊 リッチUIコンポーネント
- **プログレスバー**: 科学的なコントラスト比を持つWCAG準拠の配色
- **データテーブル**: モデル固有の統計情報を含むソート可能な列
- **レイアウトマネージャー**: ターミナルサイズに適応するレスポンシブデザイン
- **テーマシステム**: 最適な読みやすさのためにターミナル背景を自動検出

#### 📈 複数の使用状況表示
- **リアルタイム表示** (デフォルト): プログレスバー、現在のセッションデータ、バーンレート分析によるライブ監視
- **日次表示**: 日付、モデル、入力/出力/キャッシュトークン、合計トークン、コストを表示する集計された日次統計
- **月次表示**: 長期的なトレンド分析と予算計画のための月次集計データ

#### 🔮 機械学習予測
- **P90計算**: インテリジェントな制限検出のための90パーセンタイル分析
- **バーンレート分析**: マルチセッション消費パターン分析
- **コスト予測**: キャッシュトークン計算を含むモデル固有の価格設定
- **セッション予測**: 使用パターンに基づいてセッションがいつ期限切れになるかを予測

#### 🤖 インテリジェントな自動検出
- **背景検出**: ターミナルテーマ (ライト/ダーク) を自動的に決定
- **システム統合**: タイムゾーンと時間形式の設定を自動検出
- **プラン認識**: 最適なプランを提案するために使用パターンを分析
- **制限検出**: 実際のトークン制限を見つけるために履歴データをスキャン

### Claude セッションの理解

#### Claude Code セッションの仕組み

Claude Code は**5時間ローリングセッションウィンドウシステム**で動作します。

1. **セッション開始**: Claude への最初のメッセージで開始
2. **セッション期間**: 最初のメッセージから正確に5時間継続
3. **トークン制限**: 各5時間セッションウィンドウ内で適用
4. **複数セッション**: 複数のアクティブなセッションを同時に持つことができます
5. **ローリングウィンドウ**: 他のセッションがアクティブな間でも新しいセッションを開始できます

#### セッションリセットスケジュール

**セッションタイムラインの例:**
午前10時30分 - 最初のメッセージ (セッションAは午前10時に開始)
午後3時00分 - セッションAが期限切れ (5時間後)

午後12時15分 - 最初のメッセージ (セッションBは午後12時に開始)
午後5時15分 - セッションBが期限切れ (5時間後午後5時)


#### バーンレート計算

モニターは、洗練された分析を使用してバーンレートを計算します。

1. **データ収集**: 過去1時間のすべてのセッションからトークン使用量を収集
2. **パターン分析**: 重複するセッション全体の消費トレンドを特定
3. **速度追跡**: 1分あたりの消費トークン数を計算
4. **予測エンジン**: 現在のセッションのトークンがいつ枯渇するかを推定
5. **リアルタイム更新**: 使用パターンが変化するにつれて予測を調整

### プランごとのトークン制限

#### v3.0.0 更新されたプラン制限

| プラン | 制限 (トークン) | コスト制限 | メッセージ | アルゴリズム |
|------|----------------|------------------|----------|-----------|
| **Claude Pro** | 19,000 | $18.00 | 250 | 固定制限 |
| **Claude Max5** | 88,000 | $35.00 | 1,000 | 固定制限 |
| **Claude Max20** | 220,000 | $140.00 | 2,000 | 固定制限 |
| **Custom** | P90ベース | (デフォルト) $50.00 | 250+ | 機械学習 |

#### 高度な制限検出

- **P90分析**: 履歴使用量の90パーセンタイルを使用
- **信頼度しきい値**: 制限検出の95%の精度
- **キャッシュサポート**: キャッシュ作成と読み取りトークンコストを含む
- **モデル固有**: Claude 3.5、Claude 4、および将来のモデルに適応

### 技術要件

#### 依存関係 (v3.0.0)

```toml
# コア依存関係 (自動的にインストールされます)
pytz>=2023.3                # タイムゾーン処理
rich>=13.7.0                # リッチターミナルUI
pydantic>=2.0.0             # タイプ検証
pydantic-settings>=2.0.0    # 設定管理
numpy>=1.21.0               # 統計計算
sentry-sdk>=1.40.0          # エラー報告 (オプション)
pyyaml>=6.0                 # 設定ファイル
tzdata                      # Windows タイムゾーンデータ
```

#### Python要件

- **最小**: Python 3.9+
- **推奨**: Python 3.11+
- **テスト済み**: Python 3.9, 3.10, 3.11, 3.12, 3.13

### スマート検出機能

#### 自動プラン切り替え

デフォルトのProプランを使用している場合:

1. **検出**: モニターがトークン使用量が7,000を超えることを検出
2. **分析**: 以前のセッションで実際の制限をスキャン
3. **切り替え**: 自動的に custom_max モードに切り替え
4. **通知**: 変更に関する明確なメッセージを表示
5. **継続**: 新しい、より高い制限で監視を継続

#### 制限検出プロセス

自動検出システム:

1. **履歴をスキャン**: 利用可能なすべてのセッションブロックを検査
2. **ピークを検出**: 達成された最高のトークン使用量を特定
3. **データを検証**: データ品質と鮮度を保証
4. **制限を設定**: 検出された最大値を新しい制限として使用
5. **パターンを学習**: 実際の使用能力に適応

## 🚀 使用例

### 一般的なシナリオ

#### 🌅 朝型開発者
**シナリオ**: 午前9時に作業を開始し、トークンをスケジュールに合わせてリセットしたい。

```bash
# カスタムリセット時間を午前9時に設定
./claude_monitor.py --reset-hour 9

# タイムゾーンを指定
./claude_monitor.py --reset-hour 9 --timezone US/Eastern
```


**利点**:
- リセット時間が作業スケジュールと一致
- 毎日のトークン割り当ての計画が容易に
- 予測可能なセッションウィンドウ

#### 🌙 夜型コーダー
**シナリオ**: 真夜中を過ぎて作業することが多く、柔軟なリセットスケジュールが必要。

```bash
# 毎日の境界を明確にするために真夜中にリセット
./claude_monitor.py --reset-hour 0

# 深夜のリセット (午後11時)
./claude_monitor.py --reset-hour 23
```


**戦略**:
- リセット時間に合わせて大量のコーディングセッションを計画
- 深夜の作業セッションをまたぐために遅いリセットを使用
- ピーク時のバーンレートを監視

#### 🔄 変動する制限を持つヘビーユーザー
**シナリオ**: トークン制限が変更されるようで、正確なプランがわからない。

```bash
# 以前の最高使用量を自動検出
claude-monitor-ja --plan custom_max

# カスタムスケジューリングで監視
claude-monitor-ja --plan custom_max --reset-hour 6
```


**アプローチ**:
- 自動検出に実際の制限を見つけさせる
- パターンを理解するために1週間監視
- 制限が変更またはリセットされたときにメモする

#### 🌍 国際的なユーザー
**シナリオ**: 異なるタイムゾーンで作業している、または旅行中。

```bash
# 米国東海岸
claude-monitor-ja --timezone America/New_York

# ヨーロッパ
claude-monitor-ja --timezone Europe/London

# アジア太平洋
claude-monitor-ja --timezone Asia/Singapore

# 国際チーム連携のためのUTC
claude-monitor-ja --timezone UTC --reset-hour 12
```


#### ⚡ クイックチェック
**シナリオ**: 設定なしで現在のステータスを確認したいだけ。

```bash
# デフォルトで実行
claude-monitor-ja

# ステータス確認後、Ctrl+C を押して終了
```

#### 📊 使用状況分析ビュー
**シナリオ**: さまざまな期間でのトークン使用パターンを分析する。

```bash
# 詳細な統計情報を含む日次使用状況の内訳を表示
claude-monitor-ja --view daily

# 月次トークン消費トレンドを分析
claude-monitor-ja --view monthly --plan max20

# 分析のために日次使用状況データをログファイルにエクスポート
claude-monitor-ja --view daily --log-file ~/daily-usage.log

# 異なるタイムゾーンで使用状況を確認
claude-monitor-ja --view daily --timezone America/New_York
```

**ユースケース**:
- **リアルタイム**: 現在のセッションとバーンレートのライブ監視
- **日次**: 日次消費パターンを分析し、ピーク使用日を特定
- **月次**: 長期的なトレンド分析と月次予算計画

### プラン選択戦略

#### プランの選択方法

**デフォルトから開始 (新規ユーザーに推奨)**
```bash
# 自動切り替え付きProプラン検出
claude-monitor-ja
```

- モニターはPro制限を超えたかどうかを検出します
- 必要に応じて自動的に custom_max に切り替えます
- 切り替え時に通知を表示します

**既知のサブスクリプションユーザー**
```bash
# Max5 を持っていることがわかっている場合
claude-monitor-ja --plan max5

# Max20 を持っていることがわかっている場合
claude-monitor-ja --plan max20
```


**不明な制限**
```bash
# 以前の使用状況から自動検出
claude-monitor-ja --plan custom_max
```


### ベストプラクティス

#### セットアップのベストプラクティス

1. **セッションの早い段階で開始**

```bash
   # Claude 作業を開始するときに監視を開始 (uv インストール)
   claude-monitor-ja

   # または開発モード
   ./claude_monitor.py
   ```

   - 最初から正確なセッション追跡が可能
   - バーンレート計算の精度向上
   - 制限接近の早期警告

2. **最新のインストールを使用 (推奨)**

```bash
   # uv で簡単にインストールと更新
   uv tool install claude-monitor-ja
   claude-monitor-ja --plan max5
   ```

   - クリーンなシステムインストール
   - 簡単な更新とメンテナンス
   - どこからでも利用可能

3. **カスタムシェルエイリアス (レガシー設定)**

```bash
   # ~/.bashrc または ~/.zshrc に追加 (開発設定のみ)
   alias claude-monitor-ja='cd ~/Claude-Code-Usage-Monitor && source venv/bin/activate && ./claude_monitor.py'
   ```


#### 使用方法のベストプラクティス

1. **バーンレート速度の監視**
   - トークン消費量の急激な増加に注意
   - 残り時間に基づいてコーディング強度を調整
   - セッションリセットに合わせて大規模なリファクタリングを計画

2. **戦略的なセッション計画**

```bash
   # リセット時間に合わせて大量の使用を計画
   claude-monitor-ja --reset-hour 9
   ```

   - リセット後に大規模なタスクをスケジュール
   - 制限に近づいている場合は軽いタスクを使用
   - 複数の重複するセッションを活用

3. **タイムゾーンの認識**

```bash
   # 常に実際のタイムゾーンを使用
   claude-monitor-ja --timezone Europe/Warsaw
   ```

   - 正確なリセット時間の予測
   - 作業スケジュールの計画が容易に
   - 正しいセッション期限切れの推定

#### 最適化のヒント

1. **ターミナル設定**
   - 幅が80文字以上のターミナルを使用
   - 視覚的なフィードバックを向上させるために色サポートを有効にする (COLORTERM 環境変数をチェック)
   - 監視専用のターミナルウィンドウを検討
   - 最高のテーマ体験のためにトゥルーカラーサポートのあるターミナルを使用

2. **ワークフロー統合**

```bash
   # 開発セッションで監視を開始 (uv インストール)
   tmux new-session -d -s claude-monitor-ja 'claude-monitor-ja'

   # または開発モード
   tmux new-session -d -s claude-monitor-ja './claude_monitor.py'

   # いつでもステータスを確認
   tmux attach -t claude-monitor-ja
   ```


3. **マルチセッション戦略**
   - セッションは正確に5時間続くことを覚えておく
   - 複数の重複するセッションを持つことができる
   - セッション境界をまたいで作業を計画する

#### 実世界のワークフロー

**大規模プロジェクト開発**
```bash
# 持続的な開発のためのセットアップ
claude-monitor-ja --plan max20 --reset-hour 8 --timezone America/New_York
```


**日課**:
1. **午前8時**: 新しいトークン、主要な機能を開始
2. **午前10時**: バーンレートを確認し、強度を調整
3. **午後12時**: 午後のセッション計画のために監視
4. **午後2時**: 新しいセッションウィンドウ、複雑な問題に取り組む
5. **午後4時**: 軽いタスク、夜のセッションの準備

**学習と実験**
```bash
# 学習のための柔軟なセットアップ
claude-monitor-ja --plan pro
```


**スプリント開発**
```bash
# 高強度開発セットアップ
claude-monitor-ja --plan max20 --reset-hour 6
```


## 🔧 開発インストール

ソースコードを扱いたい貢献者や開発者向け:

### クイックスタート (開発/テスト)

```bash
# リポジトリをクローン
git clone https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor.git
cd Claude-Code-Usage-Monitor

# 開発モードでインストール
pip install -e .

# ソースから実行
python -m claude_monitor
```


### v3.0.0 テスト機能

新バージョンには、包括的なテストスイートが含まれています。

- **100以上のテストケース**と完全なカバレッジ
- すべてのコンポーネントの**単体テスト**
- エンドツーエンドワークフローの**統合テスト**
- ベンチマーク付きの**パフォーマンステスト**
- 隔離されたテストのための**モックオブジェクト**

```bash
# テストを実行
cd src/
python -m pytest

# カバレッジ付きで実行
python -m pytest --cov=claude_monitor --cov-report=html

# 特定のテストモジュールを実行
python -m pytest tests/test_analysis.py -v
```


### 前提条件

1. システムに**Python 3.9+**がインストールされていること
2. リポジトリをクローンするための**Git**

### 仮想環境のセットアップ

#### なぜ仮想環境を使用するのか？

仮想環境の使用は**強く推奨されます**。その理由は次のとおりです。

- **🛡️ 隔離**: システムのPythonをクリーンに保ち、依存関係の競合を防ぎます
- **📦 ポータビリティ**: 異なるマシンで正確な環境を簡単に再現できます
- **🔄 バージョン管理**: 安定性のために特定のバージョンの依存関係をロックできます
- **🧹 クリーンなアンインストール**: 仮想環境フォルダを削除するだけで、すべてを削除できます
- **👥 チームコラボレーション**: 全員が同じPythonとパッケージバージョンを使用します

#### virtualenv のインストール (必要な場合)

venv モジュールが利用できない場合:

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-venv

# Fedora/RHEL/CentOS
sudo dnf install python3-venv

# macOS (通常はPythonに付属)
# 利用できない場合は、Homebrew 経由で Python をインストール:
brew install python3

# Windows (通常はPythonに付属)
# 利用できない場合は、python.org から Python を再インストール
# インストール中に「Add Python to PATH」をチェックしてください
```


または、virtualenv パッケージを使用します。
```bash
# pip 経由で virtualenv をインストール
pip install virtualenv

# その後、次のコマンドで仮想環境を作成します:
virtualenv venv
# 代わりに: python3 -m venv venv
```


#### ステップバイステップのセットアップ

```bash
# 1. リポジトリをクローン
git clone https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor.git
cd Claude-Code-Usage-Monitor

# 2. 仮想環境を作成
python3 -m venv venv
# または virtualenv パッケージを使用する場合:
# virtualenv venv

# 3. 仮想環境をアクティブ化
# Linux/Macの場合:
source venv/bin/activate
# Windowsの場合:
# venv\Scripts\activate

# 4. Python の依存関係をインストール
pip install pytz
pip install rich>=13.0.0
# 5. スクリプトを実行可能にする (Linux/Macのみ)
chmod +x claude_monitor.py

# 6. モニターを実行
python claude_monitor.py
```


#### 日常の使用

初期設定後、必要なのは次のコマンドだけです。

```bash
# プロジェクトディレクトリに移動
cd Claude-Code-Usage-Monitor

# 仮想環境をアクティブ化
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# モニターを実行
./claude_monitor.py  # Linux/Mac
# python claude_monitor.py  # Windows

# 完了したら、非アクティブ化
deactivate
```


#### プロのヒント: シェルエイリアス

クイックアクセス用のエイリアスを作成します。
```bash
# ~/.bashrc または ~/.zshrc に追加
alias claude-monitor-ja='cd ~/Claude-Code-Usage-Monitor && source venv/bin/activate && ./claude_monitor.py'

# その後、実行するだけ:
claude-monitor-ja
```


## トラブルシューティング

### インストールに関する問題

#### 「externally-managed-environment」エラー

最新のLinuxディストリビューション (Ubuntu 23.04+, Debian 12+, Fedora 38+) では、次のエラーが発生する場合があります。
```
error: externally-managed-environment
× This environment is externally managed
```


**解決策 (推奨順):**

1. **uv を使用する (推奨)**

```bash
   # まず uv をインストール
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # その後 uv でインストール
   uv tool install claude-monitor-ja
   ```


2. **pipx を使用する (隔離された環境)**

```bash
   # pipx をインストール
   sudo apt install pipx  # Ubuntu/Debian
   # または
   python3 -m pip install --user pipx

   # claude-monitor-ja をインストール
   pipx install claude-monitor-ja
   ```


3. **仮想環境を使用する**

```bash
   python3 -m venv myenv
   source myenv/bin/activate
   pip install claude-monitor-ja
   ```


4. **強制インストール (非推奨)**

```bash
   pip install --user claude-monitor-ja --break-system-packages
   ```

   ⚠️ **警告**: これはシステム保護をバイパスし、競合を引き起こす可能性があります。代わりに仮想環境を使用することを強くお勧めします。

#### pip インストール後にコマンドが見つからない

pip インストール後に claude-monitor-ja コマンドが見つからない場合:

1. **PATH の問題かどうかを確認**

```bash
   # pip インストール中に警告メッセージを探します:
   # WARNING: The script claude-monitor-ja is installed in '/home/username/.local/bin' which is not on PATH
   ```


2. **PATH に追加**

```bash
   # ~/.bashrc または ~/.zshrc に追加
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

   # シェルを再読み込み
   source ~/.bashrc  # または source ~/.zshrc
   ```


3. **インストール場所を確認**

```bash
   # pip がスクリプトをインストールした場所を見つける
   pip show -f claude-monitor-ja | grep claude-monitor-ja
   ```


4. **Python で直接実行**

```bash
   python3 -m claude_monitor
   ```


#### Python バージョンの競合

複数のPythonバージョンがある場合:

1. **Python バージョンを確認**

```bash
   python3 --version
   pip3 --version
   ```


2. **特定の Python バージョンを使用**

```bash
   python3.11 -m pip install claude-monitor-ja
   python3.11 -m claude_monitor
   ```


3. **uv を使用する (Python バージョンを自動的に処理)**

```bash
   uv tool install claude-monitor-ja
   ```


### 実行時の問題

#### アクティブなセッションが見つかりません

「No active session found」エラーが発生した場合は、次の手順に従ってください。

1. **初期テスト**:
   Claude Code を起動し、少なくとも2つのメッセージを送信します。場合によっては、最初の試行でセッションが正しく初期化されないことがありますが、数回のやり取りで解決します。

2. **設定パス**:
   問題が解決しない場合は、カスタム設定パスを指定することを検討してください。デフォルトでは、Claude Code は ~/.config/claude を使用します。環境によっては、このパスを調整する必要がある場合があります。

```bash
CLAUDE_CONFIG_DIR=~/.config/claude ./claude_monitor.py
```



## 📞 お問い合わせ

質問、提案、または共同作業をご希望ですか？お気軽にお問い合わせください！

**📧 メール**: [maciek@roboblog.eu](mailto:maciek@roboblog.eu)

セットアップに関するヘルプが必要な場合、機能リクエストがある場合、バグを見つけた場合、または潜在的な改善点について議論したい場合でも、お気軽にご連絡ください。Claude Code Usage Monitor のユーザーからのご意見をお待ちしております！


## 📚 その他のドキュメント

- **[開発ロードマップ](DEVELOPMENT.md)** - ML機能、PyPIパッケージ、Dockerプラン
- **[貢献ガイド](CONTRIBUTING.md)** - 貢献方法、開発ガイドライン
- **[トラブルシューティング](TROUBLESHOOTING.md)** - 一般的な問題と解決策


## 📝 ライセンス

[MITライセンス](LICENSE) - 必要に応じて自由に使用および変更してください。

## 🤝 貢献者

- [@adawalli](https://github.com/adawalli)
- [@taylorwilsdon](https://github.com/taylorwilsdon)
- [@moneroexamples](https://github.com/moneroexamples)

貢献したいですか？[貢献ガイド](CONTRIBUTING.md) を確認してください！


## 🙏 謝辞

### スポンサー

このプロジェクトの継続を支援してくださるサポーターに感謝いたします。

**Ed** - *Buy Me Coffee サポーター*
> 「あなたの作品を世界と共有してくださることに感謝しています。それは私が日々の作業を続けるのに役立っています。質の高いREADME、そして全体的に本当に良いものです！」

## スター履歴

[![Star History Chart](https://api.star-history.com/svg?repos=Maciek-roboblog/Claude-Code-Usage-Monitor&type=Date)](https://www.star-history.com/#Maciek-roboblog/Claude-Code-Usage-Monitor&Date)

---

<div align="center">

**⭐ このリポジトリが役に立ったらスターを付けてください！ ⭐**

[バグを報告](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/issues) • [機能をリクエスト](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor/issues) • [貢献する](CONTRIBUTING.md)

</div>