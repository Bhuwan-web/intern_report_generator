#!/usr/bin/env python3
"""
Simple script to format documents using the IOST formatter
Usage: python format_document.py <input_file.docx>
"""

import sys
import os
from document_formatter import IOSTDocumentFormatter


def format_document(input_file, output_file=None):
    """Format a single document"""
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found!")
        return False

    try:
        print(f"Formatting document: {input_file}")
        formatter = IOSTDocumentFormatter(input_file)
        formatter.format_document()

        if output_file is None:
            base_name = os.path.splitext(os.path.basename(input_file))[0]
            output_file = f"formatted_{base_name}.docx"

        formatter.save_document(output_file)

        print(f"\n✅ Successfully formatted: {output_file}")
        return True

    except Exception as e:
        print(f"❌ Error formatting document: {str(e)}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python format_document.py <input_file.docx> [output_file.docx]")
        print("Example: python format_document.py my_report.docx")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    format_document(input_file, output_file)


if __name__ == "__main__":
    main()
