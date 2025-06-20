# Pro2Holy

A command-line tool to convert `.pro6` song files from ProPresenter 6 to Holyrics-compatible `.txt` files.

---

## ✨ Features

- Parses `.pro6` XML files
- Decodes base64 song text
- Outputs clean `.txt` format ready for Holyrics
- CLI usage via Poetry

---

## 🚀 Usage

### Run directly with Poetry:

```bash
poetry run pro2holy path/to/input.pro6 path/to/output_dir
```

- If <input> is a `.pro6` file: it converts that file only.

- If <input> is a directory: it converts all `.pro6` files in that folder to `.txt`.

### Example: convert a single file

```bash
poetry run pro2holy tests/fixtures/example.pro6 output/
```

## Example: convert all `.pro6` files in a folder

```bash
poetry run pro2holy tests/fixtures/ output/
```

---

## 🔧 Installation

Clone the project and install dependencies:

```bash

git clone https://github.com/seu-usuario/pro2holy.git
cd pro2holy
poetry install
```

---

## 📦 Project Structure

```
src/
├── pro2holy/
│   ├── main.py         # CLI script
│   ├── converter.py    # Core conversion logic
│   └── __init__.py
tests/
├── fixtures/           # Sample .pro6 files for testing
├── test_converter.py   # Unit tests

```

## 🧪 Running Tests

```bash
poetry run pytest
```

## 🛑 Disclaimer

This tool is intended for personal use only.

Do not upload copyrighted `.pro6` files or song lyrics to a public repository.
Always verify usage permissions before sharing converted files.
