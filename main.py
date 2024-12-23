import argparse

# 色と背景色の設定
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

def print_colored_text(text, color, line, count, no_line):
    color_code = color_codes.get(color.upper(), color_codes['RESET'])
    if not no_line:
        print(f"{color_code}{line * count} {text} {line * count}{color_codes['RESET']}")
    else:
        print(f"{color_code}{text}{color_codes['RESET']}")

def main():
    parser = argparse.ArgumentParser(
        description="指定した文字列を指定した色で装飾して出力します。",
        epilog="使用例: python script.py --text='Hello' --color='RED' --line='*' --count=5"
    )
    parser.add_argument(
        '--text',
        required=True,
        help='表示する文字列（例: "Hello"）'
    )
    parser.add_argument(
        '--color',
        required=False,
        default='WHITE',
        choices=[
            'BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 
            'MAGENTA', 'CYAN', 'WHITE', 'BG_BLACK', 'BG_RED', 
            'BG_GREEN', 'BG_YELLOW', 'BG_BLUE', 'BG_MAGENTA', 
            'BG_CYAN', 'BG_WHITE'
        ],
        help='文字色または背景色を指定します（例: "RED"、"BG_BLUE"）。利用可能な色: '
             'BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, '
             'BG_BLACK, BG_RED, BG_GREEN, BG_YELLOW, BG_BLUE, BG_MAGENTA, BG_CYAN, BG_WHITE'
    )
    parser.add_argument(
        '--line',
        required=False,
        default='-',
        help='文字列の左右に挟む装飾文字（デフォルトは "-"）。'
    )
    parser.add_argument(
        '--count',
        type=int,
        default=10,
        help='装飾文字の繰り返し回数（デフォルトは 10）。'
    )
    parser.add_argument(
        '--no_line',
        action='store_true',
        help='左右の文字を表示するか（デフォルトは表示される）。'
    )

    args = parser.parse_args()
    
    # 色付きで文字を表示
    print_colored_text(args.text, args.color, args.line, args.count, args.no_line)

if __name__ == '__main__':
    main()
