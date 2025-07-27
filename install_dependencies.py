#!/usr/bin/env python3
"""
Installation script for IOST Document Formatter dependencies
"""

import subprocess
import sys
import os


def install_package(package_name):
    """Install a package using pip"""
    try:
        print(f"📦 Installing {package_name}...")
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package_name], capture_output=True, text=True
        )

        if result.returncode == 0:
            print(f"✅ {package_name} installed successfully")
            return True
        else:
            print(f"❌ Failed to install {package_name}")
            print(f"Error: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error installing {package_name}: {e}")
        return False


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")

    if version.major >= 3 and version.minor >= 6:
        print("✅ Python version is compatible")
        return True
    else:
        print("❌ Python 3.6 or higher is required")
        return False


def main():
    print("IOST Document Formatter - Dependency Installer")
    print("=" * 50)

    # Check Python version
    if not check_python_version():
        print("Please upgrade Python to version 3.6 or higher")
        return

    # List of required packages
    required_packages = ["python-docx"]

    print(f"\n📋 Installing {len(required_packages)} required packages...")

    all_installed = True
    for package in required_packages:
        if not install_package(package):
            all_installed = False

    print("\n" + "=" * 50)

    if all_installed:
        print("🎉 ALL DEPENDENCIES INSTALLED SUCCESSFULLY!")
        print("\nNext steps:")
        print("1. Run: python test_setup.py")
        print("2. If tests pass, run: python main.py my_report.docx")
    else:
        print("❌ SOME INSTALLATIONS FAILED!")
        print("\nTry manual installation:")
        print("pip install python-docx")

    print("\n📁 Make sure these files are in your directory:")
    required_files = [
        "main.py",
        "document_formatter.py",
        "academic_tools.py",
        "enhanced_academic_tools.py",
        "test_setup.py",
    ]

    for file_name in required_files:
        if os.path.exists(file_name):
            print(f"✅ {file_name}")
        else:
            print(f"❌ {file_name} - MISSING!")


if __name__ == "__main__":
    main()
