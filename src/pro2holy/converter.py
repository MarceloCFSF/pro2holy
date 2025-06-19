import base64
from pathlib import Path
from bs4 import BeautifulSoup


def converter(input_file: str, output_folder: str):
    input_path = Path(input_file)
    filename = input_path.stem

    output_path = Path(output_folder)

    # assert output_path.is_dir(), "O caminho de saída não é um diretório"

    with open(input_file, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "xml")

    lyrics = soup.find_all("NSString", attrs={"rvXMLIvarName": "PlainText"})

    content = ""

    for line in lyrics:
        decoded_bytes = base64.b64decode(line.text)
        content += decoded_bytes.decode("utf-8")
        content += "\n\n"

    with open(f"{output_folder}/{filename}.txt", "w", encoding="utf-8") as f:
        f.write(content)

def folder_converter(input_folder: str, output_folder: str):
    directory = Path(input_folder)
    pro6_files = list(directory.glob("*.pro6"))

    for file in pro6_files:
        converter(f"{input_folder}/{file.name}", output_folder)
