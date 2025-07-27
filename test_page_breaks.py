#!/usr/bin/env python3
"""
Test script specifically for page break functionality
"""

import sys
import os
from page_break_manager import PageBreakManager, optimize_document_breaks


def test_page_break_detection():
    """Test page break detection on your document"""

    if not os.path.exists("my_report.docx"):
        print("❌ my_report.docx not found!")
        print("Please make sure your document is in the current directory")
        return False

    try:
        print("🔍 ANALYZING PAGE BREAKS IN YOUR DOCUMENT")
        print("=" * 50)

        manager = PageBreakManager("my_report.docx")

        # Generate detailed report
        manager.generate_break_report()

        print("\n🧪 TESTING PAGE BREAK OPTIMIZATION")
        print("=" * 50)

        # Test optimization
        result = optimize_document_breaks("my_report.docx", "test_optimized_report.docx")

        if result:
            print(f"\n✅ SUCCESS! Test optimization completed")
            print(f"📄 Original: my_report.docx")
            print(f"📄 Optimized: test_optimized_report.docx")
            print("\n💡 Compare both files in Word to see the differences")

            # Clean up test file
            if os.path.exists("test_optimized_report.docx"):
                print(f"\n🗑️  Test file created: test_optimized_report.docx")
                print("   You can delete this after reviewing")

            return True
        else:
            print("❌ Optimization test failed")
            return False

    except Exception as e:
        print(f"❌ Error during testing: {str(e)}")
        return False


def main():
    print("IOST Document Formatter - Page Break Tester")
    print("=" * 50)

    if test_page_break_detection():
        print("\n🎉 PAGE BREAK TESTING COMPLETED!")
        print("\n📋 Next steps:")
        print("1. Open both documents in Word to compare")
        print("2. Check that chapters now have proper page breaks")
        print("3. Verify unnecessary breaks were removed")
        print("4. If satisfied, run: python main.py my_report.docx complete")
    else:
        print("\n❌ PAGE BREAK TESTING FAILED!")
        print("Please check the error messages above")


if __name__ == "__main__":
    main()
