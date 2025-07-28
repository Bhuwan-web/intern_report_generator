#!/usr/bin/env python3
"""
Structure Verification Script
Verifies that the reorganized codebase structure works correctly
"""

import sys
import os
from pathlib import Path


def verify_imports():
    """Verify that all modules can be imported correctly"""
    print("🔍 Verifying Module Imports")
    print("=" * 40)

    # Add src to path
    src_path = Path(__file__).parent / "src"
    sys.path.insert(0, str(src_path))

    import_tests = [
        ("document_formatter", "IOSTDocumentFormatter"),
        ("enhanced_academic_tools", "DocumentAutoFixer"),
        ("enhanced_academic_tools", "auto_fix_document"),
        ("academic_line_break_manager", "AcademicLineBreakManager"),
        ("academic_line_break_manager", "process_document_line_breaks"),
        ("academic_tools", "LanguageChecker"),
        ("academic_tools", "CitationChecker"),
        ("academic_tools", "analyze_document"),
    ]

    success_count = 0

    for module_name, class_or_function in import_tests:
        try:
            module = __import__(module_name)
            if hasattr(module, class_or_function):
                print(f"   ✅ {module_name}.{class_or_function}")
                success_count += 1
            else:
                print(f"   ❌ {module_name}.{class_or_function} - Not found")
        except ImportError as e:
            print(f"   ❌ {module_name}.{class_or_function} - Import error: {e}")

    print(f"\n📊 Import Results: {success_count}/{len(import_tests)} successful")
    return success_count == len(import_tests)


def verify_file_structure():
    """Verify that all expected files are in the correct locations"""
    print("\n📁 Verifying File Structure")
    print("=" * 40)

    expected_files = [
        # Source files
        "src/__init__.py",
        "src/main.py",
        "src/document_formatter.py",
        "src/enhanced_academic_tools.py",
        "src/academic_tools.py",
        "src/academic_line_break_manager.py",
        "src/spacing_optimizer.py",
        "src/page_break_manager.py",
        "src/format_document.py",
        "src/install_dependencies.py",
        # Test files
        "tests/__init__.py",
        "tests/run_tests.py",
        "tests/test_document_formatter_fix.py",
        "tests/test_line_breaks.py",
        "tests/test_section_breaks.py",
        "tests/test_page_breaks.py",
        "tests/test_spacing.py",
        "tests/test_setup.py",
        # Root files
        "pyproject.toml",
        "requirements.txt",
        "README.md",
        "STRUCTURE.md",
    ]

    missing_files = []
    found_files = []

    for file_path in expected_files:
        if os.path.exists(file_path):
            print(f"   ✅ {file_path}")
            found_files.append(file_path)
        else:
            print(f"   ❌ {file_path} - Missing")
            missing_files.append(file_path)

    print(f"\n📊 File Structure: {len(found_files)}/{len(expected_files)} files found")

    if missing_files:
        print("\n⚠️  Missing files:")
        for file_path in missing_files:
            print(f"   - {file_path}")

    return len(missing_files) == 0


def verify_old_files_removed():
    """Verify that old test files have been removed from root"""
    print("\n🧹 Verifying Old Files Removed")
    print("=" * 40)

    old_files = [
        "test_line_breaks.py",
        "test_document_formatter_fix.py",
        "test_section_breaks.py",
    ]

    remaining_files = []

    for file_path in old_files:
        if os.path.exists(file_path):
            print(f"   ❌ {file_path} - Still exists (should be removed)")
            remaining_files.append(file_path)
        else:
            print(f"   ✅ {file_path} - Properly removed")

    print(
        f"\n📊 Cleanup: {len(old_files) - len(remaining_files)}/{len(old_files)} files properly removed"
    )

    return len(remaining_files) == 0


def verify_test_runner():
    """Verify that the test runner exists and is executable"""
    print("\n🧪 Verifying Test Runner")
    print("=" * 40)

    test_runner_path = "tests/run_tests.py"

    if os.path.exists(test_runner_path):
        print(f"   ✅ {test_runner_path} exists")

        # Check if it's executable
        if os.access(test_runner_path, os.X_OK):
            print(f"   ✅ {test_runner_path} is executable")
        else:
            print(f"   ⚠️  {test_runner_path} is not executable (may need chmod +x)")

        # Check if it has proper shebang
        with open(test_runner_path, "r") as f:
            first_line = f.readline().strip()
            if first_line.startswith("#!"):
                print(f"   ✅ Has proper shebang: {first_line}")
            else:
                print(f"   ⚠️  Missing shebang line")

        return True
    else:
        print(f"   ❌ {test_runner_path} not found")
        return False


def main():
    """Main verification function"""
    print("🚀 IOST Academic Tools - Structure Verification")
    print("=" * 60)

    # Run all verification checks
    checks = [
        ("File Structure", verify_file_structure),
        ("Module Imports", verify_imports),
        ("Old Files Cleanup", verify_old_files_removed),
        ("Test Runner", verify_test_runner),
    ]

    results = []

    for check_name, check_function in checks:
        try:
            result = check_function()
            results.append((check_name, result))
        except Exception as e:
            print(f"   ❌ Error in {check_name}: {e}")
            results.append((check_name, False))

    # Summary
    print("\n" + "=" * 60)
    print("📊 VERIFICATION SUMMARY")
    print("=" * 60)

    passed = sum(1 for _, success in results if success)
    total = len(results)

    for check_name, success in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"   {status} - {check_name}")

    print(f"\n🎯 Overall Result: {passed}/{total} checks passed")

    if passed == total:
        print("\n🎉 Structure verification completed successfully!")
        print("✅ The reorganized codebase is working correctly.")
        print("\n🚀 You can now use:")
        print("   - python tests/run_tests.py (run all tests)")
        print("   - python src/main.py document.docx complete (process documents)")
        return True
    else:
        print("\n⚠️  Some verification checks failed.")
        print("Please review the output above and fix any issues.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
