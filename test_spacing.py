#!/usr/bin/env python3
"""
Test script specifically for spacing optimization functionality
"""

import sys
import os
from spacing_optimizer import SpacingOptimizer, optimize_document_spacing


def test_spacing_analysis():
    """Test spacing analysis on your document"""

    if not os.path.exists("my_report.docx"):
        print("❌ my_report.docx not found!")
        print("Please make sure your document is in the current directory")
        return False

    try:
        print("🔍 ANALYZING SPACING IN YOUR DOCUMENT")
        print("=" * 50)

        optimizer = SpacingOptimizer("my_report.docx")

        # Generate detailed spacing report
        optimizer.generate_spacing_report()

        print("\n🧪 TESTING SPACING OPTIMIZATION")
        print("=" * 50)

        # Test optimization
        result, stats = optimize_document_spacing(
            "my_report.docx", "test_spacing_optimized_report.docx"
        )

        if result and stats:
            print(f"\n✅ SUCCESS! Test spacing optimization completed")
            print(f"📄 Original: my_report.docx")
            print(f"📄 Spacing-optimized: test_spacing_optimized_report.docx")

            print(f"\n📊 OPTIMIZATION STATISTICS:")
            print(f"   🔍 Issues found: {stats['issues_found']}")
            print(f"   🧹 Empty paragraphs removed: {stats['empty_removed']}")
            print(f"   📏 Paragraphs optimized: {stats['paragraphs_optimized']}")
            print(f"   🔗 Heading-content pairs fixed: {stats['heading_content_fixed']}")

            print("\n💡 Compare both files in Word to see the spacing improvements:")
            print("   • Check spacing before/after chapter headings")
            print("   • Verify section and subsection spacing")
            print("   • Look for removed excessive empty paragraphs")
            print("   • Confirm consistent line spacing (1.5)")

            # Clean up test file
            if os.path.exists("test_spacing_optimized_report.docx"):
                print(f"\n🗑️  Test file created: test_spacing_optimized_report.docx")
                print("   You can delete this after reviewing")

            return True
        else:
            print("❌ Spacing optimization test failed")
            return False

    except Exception as e:
        print(f"❌ Error during spacing testing: {str(e)}")
        return False


def demonstrate_spacing_standards():
    """Show the IOST CSIT spacing standards being applied"""
    print("\n📋 IOST CSIT SPACING STANDARDS")
    print("=" * 40)
    print("📏 Line Spacing: 1.5 for all paragraphs")
    print("📚 Chapter Headings: 12pt before and after")
    print("📑 Section Headings (1.1, 2.3): 6pt before and after")
    print("📝 Subsection Headings (1.1.1): 6pt before and after")
    print("🖼️  Figure/Table Captions: 6pt before and after")
    print("📄 Regular Paragraphs: 0pt before and after")
    print("🧹 Empty Paragraphs: Maximum 1 between sections")


def main():
    print("IOST Document Formatter - Spacing Optimizer Tester")
    print("=" * 55)

    # Show spacing standards
    demonstrate_spacing_standards()

    if test_spacing_analysis():
        print("\n🎉 SPACING OPTIMIZATION TESTING COMPLETED!")
        print("\n📋 Next steps:")
        print("1. Open both documents in Word to compare spacing")
        print("2. Check that headings have proper spacing")
        print("3. Verify excessive empty paragraphs were removed")
        print("4. Confirm consistent 1.5 line spacing throughout")
        print("5. If satisfied, run: python main.py my_report.docx complete")

        print("\n🔧 Individual spacing optimization:")
        print("   python main.py my_report.docx spacing")
    else:
        print("\n❌ SPACING OPTIMIZATION TESTING FAILED!")
        print("Please check the error messages above")


if __name__ == "__main__":
    main()
