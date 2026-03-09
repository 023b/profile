"""
PDF to Image Converter
Converts all PDF files in a folder to PNG images, saved in the same folder.

Requirements:
    pip install pdf2image pillow
    Windows also needs poppler: https://github.com/oschwartz10612/poppler-windows/releases
    Extract it and set POPPLER_PATH below if not in system PATH.
"""

from pdf2image import convert_from_path
from pathlib import Path

# ── CONFIG ────────────────────────────────────────────────────────────────────
FOLDER = r"C:\Users\Arun\Downloads\ARUN\certificate images"
DPI = 200          # Higher = sharper image (150–300 is a good range)
FORMAT = "PNG"     # "PNG" for lossless, "JPEG" for smaller files
POPPLER_PATH = None  # e.g. r"C:\poppler\Library\bin" — set if not in PATH
# ─────────────────────────────────────────────────────────────────────────────


def pdf_to_images(folder: str, dpi: int, fmt: str, poppler_path):
    folder_path = Path(folder)
    pdf_files = list(folder_path.glob("*.pdf"))

    if not pdf_files:
        print(f"No PDF files found in: {folder_path}")
        return

    print(f"Found {len(pdf_files)} PDF file(s) in '{folder_path}'\n")

    for pdf_path in pdf_files:
        print(f"Converting: {pdf_path.name}")
        try:
            pages = convert_from_path(
                str(pdf_path),
                dpi=dpi,
                poppler_path=poppler_path,
            )

            for i, page in enumerate(pages, start=1):
                suffix = f"_page{i}" if len(pages) > 1 else ""
                out_name = f"{pdf_path.stem}{suffix}.{fmt.lower()}"
                out_path = folder_path / out_name
                page.save(str(out_path), fmt)
                print(f"  ✔ Saved: {out_name}")

        except Exception as e:
            print(f"  ✘ Failed: {pdf_path.name} — {e}")

    print("\nDone!")


if __name__ == "__main__":
    pdf_to_images(FOLDER, DPI, FORMAT, POPPLER_PATH)