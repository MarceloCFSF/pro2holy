import os
from src.pro2holy.converter import converter


def read_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read().strip()


def test_converter():
    base_dir = os.path.dirname(__file__)
    propresenter = os.path.join(base_dir, "fixtures", "example.pro6")
    expected_file = os.path.join(base_dir, "fixtures", "expected.txt")
    output_file = os.path.join(base_dir, "example.txt")

    try:
        converter(propresenter, base_dir)

        assert os.path.exists(output_file), "Arquivo não foi gerado"

        excepted = read_file(expected_file)
        output = read_file(output_file)

        assert output == excepted, (
            "A conversão não gerou o conteúdo esperado para o Holyrics"
        )

    finally:
        if os.path.exists(output_file):
            os.remove(output_file)
