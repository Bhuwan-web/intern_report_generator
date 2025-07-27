#!/usr/bin/env python3
"""
Main script for IOST BSc CSIT Internship Report Formatter
Combines document formatting, language checking, citation analysis, and auto-fixing
"""

import sys
import os
from document_formatter import IOSTDocumentFormatter
from academic_tools import analyze_document
from enhanced_academic_tools import auto_fix_document
from page_break_manager import optimize_document_breaks
from spacing_optimizer import optimize_document_spacing


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
        print("  breaks    - Optimize page breaks and remove unnecessary breaks")
        print("  spacing   - Optimize spacing between sections, headings, and content")
        print(
            "  complete  - Full optimization: autofix, breaks, spacing, and format (recommended)"
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
        # Auto-fix first (if requested)
        if action in ["autofix", "complete"]:
            print("\n🤖 AUTO-FIXING LANGUAGE & CITATIONS")
            print("-" * 40)
            auto_fix_document(document_path)
            # Update document path to use the auto-fixed version for further processing
            base_name = os.path.splitext(os.path.basename(document_path))[0]
            document_path = f"auto_fixed_{base_name}.docx"

        # Optimize page breaks
        if action in ["breaks", "complete"]:
            print("\n📄 OPTIMIZING PAGE BREAKS")
            print("-" * 35)
            base_name = os.path.splitext(os.path.basename(document_path))[0]
            if action == "complete":
                optimized_path = f"breaks_optimized_{base_name}.docx"
            else:
                optimized_path = f"page_optimized_{base_name}.docx"

            result = optimize_document_breaks(document_path, optimized_path)
            if result:
                document_path = result  # Use optimized version for further processing
                print(f"✅ Page breaks optimized: {optimized_path}")

        # Optimize spacing
        if action in ["spacing", "complete"]:
            print("\n📏 OPTIMIZING SPACING")
            print("-" * 25)
            base_name = os.path.splitext(os.path.basename(document_path))[0]
            if action == "complete":
                spacing_path = f"spacing_optimized_{base_name}.docx"
            else:
                spacing_path = f"spacing_optimized_{base_name}.docx"

            result, stats = optimize_document_spacing(document_path, spacing_path)
            if result:
                document_path = result  # Use spacing-optimized version for further processing
                print(f"✅ Spacing optimized: {spacing_path}")

        # Format document
        if action in ["format", "both", "complete"]:
            print("\n🔧 FORMATTING DOCUMENT")
            print("-" * 30)
            formatter = IOSTDocumentFormatter(document_path)
            formatter.format_document()

            base_name = os.path.splitext(os.path.basename(document_path))[0]
            if action == "complete":
                output_path = f"final_{base_name}.docx"
            else:
                output_path = f"formatted_{base_name}.docx"
            formatter.save_document(output_path)

            print(f"✅ Formatted document saved as: {output_path}")

        # Analyze document
        if action in ["analyze", "both", "complete"]:
            print("\n🔍 ANALYZING DOCUMENT")
            print("-" * 30)
            analyze_document(document_path)

        print("\n" + "=" * 50)
        print("PROCESSING COMPLETED!")
        print("=" * 50)

        # Show output files
        if action == "complete":
            base_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
            print(f"📄 Auto-fixed document: auto_fixed_{base_name}.docx")
            print(f"📄 Page-optimized document: breaks_optimized_auto_fixed_{base_name}.docx")
            print(
                f"📄 Spacing-optimized document: spacing_optimized_breaks_optimized_auto_fixed_{base_name}.docx"
            )
            print(
                f"📄 Final formatted document: final_spacing_optimized_breaks_optimized_auto_fixed_{base_name}.docx"
            )
        elif action in ["format", "both"]:
            base_name = os.path.splitext(os.path.basename(document_path))[0]
            print(f"📄 Formatted document: formatted_{base_name}.docx")
        elif action == "autofix":
            base_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
            print(f"📄 Auto-fixed document: auto_fixed_{base_name}.docx")
        elif action == "breaks":
            base_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
            print(f"📄 Page-optimized document: page_optimized_{base_name}.docx")
        elif action == "spacing":
            base_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
            print(f"📄 Spacing-optimized document: spacing_optimized_{base_name}.docx")

        print("\n📋 NEXT STEPS:")
        if action == "complete":
            print("1. Review the final document for accuracy")
            print("2. Manually adjust page numbering (Roman/Arabic)")
            print("3. Add proper page breaks for chapters")
            print("4. Verify figure and table positioning")
            print("5. Check that auto-fixes maintain original meaning")
        else:
            print("1. Review the processed document in Microsoft Word")
            print("2. Manually adjust page numbering (Roman/Arabic)")
            print("3. Add proper page breaks for chapters")
            print("4. Verify figure and table positioning")
            print("5. Use citation management tools for references")

    except Exception as e:
        print(f"❌ Error processing document: {str(e)}")


if __name__ == "__main__":
    main()
