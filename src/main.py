#!/usr/bin/env python3
"""
Main script for IOST BSc CSIT Internship Report Formatter
Combines document formatting, language checking, citation analysis, and auto-fixing
"""

import sys
import os
from document_formatter import IOSTDocumentFormatter
from academic_tools import analyze_document
from academic_line_break_manager import process_document_line_breaks

try:
    from integrated_academic_tools import process_document_integrated as auto_fix_document

    print("🔧 Using integrated analysis and correction tools")
    AI_AVAILABLE = True
except ImportError:
    try:
        from enhanced_academic_tools import auto_fix_document

        print("🤖 Using enhanced AI tools")
        AI_AVAILABLE = True
    except ImportError:
        from lightweight_academic_tools import auto_fix_document

        print("📝 Using lightweight rule-based tools")
        AI_AVAILABLE = False


def main():
    if len(sys.argv) < 2:
        print("IOST BSc CSIT Internship Report Formatter")
        print("=" * 50)
        print("Usage:")
        print("  python main.py <document.docx> [options]")
        print("\nOptions:")
        print("  format    - Format document according to IOST guidelines")
        print("  analyze   - Analyze language and citations")
        print("  autofix   - Automatically fix common language/citation issues")
        print("  linebreaks - Apply academic line break standards")
        print("  breaks    - Optimize page breaks and remove unnecessary breaks")
        print("  spacing   - Optimize spacing between sections, headings, and content")
        print(
            "  complete  - Full optimization: autofix, linebreaks, breaks, spacing, and format (recommended)"
        )
        print("  both      - Format and analyze only")
        print("\nExamples:")
        print("  python main.py my_report.docx")
        print("  python main.py my_report.docx complete")
        print("  python main.py my_report.docx spacing")
        print("  python main.py my_report.docx breaks")
        print("  python main.py my_report.docx autofix")
        return

    document_path = sys.argv[1]
    action = sys.argv[2] if len(sys.argv) > 2 else "complete"

    if not os.path.exists(document_path):
        print(f"Error: File '{document_path}' not found!")
        return

    if not document_path.endswith(".docx"):
        print("Error: Please provide a .docx file")
        return

    print("IOST BSc CSIT Internship Report Processor")
    print("=" * 50)

    try:
        base_name = os.path.splitext(os.path.basename(document_path))[0]
        final_path = f"final_{base_name}.docx"

        if action == "complete":
            print("\n🤖 AUTO-FIXING LANGUAGE & CITATIONS")
            print("-" * 40)
            auto_fix_document(document_path, output_path=final_path)
            # All further steps operate on final_path
            working_path = final_path

            print("\n📏 APPLYING ACADEMIC LINE BREAKS")
            print("-" * 40)
            process_document_line_breaks(working_path, output_path=final_path)
            working_path = final_path

            print("\n🔧 FORMATTING DOCUMENT")
            print("-" * 30)
            formatter = IOSTDocumentFormatter(final_path)
            formatter.format_document()
            formatter.save_document(final_path)

            print(f"✅ Final formatted document saved as: {final_path}")

            print("\n🔍 ANALYZING DOCUMENT")
            print("-" * 30)
            analyze_document(final_path)

            print("\n" + "=" * 50)
            print("PROCESSING COMPLETED!")
            print("=" * 50)
            print(f"📄 Final document: {final_path}")
            print("\n📋 NEXT STEPS:")
            print("1. Review the final document for accuracy")
            print("2. Manually adjust page numbering (Roman/Arabic)")
            print("3. Add proper page breaks for chapters")
            print("4. Verify figure and table positioning")
            print("5. Check that auto-fixes maintain original meaning")

        else:
            # Keep previous logic for other actions
            # ...existing code for autofix, breaks, spacing, format, both, analyze...
            if action == "autofix":
                print("\n🤖 AUTO-FIXING LANGUAGE & CITATIONS")
                print("-" * 40)
                auto_fix_document(document_path)
                base_name = os.path.splitext(os.path.basename(document_path))[0]
                print(f"📄 Auto-fixed document: auto_fixed_{base_name}.docx")
            if action == "linebreaks":
                print("\n📏 APPLYING ACADEMIC LINE BREAKS")
                print("-" * 40)
                process_document_line_breaks(document_path)
                base_name = os.path.splitext(os.path.basename(document_path))[0]
                print(f"📄 Line break optimized document: line_break_fixed_{base_name}.docx")
            if action in ["format", "both"]:
                print("\n� FORMATTING DOCUMENT")
                print("-" * 30)
                formatter = IOSTDocumentFormatter(document_path)
                formatter.format_document()
                output_path = f"formatted_{base_name}.docx"
                formatter.save_document(output_path)
                print(f"📄 Formatted document: {output_path}")
            if action in ["analyze", "both"]:
                print("\n🔍 ANALYZING DOCUMENT")
                print("-" * 30)
                analyze_document(document_path)

            print("\n" + "=" * 50)
            print("PROCESSING COMPLETED!")
            print("=" * 50)

    except Exception as e:
        print(f"❌ Error processing document: {str(e)}")


if __name__ == "__main__":
    main()
