# カラーテキストスクリプト

このPythonスクリプトは、カスタマイズ可能な色、装飾文字、および繰り返しパターンで文字列を出力することができます。ANSIエスケープコードを使用してテキストを装飾し、コマンドラインでオプションを指定して実行します。

---

## 特徴

- **カスタマイズ可能なテキスト出力：** 表示する文字列を指定可能。
- **文字色および背景色の指定：** 定義済みの色と背景色から選択可能。
- **装飾文字の追加：** テキストを装飾文字で囲むことができます。
- **繰り返し回数の指定：** 装飾文字を指定回数繰り返します。

---

## 必要条件

- Python 3.x がインストールされていること。

---

## 使用方法

### コマンドラインオプション

スクリプトは以下のコマンドライン引数を受け取ります：

| 引数         | 必須   | デフォルト | 説明 |
|--------------|--------|------------|------|
| `--text`     | 必須   | なし       | 表示する文字列（例: "Hello"）。 |
| `--color`    | 必須   | WHITE      | テキストまたは背景の色を指定します。選択可能な値： `BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`, `BG_BLACK`, `BG_RED`, `BG_GREEN`, `BG_YELLOW`, `BG_BLUE`, `BG_MAGENTA`, `BG_CYAN`, `BG_WHITE`。 |
| `--line`     | 任意   | `-`        | テキストの左右に挟む装飾文字。 |
| `--count`    | 任意   | `10`       | 装飾文字の繰り返し回数。 |

---

### コマンド例

1. 赤色の文字を表示：
   ```bash
   python script.py --text="Hello World" --color="RED"
   ```

2. テキストを装飾文字で囲む：
   ```bash
   python script.py --text="Welcome" --color="BLUE" --line="*" --count=5
   ```
   出力：
   ```
   ***** Welcome *****
   ```

3. 背景色を変更：
   ```bash
   python script.py --text="Notice" --color="BG_YELLOW"
   ```

4. 実行例：
   ```bash
   ./bin/print.exe --text=Hello --color=YELLOW
   ```

---

## 色の詳細

| コード          | 説明 |
|-----------------|------|
| `BLACK`        | (文字) 黒 |
| `RED`          | (文字) 赤 |
| `GREEN`        | (文字) 緑 |
| `YELLOW`       | (文字) 黄 |
| `BLUE`         | (文字) 青 |
| `MAGENTA`      | (文字) マゼンタ |
| `CYAN`         | (文字) シアン |
| `WHITE`        | (文字) 白 |
| `BG_BLACK`     | (背景) 黒 |
| `BG_RED`       | (背景) 赤 |
| `BG_GREEN`     | (背景) 緑 |
| `BG_YELLOW`    | (背景) 黄 |
| `BG_BLUE`      | (背景) 青 |
| `BG_MAGENTA`   | (背景) マゼンタ |
| `BG_CYAN`      | (背景) シアン |
| `BG_WHITE`     | (背景) 白 |

---

## 動作仕組み

### ANSIカラーコード

スクリプトはANSIエスケープコードを使用してテキストに色を適用します。利用可能な色は `color_codes` 辞書で定義されています：

```python
color_codes = {
    'BLACK': '\033[30m',
    'RED': '\033[31m',
    'GREEN': '\033[32m',
    'YELLOW': '\033[33m',
    'BLUE': '\033[34m',
    'MAGENTA': '\033[35m',
    'CYAN': '\033[36m',
    'WHITE': '\033[37m',
    'BG_BLACK': '\033[40m',
    'BG_RED': '\033[41m',
    'BG_GREEN': '\033[42m',
    'BG_YELLOW': '\033[43m',
    'BG_BLUE': '\033[44m',
    'BG_MAGENTA': '\033[45m',
    'BG_CYAN': '\033[46m',
    'BG_WHITE': '\033[47m',
    'RESET': '\033[0m'
}
```

### 関数

`print_colored_text` 関数は装飾付きのテキストを生成して出力します：

```python
def print_colored_text(text, color, line, count):
    color_code = color_codes.get(color.upper(), color_codes['RESET'])
    print(f"{color_code}{line * count} {text} {line * count}{color_codes['RESET']}")
```

