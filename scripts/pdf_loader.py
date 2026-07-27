"""
pdf_loader.py

Purpose:
    Load a PDF document, extract its text, and save the extracted
    text to the processed data directory.

Author:
    Rashid

Project:
    AI Literature Observatory
"""

from pathlib import Path

import fitz


# -----------------------------------------------------
# Project Directories
# -----------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


# -----------------------------------------------------
# PDF Loader
# -----------------------------------------------------

def load_pdf(pdf_path: Path) -> fitz.Document:
    """
    Open a PDF document.

    Parameters
    ----------
    pdf_path : Path
        Path to the PDF file.

    Returns
    -------
    fitz.Document
        Opened PDF document.
    """

    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {pdf_path}")

    return fitz.open(pdf_path)


# -----------------------------------------------------
# Text Extraction
# -----------------------------------------------------

def extract_text(document: fitz.Document) -> str:
    """
    Extract all text from a PDF.

    Parameters
    ----------
    document : fitz.Document

    Returns
    -------
    str
        Complete text from the PDF.
    """

    pages = []

    for page in document:
        pages.append(page.get_text())

    return "\n".join(pages)


# -----------------------------------------------------
# Save Output
# -----------------------------------------------------

def save_text(text: str, output_path: Path) -> None:
    """
    Save extracted text to a text file.
    """

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(text)


# -----------------------------------------------------
# Main
# -----------------------------------------------------

def main():

    pdf_file = RAW_DATA_DIR / "paper.pdf"

    output_file = PROCESSED_DATA_DIR / "paper.txt"

    print(f"Loading PDF: {pdf_file}")

    try:
        document = load_pdf(pdf_file)
    except FileNotFoundError as e:
        print(e)
        return

    print("Extracting text...")

    try:
        text = extract_text(document)
    finally:
        document.close()

    print("Saving output...")

    save_text(text, output_file)

    print(f"Done! Output saved to:\n{output_file}")


if __name__ == "__main__":
    main()