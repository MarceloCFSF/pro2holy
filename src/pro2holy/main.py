import argparse
from pro2holy.converter import converter
import os


def main():
    parser = argparse.ArgumentParser(
        description="Conversor de arquivo ProPresenter para o formato Holyrics."
    )
    parser.add_argument("input", help="Caminho para o arquivo .pro6")
    parser.add_argument("output_dir", help="Pasta onde o arquivo Holyrics .txt será salvo")

    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    output = converter(args.input, args.output_dir)

    print(f"Arquivo convertido e salvo em: {output}")
