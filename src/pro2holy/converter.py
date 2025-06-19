import base64
from pathlib import Path
from bs4 import BeautifulSoup


def converter(input_file: str, output_folder: str):
    path = Path(input_file)
    filename = path.stem

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
