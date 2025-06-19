import argparse
from pathlib import Path
from pro2holy.converter import converter, folder_converter
import os
import sys


def main():
    try:
        parser = argparse.ArgumentParser(
            description="Conversor de arquivo ProPresenter para o formato Holyrics."
        )
        parser.add_argument("input", help="Caminho para o arquivo .pro6")
        parser.add_argument("output_dir", help="Pasta onde o arquivo Holyrics .txt será salvo")

        args = parser.parse_args()

        input = Path(args.input)
        output_dir = Path(args.output_dir)

        assert input.exists(), "O caminho de entrada não existe"
        assert not output_dir.is_file(), "O caminho de saida digitado é um arquivo"

        os.makedirs(args.output_dir, exist_ok=True)

        if (input.is_dir()):
            folder_converter(args.input, args.output_dir)
        else:
            converter(args.input, args.output_dir)

        print(f"Arquivo convertido e salvo em: {output_dir.resolve()}")
    except AssertionError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)
